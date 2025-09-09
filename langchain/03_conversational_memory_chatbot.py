#!/usr/bin/env python3
"""
Conversational Memory Chatbot Tutorial

This is the FOURTH file in the learning progression (after 02_langchain_prompts_chains.py).
It teaches how to add memory to AI conversations, making them stateful and context-aware.

What this file demonstrates:
1. The difference between stateless and stateful conversations
2. How to add memory to LangChain chains
3. Using MessagesPlaceholder for conversation history
4. Session management for multiple conversations
5. Building a complete conversational AI that remembers context

Prerequisites:
- Run 02_langchain_prompts_chains.py first to understand templates and chains
- Understand basic prompt templates and LCEL chains

Next step: Run 04_streaming_chatbot.py to learn about real-time streaming responses
"""

# Import required libraries
import boto3  # AWS SDK for Python
from langchain_aws import ChatBedrock  # LangChain's Bedrock wrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # For templates with history
from langchain_core.output_parsers import StrOutputParser  # For parsing responses
from langchain_community.chat_message_histories import ChatMessageHistory  # For storing conversation history
from langchain_core.runnables.history import RunnableWithMessageHistory  # For adding memory to chains

def demonstrate_stateless_problem():
    """
    Demonstrate the problem with stateless conversations.
    
    This shows why AI conversations without memory are frustrating
    and don't feel natural to users.
    """
    print("=== 1. The Stateless Problem ===")
    print("❌ Without memory, each AI response is independent:")
    print("   User: 'What is AWS Lambda?'")
    print("   AI: 'AWS Lambda is a serverless compute service...'")
    print("   User: 'How much does it cost?'")
    print("   AI: 'What service are you asking about?' (AI forgot about Lambda!)")
    print()
    print("✅ With memory, AI remembers the conversation:")
    print("   User: 'What is AWS Lambda?'")
    print("   AI: 'AWS Lambda is a serverless compute service...'")
    print("   User: 'How much does it cost?'")
    print("   AI: 'Lambda pricing is based on requests and duration...' (AI remembers!)")
    print()

def demonstrate_messages_placeholder():
    """
    Demonstrate MessagesPlaceholder for conversation history.
    
    This shows how to create prompt templates that can include
    previous conversation messages for context.
    """
    print("=== 2. MessagesPlaceholder for History ===")
    
    # Create a prompt template with a placeholder for conversation history
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AWS assistant. Keep responses concise but informative."),
        MessagesPlaceholder(variable_name="history"),  # This holds previous messages
        ("human", "{input}")  # Current user input
    ])
    
    print("✅ Created prompt template with MessagesPlaceholder:")
    print("   - System message: Sets AI behavior")
    print("   - MessagesPlaceholder: Holds conversation history")
    print("   - Human message: Current user input")
    print()
    print("💡 The 'history' placeholder will be filled with previous messages")
    print("   This gives the AI context about what was discussed before")
    print()

def demonstrate_chat_message_history():
    """
    Demonstrate ChatMessageHistory for storing conversations.
    
    This shows how to create and manage conversation history
    that can be passed to the AI for context.
    """
    print("=== 3. ChatMessageHistory Storage ===")
    
    # Create a chat message history object
    history = ChatMessageHistory()
    
    print("✅ Created ChatMessageHistory object")
    print("   This stores the conversation messages in memory")
    
    # Add some example messages
    history.add_user_message("What is AWS Lambda?")
    history.add_ai_message("AWS Lambda is a serverless compute service that runs code without managing servers.")
    history.add_user_message("How do I deploy a function?")
    
    print("\n📝 Added messages to history:")
    for i, message in enumerate(history.messages, 1):
        role = "User" if message.type == "human" else "AI"
        print(f"   {i}. {role}: {message.content}")
    
    print(f"\n💡 History now contains {len(history.messages)} messages")
    print("   The AI can use this context for better responses")
    print()

def demonstrate_session_management():
    """
    Demonstrate session management for multiple conversations.
    
    This shows how to manage separate conversations with different users
    or different topics, each with their own memory.
    """
    print("=== 4. Session Management ===")
    
    # Create a store for multiple conversation sessions
    store = {}
    
    def get_session_history(session_id: str) -> ChatMessageHistory:
        """
        Get or create a conversation history for a specific session.
        
        Args:
            session_id: Unique identifier for the conversation
            
        Returns:
            ChatMessageHistory object for this session
        """
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
    
    print("✅ Created session management system:")
    print("   - Each user/conversation gets a unique session_id")
    print("   - Each session has its own conversation history")
    print("   - Multiple conversations can run simultaneously")
    
    # Demonstrate multiple sessions
    sessions = ["user_alice", "user_bob", "aws_support"]
    
    for session in sessions:
        history = get_session_history(session)
        print(f"   📁 Session '{session}': {len(history.messages)} messages")
    
    print("\n💡 This allows multiple users to have separate conversations")
    print("   Each conversation maintains its own context and memory")
    print()

def create_conversational_chain():
    """
    Create a complete conversational chain with memory.
    
    This combines all the concepts to build a working chatbot
    that remembers conversation context.
    
    Returns:
        RunnableWithMessageHistory: A chain with memory capabilities
    """
    print("=== 5. Building the Conversational Chain ===")
    
    # Step 1: Initialize Bedrock client and model
    bedrock_client = boto3.client('bedrock-runtime')
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 500, "temperature": 0.7}
    )
    print("✅ Step 1: Created Bedrock LLM")
    
    # Step 2: Create prompt template with history placeholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AWS assistant. Keep responses concise but informative."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    print("✅ Step 2: Created prompt template with history")
    
    # Step 3: Create the basic chain
    chain = prompt | llm | StrOutputParser()
    print("✅ Step 3: Created basic chain (prompt | llm | parser)")
    
    # Step 4: Add memory to the chain
    store = {}
    
    def get_session_history(session_id: str) -> ChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
    
    # Wrap the chain with memory capabilities
    conversational_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )
    print("✅ Step 4: Added memory with RunnableWithMessageHistory")
    
    print("\n🎉 Complete conversational chain created!")
    print("   Input → Template (with history) → LLM → Clean Output")
    print("   Memory automatically manages conversation context")
    print()
    
    return conversational_chain

def demonstrate_conversation_flow(chain):
    """
    Demonstrate a complete conversation flow with memory.
    
    This shows how the AI remembers context across multiple
    exchanges in a conversation.
    
    Args:
        chain: The conversational chain with memory
    """
    print("=== 6. Conversation Flow Demo ===")
    
    session_id = "demo_session"
    
    # Simulate a conversation about AWS services
    conversation = [
        "What is AWS Lambda?",
        "How much does it cost?",
        "What about S3?", 
        "Which is better for a web application?"
    ]
    
    print(f"🗣️  Starting conversation (Session: {session_id})")
    
    try:
        for i, user_input in enumerate(conversation, 1):
            print(f"\n💬 Turn {i}")
            print(f"User: {user_input}")
            
            # Get AI response with memory
            response = chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )
            
            print(f"AI: {response}")
        
        print("\n✅ Conversation completed successfully!")
        print("💡 Notice how the AI remembers context from previous messages")
        
    except Exception as e:
        print(f"❌ Error during conversation: {e}")
        print("🔧 Check your AWS credentials and Bedrock access")

def main():
    """
    Main function that demonstrates conversational memory concepts.
    
    This runs through all the examples to show how to build
    AI conversations that remember context.
    """
    print("=== Conversational Memory Chatbot Tutorial ===")
    print("Learning how to build AI that remembers conversations!\n")
    
    # Step 1: Show the problem with stateless conversations
    demonstrate_stateless_problem()
    
    # Step 2: Explain MessagesPlaceholder for history
    demonstrate_messages_placeholder()
    
    # Step 3: Show how to store conversation history
    demonstrate_chat_message_history()
    
    # Step 4: Demonstrate session management
    demonstrate_session_management()
    
    # Step 5: Build the complete conversational chain
    conversational_chain = create_conversational_chain()
    
    # Step 6: Demonstrate the conversation flow
    demonstrate_conversation_flow(conversational_chain)
    
    print("\n🎉 Tutorial Complete!")
    print("You now understand how to build AI conversations with memory!")
    print("\n📚 Key Concepts Learned:")
    print("   ✅ Stateless vs Stateful conversations")
    print("   ✅ MessagesPlaceholder for conversation history")
    print("   ✅ ChatMessageHistory for storing messages")
    print("   ✅ Session management for multiple conversations")
    print("   ✅ RunnableWithMessageHistory for memory-enabled chains")
    
    print("\nNext step: Run 04_streaming_chatbot.py to learn about real-time streaming!")

# This runs the main function only if this file is run directly
if __name__ == "__main__":
    main()
