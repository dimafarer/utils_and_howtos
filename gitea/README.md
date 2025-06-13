# Gitea Server on AWS

This project sets up a Gitea Git server on AWS using CloudFormation.

## Architecture Overview

The CloudFormation template creates the following resources:

- **VPC**: A dedicated VPC with CIDR block 10.0.0.0/16
- **Public Subnet**: A public subnet in the first availability zone
- **Internet Gateway**: For internet access
- **Route Table**: With routes for internet access
- **Security Group**: Allowing SSH, HTTP, HTTPS, and Gitea port access
- **EC2 Instance**: Running Amazon Linux 2 with Docker
- **EBS Volume**: For persistent Gitea data storage
- **Elastic IP**: For a static public IP address
- **S3 Bucket**: For automated backups
- **IAM Role**: Allowing the EC2 instance to access S3 for backups

## Deployment Instructions

### Prerequisites

1. AWS CLI installed and configured with appropriate credentials
2. An SSH key pair in your AWS account (or create a new one)

### Deployment Steps

1. Create a new key pair (if needed):

   ```bash
   aws ec2 create-key-pair --key-name gitea-key --query 'KeyMaterial' --output text > gitea-key.pem
   chmod 400 gitea-key.pem
   ```

2. Deploy the CloudFormation stack:

   ```bash
   aws cloudformation create-stack \
     --stack-name gitea-server \
     --template-body file://gitea-infrastructure.yaml \
     --parameters \
       ParameterKey=KeyName,ParameterValue=gitea-key \
       ParameterKey=InstanceType,ParameterValue=t3.small \
     --capabilities CAPABILITY_IAM
   ```

3. Monitor the stack creation:

   ```bash
   aws cloudformation describe-stacks --stack-name gitea-server
   ```

4. Once the stack is created, get the outputs:

   ```bash
   aws cloudformation describe-stacks --stack-name gitea-server --query 'Stacks[0].Outputs'
   ```

5. **Important**: After the stack is created, you need to SSH into the instance and fix the Docker configuration. See the [Post-Deployment Configuration](#post-deployment-configuration) section below.

## Post-Deployment Configuration

After the CloudFormation stack is created, you need to manually configure the Gitea container:

1. SSH into the EC2 instance:
   ```bash
   ssh -i gitea-key.pem ec2-user@<instance-public-dns>
   ```

2. Update the docker-compose.yml file to use port 2222 instead of 22 for SSH:
   ```bash
   cd ~/gitea
   
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
   ```

3. Start the Gitea container with the correct domain:
   ```bash
   # Manually set the public DNS name
   PUBLIC_DNS=<your-instance-public-dns>
   
   # Start the container
   DOMAIN=$PUBLIC_DNS docker-compose up -d
   ```

4. Verify the container is running:
   ```bash
   docker-compose ps
   ```

## Initial Configuration

After the container is running:

1. Access the Gitea web interface using the URL from the stack outputs
2. Follow the Gitea setup wizard to complete the initial configuration:
   - Database: SQLite3 (default)
   - Site Title: Your preferred name
   - Repository Root Path: /data/git/repositories
   - Log Path: /data/gitea/log
   - Server Domain: Use the public DNS name of your instance
   - Gitea Base URL: http://[your-instance-dns]/
   - SSH Server Domain: Same as Server Domain
   - SSH Server Port: 2222 (important: we changed this from the default 22)
   - Gitea HTTP Listen Port: 3000
3. Create the admin account with your preferred credentials

## Backup and Restore

The system is configured to automatically back up Gitea data to S3 daily at 2 AM. The backups are stored in the S3 bucket created by the stack and are retained for 30 days.

To manually trigger a backup:

```bash
ssh -i gitea-key.pem ec2-user@<instance-ip>
sudo /home/ec2-user/backup-gitea.sh
```

To restore from a backup:

1. Download the backup from S3
2. Stop the Gitea container
3. Extract the backup to the appropriate location
4. Start the Gitea container

## Security Considerations

- The template creates security groups that allow access from anywhere (0.0.0.0/0) to ports 80, 443, and 3000
- SSH access is restricted based on the `AllowSSHFrom` parameter (default: 0.0.0.0/0)
- Consider restricting these to specific IP ranges for production use
- Git SSH operations use port 2222 instead of the default 22

## Maintenance

- **System Updates**: The EC2 instance is configured to update on launch, but regular updates should be applied
- **Gitea Updates**: Update Gitea by updating the Docker image version in the docker-compose.yml file
- **Monitoring**: Consider adding CloudWatch alarms for monitoring system health
- **Restarting**: If the instance is restarted, you'll need to manually start the Gitea container again with:
  ```bash
  cd ~/gitea
  DOMAIN=<your-instance-public-dns> docker-compose up -d
  ```