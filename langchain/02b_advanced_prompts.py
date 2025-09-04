#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class AWSService(BaseModel):
    name: str = Field(description="AWS service name")
    use_case: str = Field(description="Primary use case")
    cost_tier: str = Field(description="Cost tier: low, medium, high")

class ArchitectureRecommendation(BaseModel):
    services: List[AWSService] = Field(description="List of recommended AWS services")
    estimated_monthly_cost: str = Field(description="Estimated monthly cost range")

def main():
    bedrock_client = boto3.client('bedrock-runtime')
    
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 1000, "temperature": 0.3}
    )
    
    # 1. Basic Prompt Composition
    print("=== 1. Prompt Composition ===")
    
    base_prompt = PromptTemplate.from_template(
        "You are an AWS solutions architect. {context}"
    )
    
    specific_prompt = PromptTemplate.from_template(
        "Analyze this requirement: {requirement}\n"
        "Provide recommendations for: {focus_area}"
    )
    
    # Compose prompts
    composed = ChatPromptTemplate.from_messages([
        ("system", base_prompt.format(context="Focus on cost-effective solutions.")),
        ("human", specific_prompt.format(
            requirement="Real-time chat app for 1000 users",
            focus_area="compute and storage"
        ))
    ])
    
    chain = composed | llm | StrOutputParser()
    response = chain.invoke({})
    print(f"Composed Response:\n{response}\n")
    
    # 2. Structured Output with Pydantic
    print("=== 2. Structured Output Parsing ===")
    
    parser = PydanticOutputParser(pydantic_object=ArchitectureRecommendation)
    
    structured_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AWS architect. Respond in the exact format requested."),
        ("human", "{requirement}\n\n{format_instructions}")
    ])
    
    structured_chain = structured_prompt | llm | parser
    
    try:
        structured_response = structured_chain.invoke({
            "requirement": "E-commerce platform with 10,000 daily users",
            "format_instructions": parser.get_format_instructions()
        })
        
        print("Structured Response:")
        print(f"Services: {len(structured_response.services)}")
        for service in structured_response.services:
            print(f"  - {service.name}: {service.use_case} ({service.cost_tier} cost)")
        print(f"Estimated Cost: {structured_response.estimated_monthly_cost}")
        
    except Exception as e:
        print(f"Parsing error: {e}")
    
    # 3. Few-Shot Prompting
    print("\n=== 3. Few-Shot Learning ===")
    
    few_shot_prompt = ChatPromptTemplate.from_messages([
        ("system", "Classify AWS services by category. Examples:"),
        ("human", "Lambda"),
        ("ai", "Compute - Serverless"),
        ("human", "RDS"),
        ("ai", "Database - Managed"),
        ("human", "S3"),
        ("ai", "Storage - Object"),
        ("human", "{service}")
    ])
    
    few_shot_chain = few_shot_prompt | llm | StrOutputParser()
    
    test_services = ["API Gateway", "DynamoDB", "CloudFront"]
    for service in test_services:
        classification = few_shot_chain.invoke({"service": service})
        print(f"{service}: {classification.strip()}")

if __name__ == "__main__":
    main()
