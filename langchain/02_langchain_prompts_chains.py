#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    try:
        # Initialize Bedrock client
        bedrock_client = boto3.client('bedrock-runtime')
        
        # Create ChatBedrock instance
        llm = ChatBedrock(
            client=bedrock_client,
            model_id="us.amazon.nova-pro-v1:0",
            model_kwargs={"max_tokens": 1000, "temperature": 0.7}
        )
        
        # Create a prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a snarky AWS expert assistant."),
            ("human", "{question}")
        ])
        
        # Create a chain using LangChain Expression Language (LCEL)
        chain = prompt | llm | StrOutputParser()
        
        # Use the chain
        response = chain.invoke({"question": "What are the benefits of using AWS Lambda?"})
        print(f"LangChain Chain + Nova: {response}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Check your AWS credentials and Bedrock model access.")

if __name__ == "__main__":
    main()


print('end of file')