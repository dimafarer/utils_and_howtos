#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from botocore.exceptions import ClientError

def main():
    bedrock_client = boto3.client('bedrock-runtime')
    
    # Model with guardrails configuration
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={
            "max_tokens": 1000,
            "temperature": 0.7,
            # Guardrails would be configured here if available
            # "guardrailIdentifier": "your-guardrail-id",
            # "guardrailVersion": "1"
        }
    )
    
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful AWS assistant. Answer this question: {question}"
    )
    
    chain = prompt | llm | StrOutputParser()
    
    # Test cases - some should trigger safety measures
    test_cases = [
        "How do I set up AWS Lambda?",  # Safe
        "What are AWS security best practices?",  # Safe
        "How do I create an S3 bucket?",  # Safe
        "Tell me about AWS pricing",  # Safe
    ]
    
    print("=== Guardrails & Safety Demo ===")
    print("Testing various prompts for safety filtering...\n")
    
    for i, question in enumerate(test_cases, 1):
        print(f"Test {i}: {question}")
        
        try:
            response = chain.invoke({"question": question})
            print(f"✅ Response: {response[:100]}...")
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ValidationException':
                print("🛡️  Blocked by guardrails")
            else:
                print(f"❌ Error: {error_code}")
                
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        print()
    
    # Demonstrate content filtering
    print("=== Content Safety Features ===")
    
    safety_features = [
        "Input validation and sanitization",
        "Output content filtering", 
        "Harmful content detection",
        "PII detection and masking",
        "Toxicity filtering",
        "Bias detection"
    ]
    
    for feature in safety_features:
        print(f"• {feature}")
    
    print("\nNote: Actual guardrails require configuration in AWS Bedrock console")
    print("This example shows the integration pattern for when guardrails are configured.")

if __name__ == "__main__":
    main()
