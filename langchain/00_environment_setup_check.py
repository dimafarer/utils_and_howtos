#!/usr/bin/env python3
"""
Environment Setup Checker for LangChain + AWS Bedrock

This is the FIRST file you should run before starting the LangChain examples.
It checks that your computer has everything needed to run AI chatbots with AWS.

What this file checks:
1. Python version (needs 3.8 or higher)
2. Required Python packages are installed
3. AWS credentials are configured
4. AWS Bedrock access is working

Run this with: python 00_environment_setup.py
"""

# Import Python's built-in modules
import sys  # For checking Python version
import boto3  # AWS SDK for Python - lets us talk to AWS services
from botocore.exceptions import NoCredentialsError, ClientError  # AWS error types

def check_python_version():
    """
    Check if Python version is 3.8 or higher.
    
    LangChain and AWS Bedrock need modern Python features,
    so we need at least Python 3.8.
    
    Returns:
        bool: True if Python version is good, False if too old
    """
    # Get the current Python version (like 3.12.0)
    version = sys.version_info
    
    # Check if it's Python 3.8 or newer
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} - Need Python 3.8+")
        print("   Please upgrade Python from https://python.org")
        return False

def check_dependencies():
    """
    Check if required Python packages are installed.
    
    We need several packages to make LangChain work with AWS:
    - langchain: The main AI framework
    - langchain-aws: Connects LangChain to AWS services
    - langchain-community: Extra LangChain features
    - boto3: AWS SDK for Python
    
    Returns:
        bool: True if all packages are installed, False if any are missing
    """
    # List of packages we need for the examples
    required_packages = [
        'langchain',        # Main LangChain framework
        'langchain_aws',    # AWS integration for LangChain
        'langchain_community',  # Community features (chat history, etc.)
        'boto3'            # AWS SDK - lets Python talk to AWS
    ]
    
    # Keep track of any missing packages
    missing_packages = []
    
    # Check each package one by one
    for package in required_packages:
        try:
            # Try to import the package
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            # Package is not installed
            print(f"❌ {package} - not installed")
            missing_packages.append(package)
    
    # If any packages are missing, show how to install them
    if missing_packages:
        print(f"\nInstall missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def check_aws_credentials():
    """
    Check if AWS credentials are configured and Bedrock is accessible.
    
    AWS credentials are like a username/password for AWS services.
    Without them, we can't use Bedrock (AWS's AI service).
    
    Returns:
        bool: True if AWS is set up correctly, False if there are issues
    """
    try:
        # Create an AWS session - this is like logging into AWS
        session = boto3.Session()
        credentials = session.get_credentials()
        
        # Check if we found any credentials
        if credentials is None:
            print("❌ No AWS credentials found")
            print("   Run: aws configure")
            print("   You'll need your AWS Access Key ID and Secret Access Key")
            return False
        
        print("✅ AWS credentials configured")
        
        # Now test if we can actually use Bedrock (AWS's AI service)
        # Note: We use 'bedrock' client to list models, 'bedrock-runtime' for inference
        bedrock_client = boto3.client('bedrock')
        
        # Try to list available AI models - this tests our permissions
        try:
            bedrock_client.list_foundation_models()
            print("✅ Bedrock access confirmed")
            return True
        except ClientError as e:
            # AWS returned an error - figure out what went wrong
            error_code = e.response['Error']['Code']
            if error_code == 'AccessDeniedException':
                print("❌ Bedrock access denied - check IAM permissions")
                print("   Your AWS user needs Bedrock permissions")
            else:
                print(f"❌ Bedrock error: {error_code}")
            return False
            
    except NoCredentialsError:
        # This happens when AWS credentials aren't set up at all
        print("❌ AWS credentials not configured")
        print("   Run: aws configure")
        print("   You'll need your AWS Access Key ID and Secret Access Key")
        return False
    except Exception as e:
        # Catch any other unexpected errors
        print(f"❌ AWS setup error: {e}")
        return False

def main():
    """
    Run all environment checks in the right order.
    
    This function runs all our checks and gives a final summary.
    If anything fails, the program exits with an error.
    """
    print("=== LangChain + AWS Bedrock Environment Check ===")
    print("This checks if your computer is ready for AI chatbot development!\n")
    
    # List of checks to run, in order
    # Each check has a name and a function to call
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("AWS Setup", check_aws_credentials)
    ]
    
    # Keep track of whether all checks passed
    all_passed = True
    
    # Run each check
    for check_name, check_func in checks:
        print(f"Checking {check_name}...")
        if not check_func():
            all_passed = False  # Mark that something failed
        print()  # Add blank line for readability
    
    # Give final result
    if all_passed:
        print("🎉 Environment setup complete! Ready for LangChain examples.")
        print("Next step: Run 01_langchain_bedrock_basic.py")
    else:
        print("❌ Please fix the issues above before proceeding.")
        print("The other example files won't work until these problems are solved.")
        sys.exit(1)  # Exit with error code 1 (means something went wrong)

# This runs the main function only if this file is run directly
# (not if it's imported by another Python file)
if __name__ == "__main__":
    main()
