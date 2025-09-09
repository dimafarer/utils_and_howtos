#!/usr/bin/env python3
"""
AWS Error Analysis and Troubleshooting Workflow Tutorial

This is the SEVENTH file in the learning progression (after 05_aws_architecture_chaining.py).
It teaches how to build AI-powered troubleshooting systems that can analyze AWS errors
and provide step-by-step solutions, demonstrating advanced chaining for problem-solving.

What this file demonstrates:
1. Error analysis workflows using AI chaining
2. Sequential problem-solving: Error → Root Cause → Solutions → Steps
3. Building AI-powered support and troubleshooting tools
4. Handling real AWS error messages and providing actionable solutions
5. Advanced prompt engineering for technical problem-solving
6. Creating automated diagnostic and resolution workflows

Prerequisites:
- Run 05_aws_architecture_chaining.py first to understand multi-step chaining
- Understand how to chain AI calls and pass outputs between steps
- Basic familiarity with AWS error messages (helpful but not required)

Next step: Run 07_advanced_prompts.py to learn about structured outputs and advanced templates
"""

# Import required libraries
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock models
from langchain_core.prompts import ChatPromptTemplate  # For creating structured prompt templates
from langchain_core.output_parsers import StrOutputParser  # For parsing AI responses into clean strings

def main():
    """
    Main function demonstrating AI-powered AWS troubleshooting workflow.
    
    This creates a 3-step troubleshooting workflow:
    1. Analyze the error message and identify the root cause
    2. Generate specific solutions based on the root cause analysis
    3. Create detailed step-by-step instructions to fix the issue
    
    This pattern can be applied to any technical troubleshooting scenario
    where you need systematic problem analysis and resolution.
    """
    
    # Step 1: Initialize AWS Bedrock connection
    # Same initialization pattern as previous files
    bedrock_client = boto3.client('bedrock-runtime')
    print("✅ Connected to AWS Bedrock")
    
    # Step 2: Create ChatBedrock instance
    # Using lower temperature for more precise, technical analysis
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={
            "max_tokens": 1000,  # Allow detailed technical explanations
            "temperature": 0.3   # Lower temperature for more focused, accurate technical responses
        }
    )
    print("✅ AI model initialized (Nova Pro) with low temperature for precise analysis")
    
    # Step 3: Create specialized prompt templates for each troubleshooting step
    # Each prompt is designed for a specific part of the diagnostic process
    
    # Chain 1: Analyze error message and identify root cause
    # This prompt focuses the AI on understanding what's actually wrong
    root_cause_prompt = ChatPromptTemplate.from_template(
        "Analyze this AWS error message and identify the root cause:\n\n{error_message}\n\n"
        "Provide only the root cause analysis, be specific about what's wrong."
    )
    print("✅ Created root cause analysis prompt")
    
    # Chain 2: Generate solutions based on root cause analysis
    # This prompt takes the root cause and suggests specific fixes
    solutions_prompt = ChatPromptTemplate.from_template(
        "Based on this root cause analysis:\n\n{root_cause}\n\n"
        "Suggest 2-3 specific solutions to fix this issue. Be concise."
    )
    print("✅ Created solutions generation prompt")
    
    # Chain 3: Create detailed step-by-step instructions
    # This prompt takes the solutions and creates actionable steps
    steps_prompt = ChatPromptTemplate.from_template(
        "Based on these solutions:\n\n{solutions}\n\n"
        "Create a detailed step-by-step fix guide. Include AWS CLI commands where applicable."
    )
    print("✅ Created step-by-step instructions prompt")
    
    # Step 4: Create individual chains for each troubleshooting step
    # Each chain combines: prompt template → AI model → output parser
    # This follows the same LCEL pattern from previous files
    root_cause_chain = root_cause_prompt | llm | StrOutputParser()
    solutions_chain = solutions_prompt | llm | StrOutputParser()
    steps_chain = steps_prompt | llm | StrOutputParser()
    print("✅ Created 3-step troubleshooting chain")
    
    # Step 5: Get error message from user
    print("\n=== AWS Troubleshooting Assistant ===")
    print("I'll help you troubleshoot AWS errors in 3 steps:")
    print("1. 🔍 Analyze the error and identify root cause")
    print("2. 💡 Suggest specific solutions")
    print("3. 🛠️  Create step-by-step fix instructions")
    print()
    
    # Get the AWS error message from the user
    error_message = input("Paste your AWS error message: ")
    
    try:
        # Step 6: Execute the 3-step troubleshooting workflow
        # Each step builds on the analysis from the previous step
        
        print("\n🔍 Step 1: Analyzing error and identifying root cause...")
        # First AI call: Analyze error → Identify root cause
        root_cause = root_cause_chain.invoke({"error_message": error_message})
        print(f"Root Cause:\n{root_cause}")
        
        print("\n💡 Step 2: Suggesting solutions...")
        # Second AI call: Take root cause → Generate solutions
        # Notice how we pass the output of step 1 as input to step 2
        solutions = solutions_chain.invoke({"root_cause": root_cause})
        print(f"Solutions:\n{solutions}")
        
        print("\n🛠️  Step 3: Creating step-by-step fix guide...")
        # Third AI call: Take solutions → Create detailed steps
        # Notice how we pass the output of step 2 as input to step 3
        steps = steps_chain.invoke({"solutions": solutions})
        print(f"Step-by-Step Fix:\n{steps}")
        
        print("\n✅ Troubleshooting analysis complete!")
        print("💡 This demonstrates AI-powered systematic problem-solving")
        
    except Exception as e:
        print(f"❌ Error during troubleshooting analysis: {e}")
        print("\n🔧 Troubleshooting the troubleshooter:")
        print("1. Check your AWS credentials are configured")
        print("2. Verify Bedrock model access in AWS console")
        print("3. Ensure you have proper IAM permissions")
        print("4. Try with a simpler error message if the input was very long")

# This runs the main function only if this file is run directly
# (not if it's imported by another Python file or test)
if __name__ == "__main__":
    main()
