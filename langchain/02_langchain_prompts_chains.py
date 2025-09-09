#!/usr/bin/env python3
"""
LangChain Prompt Templates and Chains Tutorial

This is the THIRD file in the learning progression (after 01_langchain_bedrock_basic.py).
It teaches the fundamental concepts that make LangChain powerful: prompt templates and chains.

What this file demonstrates:
1. Why prompt templates are better than hardcoded strings
2. How to create and use ChatPromptTemplate
3. Variable substitution in prompts
4. Output parsers for clean responses
5. LCEL (LangChain Expression Language) for chaining
6. Building reusable, composable AI workflows

Prerequisites:
- Run 01_langchain_bedrock_basic.py first to understand basic Bedrock usage
- Understand basic Python string formatting

Next step: Run 03_conversational_memory_chatbot.py to learn about stateful conversations
"""

# Import required libraries
import boto3  # AWS SDK for Python
from langchain_aws import ChatBedrock  # LangChain's Bedrock wrapper
from langchain_core.prompts import ChatPromptTemplate  # For creating prompt templates
from langchain_core.output_parsers import StrOutputParser  # For parsing AI responses

def demonstrate_hardcoded_vs_template():
    """
    Demonstrate why prompt templates are better than hardcoded strings.
    
    This shows the difference between inflexible hardcoded prompts
    and flexible, reusable prompt templates.
    """
    print("=== 1. Hardcoded vs Template Comparison ===")
    
    # ❌ BAD: Hardcoded prompt (inflexible)
    hardcoded_prompt = "You are an AWS expert. Explain Lambda functions."
    print(f"❌ Hardcoded: {hardcoded_prompt}")
    print("   Problem: Can't change the topic without rewriting code")
    
    # ✅ GOOD: Template with variables (flexible)
    template_prompt = "You are an AWS expert. Explain {topic}."
    print(f"✅ Template: {template_prompt}")
    print("   Benefit: Can use for any AWS topic by changing the variable")
    print()

def demonstrate_basic_template():
    """
    Demonstrate basic prompt template creation and usage.
    
    This shows how to create a simple template with one variable
    and how to format it with different values.
    """
    print("=== 2. Basic Prompt Template ===")
    
    # Create a simple prompt template
    # The {topic} is a placeholder that will be replaced with actual values
    prompt = ChatPromptTemplate.from_template(
        "You are an AWS expert. Explain {topic} in simple terms for beginners."
    )
    
    print("✅ Created template with variable: {topic}")
    
    # Show how the template can be used with different topics
    topics = ["Lambda functions", "S3 buckets", "DynamoDB tables"]
    
    for topic in topics:
        # Format the template with a specific topic
        formatted_messages = prompt.format_messages(topic=topic)
        print(f"   Topic '{topic}' → {formatted_messages[0].content}")
    
    print("💡 Same template, different outputs - that's the power of templates!")
    print()

def demonstrate_multi_variable_template():
    """
    Demonstrate templates with multiple variables.
    
    This shows how templates can have multiple placeholders
    for more complex and flexible prompts.
    """
    print("=== 3. Multi-Variable Template ===")
    
    # Create a template with multiple variables
    prompt = ChatPromptTemplate.from_template(
        "You are a {role} expert. Explain {topic} to a {audience} "
        "in {style} style. Keep it under {word_count} words."
    )
    
    print("✅ Created template with 4 variables: role, topic, audience, style, word_count")
    
    # Show different combinations
    scenarios = [
        {
            "role": "AWS", 
            "topic": "serverless computing", 
            "audience": "beginner developer",
            "style": "friendly",
            "word_count": "50"
        },
        {
            "role": "security", 
            "topic": "IAM policies", 
            "audience": "system administrator",
            "style": "technical",
            "word_count": "100"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        formatted = prompt.format_messages(**scenario)
        print(f"   Scenario {i}: {formatted[0].content}")
    
    print("💡 Multiple variables allow for very flexible and reusable prompts!")
    print()

def demonstrate_chat_template_structure():
    """
    Demonstrate ChatPromptTemplate with system and human messages.
    
    This shows the proper structure for chat-based AI interactions
    with separate system instructions and user messages.
    """
    print("=== 4. Chat Template Structure ===")
    
    # Create a chat template with system and human messages
    # System message: Sets the AI's role and behavior
    # Human message: The actual user input/question
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AWS assistant. Always provide practical examples."),
        ("human", "Explain {aws_service} and give me a real-world use case.")
    ])
    
    print("✅ Created chat template with:")
    print("   - System message: Sets AI behavior")
    print("   - Human message: User input with variable")
    
    # Show the structure
    formatted = prompt.format_messages(aws_service="AWS Lambda")
    print(f"\n   System: {formatted[0].content}")
    print(f"   Human: {formatted[1].content}")
    print()

def demonstrate_output_parser():
    """
    Demonstrate output parsers for clean response handling.
    
    This shows how output parsers clean up AI responses
    and make them easier to work with in your code.
    """
    print("=== 5. Output Parser ===")
    
    print("🔧 Output parsers clean up AI responses:")
    print("   - Remove extra whitespace")
    print("   - Convert to proper data types")
    print("   - Extract just the content you need")
    
    # Create an output parser
    output_parser = StrOutputParser()
    print("✅ Created StrOutputParser (converts AI response to clean string)")
    
    # Simulate what the parser does
    print("\n   Raw AI response: AIMessage(content='  AWS Lambda is great!  ')")
    print("   After parser: 'AWS Lambda is great!'")
    print("💡 Parser removes extra whitespace and extracts just the text content")
    print()

def demonstrate_lcel_chain():
    """
    Demonstrate LCEL (LangChain Expression Language) for chaining.
    
    This shows how to combine prompt templates, AI models, and output parsers
    into a single, reusable chain using the | (pipe) operator.
    """
    print("=== 6. LCEL Chain Composition ===")
    
    print("🔗 LCEL lets you chain components together:")
    print("   prompt | llm | output_parser")
    print("   ↓")
    print("   Input → Template → AI Model → Clean Output")
    
    # Initialize Bedrock client and model
    bedrock_client = boto3.client('bedrock-runtime')
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 200, "temperature": 0.7}
    )
    
    # Create the components
    prompt = ChatPromptTemplate.from_template(
        "You are an AWS expert. Explain {topic} in exactly 2 sentences."
    )
    output_parser = StrOutputParser()
    
    # Chain them together using LCEL (the | operator)
    chain = prompt | llm | output_parser
    
    print("\n✅ Created chain: prompt | llm | output_parser")
    print("💡 The | operator connects components in sequence")
    print()
    
    return chain

def main():
    """
    Main function that demonstrates all prompt template and chain concepts.
    
    This runs through all the examples to show the progression from
    basic templates to complete chains.
    """
    print("=== LangChain Prompt Templates and Chains Tutorial ===")
    print("Learning how to create flexible, reusable AI workflows!\n")
    
    # Step 1: Show why templates are better than hardcoded strings
    demonstrate_hardcoded_vs_template()
    
    # Step 2: Basic template with one variable
    demonstrate_basic_template()
    
    # Step 3: Template with multiple variables
    demonstrate_multi_variable_template()
    
    # Step 4: Proper chat template structure
    demonstrate_chat_template_structure()
    
    # Step 5: Output parsers for clean responses
    demonstrate_output_parser()
    
    # Step 6: LCEL chains for complete workflows
    chain = demonstrate_lcel_chain()
    
    # Step 7: Use the chain with real AI
    print("=== 7. Using the Complete Chain ===")
    try:
        print("🤖 Testing our chain with real AI...")
        
        # Test the chain with different topics
        topics = ["S3 buckets", "Lambda functions", "DynamoDB"]
        
        for topic in topics:
            print(f"\n📝 Topic: {topic}")
            response = chain.invoke({"topic": topic})
            print(f"🎯 AI Response: {response}")
        
        print("\n✅ Success! You've built a complete, reusable AI chain.")
        print("💡 This same chain can be used for any AWS topic!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("🔧 Troubleshooting:")
        print("1. Check your AWS credentials are configured")
        print("2. Verify Bedrock model access in AWS console")
        print("3. Ensure you have proper IAM permissions")
    
    print("\n🎉 Tutorial Complete!")
    print("Next step: Run 03_conversational_memory_chatbot.py to learn about stateful conversations")

# This runs the main function only if this file is run directly
if __name__ == "__main__":
    main()