#!/bin/bash

# Specify size in GiB (e.g., 20)
SIZE=${1:-20}

# Get instance metadata
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
INSTANCEID=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
REGION=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/region)

# Get the EBS volume ID
VOLUMEID=$(aws ec2 describe-instances \
  --instance-id $INSTANCEID \
  --query "Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId" \
  --output text \
  --region $REGION)

# Resize the EBS volume
aws ec2 modify-volume --volume-id $VOLUMEID --size $SIZE

# Wait for the resize to finish with timeout
TIMEOUT=300  # 5 minutes timeout
ELAPSED=0
echo "Waiting for volume modification to complete..."
while [ $ELAPSED -lt $TIMEOUT ]; do
    STATUS=$(aws ec2 describe-volumes-modifications \
        --volume-id $VOLUMEID \
        --filters Name=modification-state,Values="optimizing","completed" \
        --query "length(VolumesModifications)" \
        --output text)
    
    if [ "$STATUS" = "1" ]; then
        echo "Volume modification completed"
        break
    fi
    
    sleep 10
    ELAPSED=$((ELAPSED + 10))
    echo "Still waiting... ($ELAPSED seconds elapsed)"
done

if [ $ELAPSED -ge $TIMEOUT ]; then
    echo "Timeout waiting for volume modification"
    exit 1
fi

# Check if we're on an NVMe filesystem
if [[ -e "/dev/xvda" && $(readlink -f /dev/xvda) = "/dev/xvda" ]]; then
    echo "Processing xvda device..."
    sudo growpart /dev/xvda 1
    
    # Check if we're on AL2 or AL2023
    STR=$(cat /etc/os-release)
    SUBAL2="VERSION_ID=\"2\""
    SUBAL2023="VERSION_ID=\"2023\""
    if [[ "$STR" == *"$SUBAL2"* || "$STR" == *"$SUBAL2023"* ]]; then
        sudo xfs_growfs -d /
    else
        sudo resize2fs /dev/xvda1
    fi
else
    echo "Processing nvme device..."
    sudo growpart /dev/nvme0n1 1
    
    # Check if we're on AL2 or AL2023
    STR=$(cat /etc/os-release)
    SUBAL2="VERSION_ID=\"2\""
    SUBAL2023="VERSION_ID=\"2023\""
    if [[ "$STR" == *"$SUBAL2"* || "$STR" == *"$SUBAL2023"* ]]; then
        sudo xfs_growfs -d /
    else
        sudo resize2fs /dev/nvme0n1p1
    fi
fi

echo "Resize operation completed"
exit 0