#!/usr/bin/env python3
"""
Multi-step AWS Architecture Planning Tutorial

This is the SIXTH file in the learning progression (after 04_streaming_chatbot.py).
It teaches how to chain multiple AI calls together to solve complex problems that require
multiple steps, using AWS architecture planning as a practical example.

What this file demonstrates:
1. Multi-step AI workflows (chaining multiple LLM calls)
2. Sequential processing: Requirements → Services → Architecture → Costs
3. How to pass outputs from one AI call as inputs to the next
4. Building AI-powered consulting and advisory tools
5. Real-world application of LangChain for complex business logic
6. Interactive workflow with user input and step-by-step results

Prerequisites:
- Run 04_streaming_chatbot.py first to understand interactive AI applications
- Understand prompt templates, chains, and basic LangChain patterns
- Basic knowledge of AWS services (helpful but not required)

Next step: Run 06_aws_troubleshooting_chaining.py to learn about error analysis workflows
"""

# Import required libraries
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock models
from langchain_core.prompts import ChatPromptTemplate  # For creating structured prompt templates
from langchain_core.output_parsers import StrOutputParser  # For parsing AI responses into clean strings

def main():
    """
    Main function demonstrating multi-step architecture planning workflow.
    
    This creates a 3-step AI workflow:
    1. Analyze user requirements and suggest AWS services
    2. Create detailed architecture using those services  
    3. Estimate costs for the proposed architecture
    
    Each step builds on the output of the previous step, showing how to
    chain AI calls together for complex problem-solving.
    """
    
    # Step 1: Initialize AWS Bedrock connection
    # This is the same pattern we've used in previous files
    bedrock_client = boto3.client('bedrock-runtime')
    print("✅ Connected to AWS Bedrock")
    
    # Step 2: Create ChatBedrock instance
    # Using slightly lower temperature for more focused, technical responses
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={
            "max_tokens": 1000,  # Allow detailed technical responses
            "temperature": 0.7   # Balanced creativity for architecture suggestions
        }
    )
    print("✅ AI model initialized (Nova Pro)")
    
    # Step 3: Create specialized prompt templates for each step of the workflow
    # Each prompt is designed for a specific part of the architecture planning process
    
    # Chain 1: Analyze requirements and suggest specific AWS services
    # This prompt focuses the AI on identifying the right AWS services for the use case
    services_prompt = ChatPromptTemplate.from_template(
        "Analyze these requirements and suggest specific AWS services:\n\n{requirements}\n\n"
        "Respond with only the AWS service names, one per line."
    )
    print("✅ Created services analysis prompt")
    
    # Chain 2: Create detailed architecture from the suggested services
    # This prompt takes the service list and designs how they work together
    architecture_prompt = ChatPromptTemplate.from_template(
        "Create a detailed AWS architecture using these services:\n\n{services}\n\n"
        "Describe how they connect and interact. Be specific about data flow."
    )
    print("✅ Created architecture design prompt")
    
    # Chain 3: Estimate costs based on the architecture design
    # This prompt provides cost estimates for different scale scenarios
    cost_prompt = ChatPromptTemplate.from_template(
        "Based on this AWS architecture, provide cost estimates:\n\n{architecture}\n\n"
        "Give rough monthly costs for small, medium, and large scale deployments."
    )
    print("✅ Created cost estimation prompt")
    
    # Step 4: Create individual chains for each step
    # Each chain combines: prompt template → AI model → output parser
    # This is the same LCEL pattern we learned in file 02
    services_chain = services_prompt | llm | StrOutputParser()
    architecture_chain = architecture_prompt | llm | StrOutputParser()
    cost_chain = cost_prompt | llm | StrOutputParser()
    print("✅ Created 3-step processing chain")
    
    # Step 5: Get user requirements for the architecture
    print("\n=== AWS Architecture Advisor ===")
    print("I'll help you design an AWS architecture in 3 steps:")
    print("1. 🔍 Analyze your requirements and suggest services")
    print("2. 🏗️  Design detailed architecture")
    print("3. 💰 Estimate costs for different scales")
    print()
    
    # Get user input about their application requirements
    requirements = input("Describe your application requirements: ")
    
    try:
        # Step 6: Execute the 3-step workflow
        # Each step uses the output from the previous step as input
        
        print("\n🔍 Step 1: Analyzing requirements and suggesting services...")
        # First AI call: Analyze requirements → Suggest AWS services
        services = services_chain.invoke({"requirements": requirements})
        print(f"Suggested Services:\n{services}")
        
        print("\n🏗️  Step 2: Creating detailed architecture...")
        # Second AI call: Take services → Design architecture
        # Notice how we pass the output of step 1 as input to step 2
        architecture = architecture_chain.invoke({"services": services})
        print(f"Architecture Design:\n{architecture}")
        
        print("\n💰 Step 3: Estimating costs...")
        # Third AI call: Take architecture → Estimate costs
        # Notice how we pass the output of step 2 as input to step 3
        costs = cost_chain.invoke({"architecture": architecture})
        print(f"Cost Estimates:\n{costs}")
        
        print("\n✅ Architecture planning complete!")
        print("💡 This demonstrates how to chain multiple AI calls for complex workflows")
        
    except Exception as e:
        print(f"❌ Error during architecture planning: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Check your AWS credentials are configured")
        print("2. Verify Bedrock model access in AWS console")
        print("3. Ensure you have proper IAM permissions")
        print("4. Try with simpler requirements if the input was very complex")

# This runs the main function only if this file is run directly
# (not if it's imported by another Python file or test)
if __name__ == "__main__":
    main()
