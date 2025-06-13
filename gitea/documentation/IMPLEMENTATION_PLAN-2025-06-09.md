# Implementation Plan: Gitea Git Server Deployment in Isengard

This document provides step-by-step instructions for deploying the Gitea git server in an Isengard account, following the architecture outlined in the High-Level Design document and Component Diagram.

## Prerequisites

Before beginning the implementation, ensure you have:

1. **Isengard Account Access**: Admin access to your Isengard account in the us-west-2 region
2. **AWS CLI**: Configured with appropriate credentials
3. **SSH Key Pair**: Created or imported into your AWS account for EC2 access
4. **Basic AWS Knowledge**: Familiarity with EC2, S3, and networking concepts

## Phase 1: Infrastructure Setup

### Step 1: Set up Virtual Private Cloud (VPC)

1. Use the default VPC in your Isengard account or create a new one:

   ```bash
   aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region us-west-2
   ```

2. Create a subnet in the VPC:

   ```bash
   aws ec2 create-subnet --vpc-id vpc-xxxxxxxx --cidr-block 10.0.1.0/24 --availability-zone us-west-2a --region us-west-2
   ```

3. Create an Internet Gateway and attach it to your VPC:

   ```bash
   aws ec2 create-internet-gateway --region us-west-2
   aws ec2 attach-internet-gateway --internet-gateway-id igw-xxxxxxxx --vpc-id vpc-xxxxxxxx --region us-west-2
   ```

4. Create a route table and add a route to the Internet:

   ```bash
   aws ec2 create-route-table --vpc-id vpc-xxxxxxxx --region us-west-2
   aws ec2 create-route --route-table-id rtb-xxxxxxxx --destination-cidr-block 0.0.0.0/0 --gateway-id igw-xxxxxxxx --region us-west-2
   aws ec2 associate-route-table --route-table-id rtb-xxxxxxxx --subnet-id subnet-xxxxxxxx --region us-west-2
   ```

### Step 2: Create Security Group

Create a security group for the Gitea server:

```bash
aws ec2 create-security-group --group-name gitea-sg --description "Security group for Gitea server" --vpc-id vpc-xxxxxxxx --region us-west-2
```

Add necessary inbound rules:

```bash
# Allow HTTPS access
aws ec2 authorize-security-group-ingress --group-id sg-xxxxxxxx --protocol tcp --port 443 --cidr 0.0.0.0/0 --region us-west-2

# Allow SSH access (restrict to your IP for better security)
aws ec2 authorize-security-group-ingress --group-id sg-xxxxxxxx --protocol tcp --port 22 --cidr YOUR_IP/32 --region us-west-2

# Allow HTTP temporarily for Let's Encrypt verification (can be removed later)
aws ec2 authorize-security-group-ingress --group-id sg-xxxxxxxx --protocol tcp --port 80 --cidr 0.0.0.0/0 --region us-west-2
```

### Step 3: Create EBS Volume

Create an EBS volume for persistent storage:

```bash
aws ec2 create-volume --availability-zone us-west-2a --size 20 --volume-type gp3 --region us-west-2
```

### Step 4: Launch EC2 Instance

Launch an EC2 instance:

```bash
aws ec2 run-instances \
  --image-id ami-0c101f26f147fa7fd \  # Amazon Linux 2 AMI (adjust as needed)
  --instance-type t3.small \
  --key-name YOUR_KEY_NAME \
  --security-group-ids sg-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx \
  --block-device-mappings 'DeviceName=/dev/sda1,Ebs={VolumeSize=8}' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=GitServer}]' \
  --region us-west-2
```

### Step 5: Allocate and Associate Elastic IP

Allocate an Elastic IP address and associate it with your instance:

```bash
aws ec2 allocate-address --domain vpc --region us-west-2
aws ec2 associate-address --instance-id i-xxxxxxxx --allocation-id eipalloc-xxxxxxxx --region us-west-2
```

Note your Elastic IP address for later use.

### Step 6: Attach EBS Volume

Attach the EBS volume to your instance:

```bash
aws ec2 attach-volume --volume-id vol-xxxxxxxx --instance-id i-xxxxxxxx --device /dev/sdf --region us-west-2
```

## Phase 2: Server Configuration

### Step 1: Connect to the EC2 Instance

Connect to your instance via SSH:

```bash
ssh -i /path/to/your-key.pem ec2-user@YOUR_ELASTIC_IP
```

### Step 2: Update the System

Update the package list and install system updates:

```bash
sudo yum update -y
```

### Step 3: Format and Mount the EBS Volume

Prepare the EBS volume:

```bash
# Check the volume name
lsblk

# Format the volume (typically xvdf for the device we attached earlier)
sudo mkfs -t ext4 /dev/xvdf

# Create a mount point
sudo mkdir -p /data

# Mount the volume
sudo mount /dev/xvdf /data

# Add to fstab for automatic mounting on reboot
echo '/dev/xvdf /data ext4 defaults,nofail 0 2' | sudo tee -a /etc/fstab

# Create directory for Docker volumes
sudo mkdir -p /data/docker-volumes
```

### Step 4: Install Docker and Docker Compose

Install Docker:

```bash
sudo amazon-linux-extras install docker -y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user
```

Install Docker Compose:

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Log out and back in for the group changes to take effect:

```bash
exit
# reconnect via SSH
ssh -i /path/to/your-key.pem ec2-user@YOUR_ELASTIC_IP
```

## Phase 3: Gitea Deployment

### Step 1: Create Docker Compose Configuration

Create a directory for Gitea configuration:

```bash
mkdir -p ~/gitea
cd ~/gitea
```

Create a `docker-compose.yml` file:

```bash
cat > docker-compose.yml << 'EOF'
version: '3'

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__server__DOMAIN=YOUR_ELASTIC_IP
      - GITEA__server__ROOT_URL=https://YOUR_ELASTIC_IP/
      - GITEA__server__SSH_DOMAIN=YOUR_ELASTIC_IP
      - GITEA__server__PROTOCOL=https
    restart: always
    volumes:
      - /data/docker-volumes/gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "80:3000"
      - "443:3000" 
      - "22:22"
    networks:
      - gitea

networks:
  gitea:
    external: false
EOF
```

Replace `YOUR_ELASTIC_IP` with your actual Elastic IP address.

### Step 2: Start Gitea

Start the Gitea container:

```bash
docker-compose up -d
```

### Step 3: Configure Initial Setup

Access the Gitea web interface by navigating to `http://YOUR_ELASTIC_IP` in your browser.

Complete the initial setup:

1. Database Settings:
   - Select SQLite3 (simplest option)
   - Keep the default path

2. General Settings:
   - Set the Site Title (e.g., "AWS Teaching Git Server")
   - Set the Repository Root Path (default is fine)
   - Set the Server Domain to your Elastic IP
   - Set the Gitea Base URL to `https://YOUR_ELASTIC_IP/`
   - Disable user registration (you can create accounts manually)

3. Admin Account Settings:
   - Create an admin username and strong password
   - Provide your email address

4. Click "Install Gitea" to complete the setup

## Phase 4: HTTPS Configuration

### Step 1: Generate SSL Certificate with Let's Encrypt

Install Certbot:

```bash
sudo amazon-linux-extras install epel -y
sudo yum install certbot -y
```

Stop the Gitea container temporarily:

```bash
cd ~/gitea
docker-compose down
```

Obtain SSL certificate:

```bash
sudo certbot certonly --standalone --preferred-challenges http -d YOUR_ELASTIC_IP --agree-tos --email YOUR_EMAIL
```

### Step 2: Update Docker Compose for HTTPS

Update the `docker-compose.yml` file to use the SSL certificates:

```bash
cat > docker-compose.yml << 'EOF'
version: '3'

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__server__DOMAIN=YOUR_ELASTIC_IP
      - GITEA__server__ROOT_URL=https://YOUR_ELASTIC_IP/
      - GITEA__server__SSH_DOMAIN=YOUR_ELASTIC_IP
      - GITEA__server__PROTOCOL=https
      - GITEA__server__CERT_FILE=/data/ssl/fullchain.pem
      - GITEA__server__KEY_FILE=/data/ssl/privkey.pem
    restart: always
    volumes:
      - /data/docker-volumes/gitea:/data
      - /etc/letsencrypt/live/YOUR_ELASTIC_IP/fullchain.pem:/data/ssl/fullchain.pem:ro
      - /etc/letsencrypt/live/YOUR_ELASTIC_IP/privkey.pem:/data/ssl/privkey.pem:ro
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "80:3000"
      - "443:3000"
      - "22:22"
    networks:
      - gitea

networks:
  gitea:
    external: false
EOF
```

Replace `YOUR_ELASTIC_IP` with your actual Elastic IP address.

### Step 3: Restart Gitea with HTTPS

```bash
docker-compose up -d
```

## Phase 5: Backup Configuration

### Step 1: Create S3 Bucket

Create an S3 bucket for backups:

```bash
aws s3 mb s3://gitea-backups-YOUR_ACCOUNT_ID --region us-west-2
```

Configure lifecycle policy for the bucket (optional):

```bash
cat > lifecycle.json << 'EOF'
{
  "Rules": [
    {
      "ID": "Delete old backups",
      "Status": "Enabled",
      "Prefix": "",
      "Expiration": {
        "Days": 30
      }
    }
  ]
}
EOF

aws s3api put-bucket-lifecycle-configuration --bucket gitea-backups-YOUR_ACCOUNT_ID --lifecycle-configuration file://lifecycle.json
```

### Step 2: Create Backup Script

Create a backup script:

```bash
cat > ~/backup-gitea.sh << 'EOF'
#!/bin/bash

# Set variables
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_DIR="/tmp/gitea-backup-${TIMESTAMP}"
S3_BUCKET="s3://gitea-backups-YOUR_ACCOUNT_ID"

# Create temporary backup directory
mkdir -p $BACKUP_DIR

# Stop Gitea container
cd ~/gitea
docker-compose stop gitea

# Create backup archive
tar -czf "${BACKUP_DIR}/gitea-backup-${TIMESTAMP}.tar.gz" -C /data/docker-volumes gitea

# Start Gitea container
docker-compose start gitea

# Upload to S3
aws s3 cp "${BACKUP_DIR}/gitea-backup-${TIMESTAMP}.tar.gz" "${S3_BUCKET}/gitea-backup-${TIMESTAMP}.tar.gz"

# Clean up
rm -rf $BACKUP_DIR

echo "Backup completed and uploaded to ${S3_BUCKET}/gitea-backup-${TIMESTAMP}.tar.gz"
EOF
```

Make the script executable:

```bash
chmod +x ~/backup-gitea.sh
```

### Step 3: Schedule Automated Backups

Add a cron job to run the backup daily:

```bash
(crontab -l 2>/dev/null; echo "0 2 * * * ~/backup-gitea.sh >> ~/backup-gitea.log 2>&1") | crontab -
```

## Phase 6: Testing and Validation

### Step 1: Test HTTPS Access

Access your Gitea server via the secure URL:

```url
https://YOUR_ELASTIC_IP
```

Verify the connection is secure (green padlock in browser).

### Step 2: Test User Creation

1. Log in with the admin account
2. Create a test user account
3. Verify login functionality

### Step 3: Test Git Operations

Create a test repository:

1. Log in to Gitea
2. Create a new repository
3. Clone the repository to your local machine:

   ```bash
   git clone https://YOUR_ELASTIC_IP/username/test-repo.git
   ```

4. Make changes, commit, and push:

   ```bash
   cd test-repo
   echo "# Test Repository" > README.md
   git add README.md
   git commit -m "Initial commit"
   git push
   ```

5. Verify changes appear in the web interface

### Step 4: Test Backup and Restore

1. Run the backup script manually:

   ```bash
   ~/backup-gitea.sh
   ```

2. Verify the backup file exists in the S3 bucket:

   ```bash
   aws s3 ls s3://gitea-backups-YOUR_ACCOUNT_ID/
   ```

Optionally, test restoration:

1. Download the backup:

   ```bash
   aws s3 cp s3://gitea-backups-YOUR_ACCOUNT_ID/gitea-backup-TIMESTAMP.tar.gz .
   ```

2. Stop Gitea:

   ```bash
   cd ~/gitea
   docker-compose stop gitea
   ```

3. Extract the backup (be careful with this command in a production setting):

   ```bash
   # Create a temporary restoration directory
   mkdir -p /tmp/gitea-restore
   tar -xzf gitea-backup-TIMESTAMP.tar.gz -C /tmp/gitea-restore
   
   # Verify contents
   ls -la /tmp/gitea-restore
   ```

4. Start Gitea again:

   ```bash
   docker-compose start gitea
   ```

## Maintenance Procedures

### Updating Gitea

To update Gitea to the latest version:

```bash
cd ~/gitea
docker-compose pull
docker-compose down
docker-compose up -d
```

### Monitoring Logs

View Gitea logs:

```bash
cd ~/gitea
docker-compose logs -f gitea
```

### Troubleshooting

If you encounter issues:

1. Check container status:

   ```bash
   docker ps -a
   ```

2. Check container logs:

   ```bash
   cd ~/gitea
   docker-compose logs gitea
   ```

3. Verify disk space:

   ```bash
   df -h
   ```

4. Check backup logs:

   ```bash
   cat ~/backup-gitea.log
   ```

## Security Recommendations

1. **Restrict SSH Access**: Update security group to allow SSH only from your specific IP addresses
2. **Regularly Update**: Keep the system, Docker, and Gitea updated
3. **Monitor Logs**: Regularly check logs for suspicious activity
4. **Backup Verification**: Periodically verify backup integrity
5. **Strong Passwords**: Enforce strong passwords for all user accounts

## Conclusion

You now have a functional Gitea git server running in your Isengard account. This server provides:

- Secure repository hosting with HTTPS
- User management with local authentication
- Persistent storage on EBS
- Automated daily backups to S3
- A simple, maintainable architecture

This implementation meets the requirements for hosting demo projects for teaching coding on AWS, with minimal administrative overhead and good security practices.
