#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock

def main():
    try:
        # Initialize Bedrock client
        bedrock_client = boto3.client(
            service_name='bedrock-runtime'
        )
        
        # Create ChatBedrock instance with Nova Pro inference profile
        chat = ChatBedrock(
            client=bedrock_client,
            model_id="us.amazon.nova-pro-v1:0",
            model_kwargs={
                "max_tokens": 1000,
                "temperature": 0.7
            }
        )
        
        # Simple chat interaction
        response = chat.invoke("Hello! Tell me a fun fact about AWS.")
        print(f"Nova Pro: {response.content}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTo use Nova models, you may need to:")
        print("1. Request model access in the AWS Bedrock console")
        print("2. Ensure your AWS credentials have proper permissions")

if __name__ == "__main__":
    main()
    
    
print('end of file')    
