#!/usr/bin/env python3
"""
Basic LangChain + AWS Bedrock Example

This is the SECOND file in the learning progression (after 00_environment_setup_check.py).
It demonstrates the simplest possible AI chatbot using AWS Bedrock and LangChain.

What this file demonstrates:
1. How to connect to AWS Bedrock (AWS's AI service)
2. How to create a ChatBedrock instance (LangChain's wrapper for Bedrock)
3. How to send a simple message and get an AI response
4. Basic error handling for common issues

Prerequisites:
- Run 00_environment_setup_check.py first to verify your setup
- AWS credentials configured with Bedrock access
- Required Python packages installed

Next step: Run 02_langchain_prompts_chains.py to learn about prompt templates
"""

# Import required libraries
import boto3  # AWS SDK for Python - lets us connect to AWS services
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock

def main():
    """
    Main function that demonstrates basic Bedrock usage.
    
    This function shows the minimal steps needed to:
    1. Connect to AWS Bedrock
    2. Create an AI chat model
    3. Send a message and get a response
    """
    try:
        # Step 1: Initialize Bedrock client
        # This creates a connection to AWS Bedrock's runtime service
        # 'bedrock-runtime' is for getting AI responses (not managing models)
        bedrock_client = boto3.client(
            service_name='bedrock-runtime'  # The service that runs AI models
        )
        print("✅ Connected to AWS Bedrock")
        
        # Step 2: Create ChatBedrock instance
        # This is LangChain's wrapper that makes Bedrock easier to use
        chat = ChatBedrock(
            client=bedrock_client,  # Use our Bedrock connection
            model_id="us.amazon.nova-pro-v1:0",  # AWS's Nova Pro model (good balance of speed/quality)
            model_kwargs={
                # Model parameters that control AI behavior
                "max_tokens": 1000,    # Maximum response length (about 750 words)
                "temperature": 0.7     # Creativity level: 0=focused, 1=creative, 0.7=balanced
            }
        )
        print("✅ AI model initialized (Nova Pro)")
        
        # Step 3: Simple chat interaction
        # The invoke() method sends a message and waits for the complete response
        print("\n🤖 Asking AI a question...")
        response = chat.invoke("Hello! Tell me a fun fact about AWS.")
        
        # Step 4: Display the response
        # The response object has a .content attribute with the AI's text
        print(f"\n🎯 AI Response:")
        print(f"Nova Pro: {response.content}")
        
        print("\n✅ Success! Your basic AI chatbot is working.")
        print("Next step: Try 02_langchain_prompts_chains.py to learn about prompt templates")
        
    except Exception as e:
        # Handle errors with helpful guidance for beginners
        print(f"❌ Error: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Run 00_environment_setup_check.py to verify your setup")
        print("2. Check that you have AWS credentials configured ('aws configure')")
        print("3. Ensure your AWS account has access to Bedrock models")
        print("4. For Nova models, you may need to request access in the AWS Bedrock console")
        print("5. Verify your AWS user has bedrock:InvokeModel permissions")

# This runs the main function only if this file is run directly
# (not if it's imported by another Python file)
if __name__ == "__main__":
    main()    
