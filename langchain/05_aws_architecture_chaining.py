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
        model_kwargs={"max_tokens": 1000, "temperature": 0.7}
    )
    
    # Chain 1: Analyze requirements and suggest services
    services_prompt = ChatPromptTemplate.from_template(
        "Analyze these requirements and suggest specific AWS services:\n\n{requirements}\n\n"
        "Respond with only the AWS service names, one per line."
    )
    
    # Chain 2: Create detailed architecture from services
    architecture_prompt = ChatPromptTemplate.from_template(
        "Create a detailed AWS architecture using these services:\n\n{services}\n\n"
        "Describe how they connect and interact. Be specific about data flow."
    )
    
    # Chain 3: Estimate costs from architecture
    cost_prompt = ChatPromptTemplate.from_template(
        "Based on this AWS architecture, provide cost estimates:\n\n{architecture}\n\n"
        "Give rough monthly costs for small, medium, and large scale deployments."
    )
    
    # Create individual chains
    services_chain = services_prompt | llm | StrOutputParser()
    architecture_chain = architecture_prompt | llm | StrOutputParser()
    cost_chain = cost_prompt | llm | StrOutputParser()
    
    # Get user requirements
    print("=== AWS Architecture Advisor ===")
    requirements = input("Describe your application requirements: ")
    
    print("\n🔍 Step 1: Analyzing requirements and suggesting services...")
    services = services_chain.invoke({"requirements": requirements})
    print(f"Suggested Services:\n{services}")
    
    print("\n🏗️  Step 2: Creating detailed architecture...")
    architecture = architecture_chain.invoke({"services": services})
    print(f"Architecture Design:\n{architecture}")
    
    print("\n💰 Step 3: Estimating costs...")
    costs = cost_chain.invoke({"architecture": architecture})
    print(f"Cost Estimates:\n{costs}")

if __name__ == "__main__":
    main()
