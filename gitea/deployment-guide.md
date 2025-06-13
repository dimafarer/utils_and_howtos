# Gitea Server Deployment Guide

This guide provides step-by-step instructions for deploying a Gitea Git server on AWS using the CloudFormation template.

## Step 1: Prepare Your Environment

Ensure you have:
- AWS CLI installed and configured
- Appropriate AWS permissions to create resources
- A terminal or command prompt

## Step 2: Create a Key Pair

Create a new SSH key pair for accessing your EC2 instance:

```bash
aws ec2 create-key-pair --key-name gitea-key --query 'KeyMaterial' --output text > gitea-key.pem
chmod 400 gitea-key.pem
```

## Step 3: Deploy the CloudFormation Stack

Deploy the CloudFormation template:

```bash
aws cloudformation create-stack \
  --stack-name gitea-server \
  --template-body file://gitea-infrastructure.yaml \
  --parameters \
    ParameterKey=KeyName,ParameterValue=gitea-key \
    ParameterKey=InstanceType,ParameterValue=t3.small \
  --capabilities CAPABILITY_IAM
```

<!-- Replace `YOUR_IP_ADDRESS` with your public IP address to restrict SSH access. -->

## Step 4: Monitor Stack Creation

Check the status of your stack:

```bash
aws cloudformation describe-stacks --stack-name gitea-server --query 'Stacks[0].StackStatus'
```

Wait until the status is `CREATE_COMPLETE`.

## Step 5: Get Stack Outputs

Retrieve important information about your deployment:

```bash
aws cloudformation describe-stacks --stack-name gitea-server --query 'Stacks[0].Outputs'
```

This will provide:
- The URL to access your Gitea server
- The SSH command to connect to your instance
- The S3 bucket name for backups

## Step 6: Fix Docker Container Configuration

After the stack is created, you need to SSH into the instance and fix the Docker configuration:

```bash
# SSH into the instance using the key pair and the public DNS name from the stack outputs
ssh -i gitea-key.pem ec2-user@<instance-public-dns>

# Navigate to the Gitea directory
cd ~/gitea

# Update the docker-compose.yml file to use port 2222 instead of 22 for SSH
cat > docker-compose.yml << 'EOF'
version: '3'

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__server__DOMAIN=${DOMAIN}
      - GITEA__server__ROOT_URL=http://${DOMAIN}/
      - GITEA__server__SSH_DOMAIN=${DOMAIN}
      - GITEA__server__SSH_PORT=2222
    restart: always
    volumes:
      - /data/docker-volumes/gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "80:3000"
      - "443:3000" 
      - "2222:22"
    networks:
      - gitea

networks:
  gitea:
    external: false
EOF

# Set the domain to the instance's public DNS name
PUBLIC_DNS=$(curl -s http://169.254.169.254/latest/meta-data/public-hostname)

# If the above command doesn't work, manually set the public DNS name
# PUBLIC_DNS=<your-instance-public-dns>

# Start the Gitea container with the correct domain
DOMAIN=$PUBLIC_DNS docker-compose up -d

# Verify the container is running
docker-compose ps
```

## Step 7: Access Your Gitea Server

1. Open the Gitea URL in your web browser (from the stack outputs)
2. You'll be redirected to the Gitea installation page
3. Configure the following settings:
   - Database: SQLite3 (default)
   - Site Title: Your preferred name
   - Repository Root Path: /data/git/repositories
   - Log Path: /data/gitea/log
   - Server Domain: Use the public DNS name of your instance
   - Gitea Base URL: http://[your-instance-dns]/
   - SSH Server Domain: Same as Server Domain
   - SSH Server Port: 2222 (important: we changed this from the default 22)
   - Gitea HTTP Listen Port: 3000

4. Create the admin account with your preferred credentials

## Step 7: Secure Your Gitea Server

For production use, consider:

1. Setting up HTTPS with Let's Encrypt:
   ```bash
   ssh -i gitea-key.pem ec2-user@<instance-ip>
   cd ~/gitea
   # Edit docker-compose.yml to add Let's Encrypt configuration
   ```

2. Restricting access in the security group:
   ```bash
   aws ec2 update-security-group-rule-descriptions-ingress \
     --group-id <security-group-id> \
     --ip-permissions '[{"IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "IpRanges": [{"CidrIp": "YOUR_IP_ADDRESS/32", "Description": "SSH access"}]}]'
   ```

## Step 8: Test Backup and Restore

1. Manually trigger a backup:
   ```bash
   ssh -i gitea-key.pem ec2-user@<instance-ip>
   sudo /home/ec2-user/backup-gitea.sh
   ```

2. Verify the backup was created in S3:
   ```bash
   aws s3 ls s3://gitea-backups-<account-id>/
   ```

## Troubleshooting

### Common Issues

1. **Cannot connect to the EC2 instance**:
   - Verify the security group allows SSH from your IP
   - Check that you're using the correct key pair

2. **Gitea is not accessible**:
   - Check the EC2 instance status
   - Verify the security group allows traffic on port 80/443/3000
   - Check Docker container status: `docker ps`

3. **Backup failures**:
   - Check IAM permissions for S3 access
   - Verify the S3 bucket exists
   - Check the backup script logs: `cat ~/backup-gitea.log`

### Logs to Check

- EC2 system logs: `/var/log/cloud-init-output.log`
- Docker logs: `docker logs gitea`
- Backup logs: `/home/ec2-user/backup-gitea.log`