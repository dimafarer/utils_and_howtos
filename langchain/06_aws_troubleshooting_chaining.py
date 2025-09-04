#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    # Initialize Bedrock client
    bedrock_client = boto3.client('bedrock-runtime')
    
    # Create ChatBedrock instance
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 1000, "temperature": 0.3}
    )
    
    # Chain 1: Analyze error message and identify root cause
    root_cause_prompt = ChatPromptTemplate.from_template(
        "Analyze this AWS error message and identify the root cause:\n\n{error_message}\n\n"
        "Provide only the root cause analysis, be specific about what's wrong."
    )
    
    # Chain 2: Take root cause and suggest solutions
    solutions_prompt = ChatPromptTemplate.from_template(
        "Based on this root cause analysis:\n\n{root_cause}\n\n"
        "Suggest 2-3 specific solutions to fix this issue. Be concise."
    )
    
    # Chain 3: Take solutions and create step-by-step fix
    steps_prompt = ChatPromptTemplate.from_template(
        "Based on these solutions:\n\n{solutions}\n\n"
        "Create a detailed step-by-step fix guide. Include AWS CLI commands where applicable."
    )
    
    # Create individual chains
    root_cause_chain = root_cause_prompt | llm | StrOutputParser()
    solutions_chain = solutions_prompt | llm | StrOutputParser()
    steps_chain = steps_prompt | llm | StrOutputParser()
    
    # Get error message
    print("=== AWS Troubleshooting Assistant ===")
    error_message = input("Paste your AWS error message: ")
    
    print("\n🔍 Step 1: Analyzing error and identifying root cause...")
    root_cause = root_cause_chain.invoke({"error_message": error_message})
    print(f"Root Cause:\n{root_cause}")
    
    print("\n💡 Step 2: Suggesting solutions...")
    solutions = solutions_chain.invoke({"root_cause": root_cause})
    print(f"Solutions:\n{solutions}")
    
    print("\n🛠️  Step 3: Creating step-by-step fix guide...")
    steps = steps_chain.invoke({"solutions": solutions})
    print(f"Step-by-Step Fix:\n{steps}")

if __name__ == "__main__":
    main()
