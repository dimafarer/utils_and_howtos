#!/usr/bin/env python3

import sys
import subprocess
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    return True

def check_dependencies():
    """Check if required packages are installed."""
    required = ['langchain_aws', 'boto3', 'langchain_community']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing.append(package)
            print(f"❌ {package}")
    
    if missing:
        print(f"\nInstall missing packages: pip install {' '.join(missing)}")
        return False
    return True

def check_aws_credentials():
    """Check AWS credentials and Bedrock access."""
    try:
        session = boto3.Session()
        credentials = session.get_credentials()
        if not credentials:
            print("❌ No AWS credentials found")
            return False
        print("✅ AWS credentials configured")
        
        # Test Bedrock access
        bedrock = boto3.client('bedrock-runtime')
        # Try to list foundation models to test access
        bedrock.list_foundation_models()
        print("✅ Bedrock access confirmed")
        return True
        
    except NoCredentialsError:
        print("❌ AWS credentials not configured")
        return False
    except ClientError as e:
        if e.response['Error']['Code'] == 'UnauthorizedOperation':
            print("❌ No Bedrock permissions")
        else:
            print(f"❌ AWS error: {e}")
        return False

def main():
    print("=== LangChain + Bedrock Environment Check ===\n")
    
    checks = [
        check_python_version(),
        check_dependencies(),
        check_aws_credentials()
    ]
    
    if all(checks):
        print("\n🎉 Environment ready for LangChain + Bedrock!")
    else:
        print("\n⚠️  Please fix the issues above before proceeding.")

if __name__ == "__main__":
    main()
