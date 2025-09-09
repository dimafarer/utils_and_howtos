#!/usr/bin/env python3
"""
Advanced Prompt Engineering and Structured Outputs Tutorial

This is the EIGHTH file in the learning progression (after 06_aws_troubleshooting_chaining.py).
It teaches advanced prompt engineering techniques including structured outputs, Pydantic models,
and sophisticated prompt composition for production-ready AI applications.

What this file demonstrates:
1. Structured outputs using Pydantic models for type-safe AI responses
2. Advanced prompt composition and template techniques
3. Few-shot learning with examples in prompts
4. Output parsing for complex data structures
5. Production-ready prompt patterns for reliable AI applications
6. Type safety and validation in AI workflows

Prerequisites:
- Run 06_aws_troubleshooting_chaining.py first to understand advanced chaining
- Understand basic prompt templates and chains from earlier files
- Basic knowledge of Python data classes and type hints (helpful)

Next step: Run 08_callbacks_monitoring.py to learn about production monitoring
"""

# Import required libraries
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock models
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate  # For creating various types of prompt templates
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser  # For parsing different types of AI responses
from pydantic import BaseModel, Field  # For creating structured data models with validation
from typing import List  # For type hints in data structures

# Step 1: Define Pydantic models for structured outputs
# These models ensure the AI returns data in a specific, predictable format

class AWSService(BaseModel):
    """
    Represents a single AWS service recommendation.
    
    Pydantic models provide:
    - Type safety: Ensures fields are the correct data type
    - Validation: Checks that required fields are present
    - Documentation: Field descriptions help the AI understand what to return
    """
    name: str = Field(description="AWS service name (e.g., 'Lambda', 'S3')")
    use_case: str = Field(description="Primary use case for this service")
    cost_tier: str = Field(description="Cost tier: 'low', 'medium', or 'high'")

class ArchitectureRecommendation(BaseModel):
    """
    Represents a complete AWS architecture recommendation.
    
    This shows how to create complex, nested data structures
    that the AI can reliably populate with structured information.
    """
    services: List[AWSService] = Field(description="List of recommended AWS services")
    estimated_monthly_cost: str = Field(description="Estimated monthly cost range (e.g., '$100-500')")

def demonstrate_basic_prompt_composition():
    """
    Demonstrate advanced prompt composition techniques.
    
    This shows how to build complex prompts from smaller, reusable components
    for better maintainability and flexibility.
    """
    print("=== 1. Advanced Prompt Composition ===")
    
    # Create reusable prompt components
    # These can be mixed and matched for different use cases
    
    # System role component - defines the AI's expertise and behavior
    system_role = "You are an expert AWS solutions architect with 10+ years of experience."
    
    # Context component - provides background information
    context_template = """
    Consider these factors when making recommendations:
    - Cost optimization is a high priority
    - The solution should be scalable and maintainable
    - Security best practices must be followed
    - Prefer serverless solutions when appropriate
    """
    
    # Task component - specific instructions for the current task
    task_template = """
    Based on the requirements below, recommend AWS services and architecture:
    
    Requirements: {requirements}
    
    Provide your recommendations in a structured format.
    """
    
    # Combine components into a complete prompt
    # This modular approach makes prompts easier to maintain and modify
    complete_prompt = ChatPromptTemplate.from_template(
        system_role + "\n\n" + context_template + "\n\n" + task_template
    )
    
    print("✅ Created modular prompt with reusable components:")
    print("   - System role (defines AI expertise)")
    print("   - Context (provides guidelines)")
    print("   - Task (specific instructions)")
    print("💡 This approach makes prompts maintainable and consistent")
    print()
    
    return complete_prompt

def demonstrate_structured_output_parsing():
    """
    Demonstrate structured output parsing with Pydantic models.
    
    This shows how to get reliable, type-safe responses from AI
    instead of just plain text that needs manual parsing.
    """
    print("=== 2. Structured Output Parsing ===")
    
    # Create a Pydantic output parser
    # This tells the AI exactly what format to return data in
    parser = PydanticOutputParser(pydantic_object=ArchitectureRecommendation)
    
    print("✅ Created Pydantic parser for structured outputs")
    print("💡 Benefits of structured outputs:")
    print("   - Type safety: Fields have guaranteed data types")
    print("   - Validation: Required fields must be present")
    print("   - Consistency: Same format every time")
    print("   - Easy processing: Direct access to structured data")
    print()
    
    # Get format instructions for the AI
    # This tells the AI exactly how to format its response
    format_instructions = parser.get_format_instructions()
    print("📋 Format instructions for AI:")
    print(format_instructions[:200] + "..." if len(format_instructions) > 200 else format_instructions)
    print()
    
    return parser

def demonstrate_few_shot_learning():
    """
    Demonstrate few-shot learning with examples in prompts.
    
    Few-shot learning provides examples to the AI to improve
    the quality and consistency of responses.
    """
    print("=== 3. Few-Shot Learning with Examples ===")
    
    # Create a prompt template with examples
    # Examples help the AI understand the expected response format and quality
    few_shot_prompt = PromptTemplate(
        input_variables=["requirements"],
        template="""
You are an AWS expert. Analyze requirements and recommend services.

Example 1:
Requirements: "I need to build a simple website with a contact form"
Recommendation: Use S3 for static hosting, Lambda for form processing, SES for email

Example 2:
Requirements: "I need a scalable API for a mobile app with user authentication"
Recommendation: Use API Gateway for the API, Lambda for business logic, Cognito for auth, DynamoDB for data

Now analyze these requirements:
Requirements: {requirements}
Recommendation: """
    )
    
    print("✅ Created few-shot prompt with examples")
    print("💡 Few-shot learning benefits:")
    print("   - Better response quality through examples")
    print("   - Consistent output format")
    print("   - Reduced need for detailed instructions")
    print("   - AI learns patterns from examples")
    print()
    
    return few_shot_prompt

def main():
    """
    Main function demonstrating advanced prompt engineering techniques.
    
    This combines all the advanced concepts to show how to build
    production-ready AI applications with reliable, structured outputs.
    """
    print("=== Advanced Prompt Engineering Tutorial ===")
    print("Learning production-ready prompt patterns and structured outputs!\n")
    
    # Initialize Bedrock connection
    bedrock_client = boto3.client('bedrock-runtime')
    print("✅ Connected to AWS Bedrock")
    
    # Create ChatBedrock instance with settings optimized for structured output
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={
            "max_tokens": 1000,
            "temperature": 0.3  # Lower temperature for more consistent structured outputs
        }
    )
    print("✅ AI model initialized with low temperature for consistent outputs")
    
    # Demonstrate advanced techniques
    print("\n" + "="*60)
    
    # 1. Advanced prompt composition
    composed_prompt = demonstrate_basic_prompt_composition()
    
    # 2. Structured output parsing
    structured_parser = demonstrate_structured_output_parsing()
    
    # 3. Few-shot learning
    few_shot_prompt = demonstrate_few_shot_learning()
    
    # 4. Combine everything into a production-ready chain
    print("=== 4. Production-Ready Structured Chain ===")
    
    # Create a prompt that includes format instructions for structured output
    structured_prompt = ChatPromptTemplate.from_template(
        """You are an expert AWS solutions architect.
        
Analyze the requirements and provide recommendations in the exact format specified.

Requirements: {requirements}

{format_instructions}"""
    )
    
    # Create the complete chain with structured output
    structured_chain = structured_prompt | llm | structured_parser
    print("✅ Created production chain: prompt → AI → structured parser")
    
    # 5. Test the structured output chain
    print("\n=== 5. Testing Structured Output ===")
    
    try:
        # Test with sample requirements
        test_requirements = "I need to build a real-time chat application for 10,000 users with message history"
        
        print(f"🧪 Test requirements: {test_requirements}")
        print("\n🤖 Getting structured AI response...")
        
        # Get structured response
        result = structured_chain.invoke({
            "requirements": test_requirements,
            "format_instructions": structured_parser.get_format_instructions()
        })
        
        print("✅ Received structured response!")
        print(f"📊 Response type: {type(result)}")
        print(f"📋 Services recommended: {len(result.services)}")
        
        # Display the structured data
        print("\n📈 Structured Results:")
        for i, service in enumerate(result.services, 1):
            print(f"   {i}. {service.name}")
            print(f"      Use case: {service.use_case}")
            print(f"      Cost tier: {service.cost_tier}")
        
        print(f"\n💰 Estimated cost: {result.estimated_monthly_cost}")
        
        print("\n✅ Success! The AI returned perfectly structured, type-safe data")
        print("💡 This data can be directly used in applications without parsing")
        
    except Exception as e:
        print(f"❌ Error during structured output test: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Check your AWS credentials are configured")
        print("2. Verify Bedrock model access in AWS console")
        print("3. Ensure the AI response matches the expected Pydantic model format")
    
    print("\n🎉 Tutorial Complete!")
    print("You now understand advanced prompt engineering for production AI!")
    print("\n📚 Key Concepts Learned:")
    print("   ✅ Modular prompt composition")
    print("   ✅ Structured outputs with Pydantic models")
    print("   ✅ Few-shot learning with examples")
    print("   ✅ Type-safe AI responses")
    print("   ✅ Production-ready prompt patterns")
    
    print("\nNext step: Run 08_callbacks_monitoring.py to learn about production monitoring!")

# This runs the main function only if this file is run directly
if __name__ == "__main__":
    main()
