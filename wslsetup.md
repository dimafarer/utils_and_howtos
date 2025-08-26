# WSL Setup

## What is wsl?

wsl (Windows Subsystem for Linux) allows windows based developers to work in a linux environment. From Windows 10 (version 2004+) forword wsl is a pre-installed as a powershell command. After installation the

```powershell
wsl
```

command  with no flags will launch the default wsl linux instance. Before installation the **wsl** command by itself will cause and error.  
before installation you may list wsl instances you can install.

```powershell
wsl --list --online
```

will show all your remote wsl linux options.
you can also list your local options

```powershell
wsl --list 
```

its unlikly you will have any local options if you are installing wsl right now.

## easy installation

1. list you avalible instances

```powershell
wsl --list --online
```

2. run **wsl install** with one of the listed options. this one command will complete the full installation, including 
- Enable all necessary Windows features
- Install the WSL subsystem
- Download and install Ubuntu 24.04
- Set Ubuntu 24.04 as your default Linux distribution
- including restarting the computer if nessarry.
- it will automaticlly start wsl  
ex:

```powershell
wsl --install -d Ubuntu-24.04
```

3. once installation is complete you will be on the bash command line. type

```bash
exit
```

to return to powershell

4. install the vscode wsl extention

5. click the blue remote button at the bottom left of the ide

6. choose "connect to wsl from the pop-up window to choose the default wsl instance you previously installed.

## wsl instance clone

to install a clean root version of Ubuntu24.04 to make local instances

1. dowload the WSL version you want and then create the insteance from it before you modify it.
2. it will ask you to make a user as part of the instalation proccess.
3. at this point your commandline is inside the new WSL instance (not Windows). it will ask you to set up a user and password
4. close the command line to go back to your system powershell
5. Create a directory to store the download  

```bash
# make a folder to hold to the distribution. 
mkdir Ubuntu24-Root
cd Ubuntu24-Root
# export a wsl distribution to your local file system
wsl --export Ubuntu-24.04 "C:\Users\dimfarer\Ubuntu24-Root\ubuntu24-backup.tar.gz"
# you could use this directly but if you want multiple versions then import the version you just exported to local with a new name and new location
wsl --import [yourcustomenvname] "C:\Users\dimfarer\[yourcustomenvname]" "C:\Users\dimfarer\Ubuntu24-Root\ubuntu24-backup.tar.gz"

# To verify your installations:
wsl --list
# To launch a specific instance use your IDE WSL plugin or:
wsl -d [yourcustomenvname] # For Python development

# Note: By default, the imported distribution will log you in as root. To set up a default user:
# From inside the WSL instance
NEW_USER=yourusername
useradd -m -G sudo -s /bin/bash "$NEW_USER"
passwd "$NEW_USER"
# Still inside WSL
echo -e "[user]\ndefault=$NEW_USER" > /etc/wsl.conf
# Exit WSL and restart the instance:
# In PowerShell
wsl --terminate Ubuntu24-Root
wsl -d Ubuntu24-Root  
```

## Install Q For Devlopers

* click extension
* Do A search for Q in the search bar
* click install
* follow auth instructions for web authentication via your devloperID

## Update OS

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl unzip python3.12-venv gcc python3-dev libkrb5-dev
# you make also need  
```

## AWS CLI

```bash
mkdir ~/temp
cd temp
curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip
unzip awscliv2.zip 
sudo ./aws/install
cd ~
rm -rf ~/temp
# run aws configure and input your credentials
aws configure
# or 
# get the AWS plugin and log in and login with your credentials
```

## AWS SAM CLI

```bash
# Create a temporary directory for the download
mkdir -p ~/tmp/sam-install
cd ~/tmp/sam-install

# Download the SAM CLI installer
curl -Lo aws-sam-cli-linux-x86_64.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip

# Unzip and install
mkdir sam-installation
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install

# Verify the installation
sam --version

# Clean up - remove the temporary directory
cd ~
rm -rf ~/tmp/sam-install
```

## Install Node

```bash
# use node version manager to install node
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# Install the latest LTS version of Node.js (which meets Amplify Gen 2's requirement of Node.js v18.16.0 or later):
# you must close and re-open the terminal to use nvm
nvm install 20
nvm use 20
nvm alias default 20
```

## Install Amplify CLI

```bash
npm install -g @aws-amplify/cli@latest
```

### Clone  Starter Project

* go to https://docs.amplify.aws/react/start/quickstart/
* click "create repository from template" to create an Amplify starter app git server repo in your account git service account 
* once the repo has been created click "deploy to aws" which will lead you through the setup of a new Amplify project that will be driven by a CICD proccess triggered by updates to the git server repo ; (the one you created in the previous step)
* View your deployed website
* download the amplify_outputs.json 

```bash
mkdir projects
cd projects
git clone [git server repo url]
```

* copy amplify_outputs.json to project root

```bash
cd amplify-vite-react-template
npm install
```

### Create a dev sandbox and add delete functionality

```bash
npx ampx sandbox
```
