#!/usr/bin/env python3
"""
Real-time Streaming Chatbot Tutorial

This is the FIFTH file in the learning progression (after 03_conversational_memory_chatbot.py).
It teaches how to build AI chatbots that stream responses in real-time, creating a more 
interactive and responsive user experience.

What this file demonstrates:
1. The difference between batch and streaming responses
2. How to implement real-time streaming with LangChain
3. Building interactive chat interfaces with memory
4. Debug mode for development and troubleshooting
5. Error handling in streaming applications
6. Production-ready streaming patterns

Prerequisites:
- Run 03_conversational_memory_chatbot.py first to understand memory concepts
- Understand prompt templates, chains, and conversation history
- Basic knowledge of real-time applications

Next step: Run 05_aws_architecture_chaining.py to learn about multi-step AI workflows

Usage:
    python 04_streaming_chatbot.py          # Normal streaming mode
    python 04_streaming_chatbot.py --debug  # Debug mode (shows streaming details)
"""

# Import required libraries
import sys  # For command-line argument processing and debug mode
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock models
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # For creating prompt templates with conversation history
from langchain_community.chat_message_histories import ChatMessageHistory  # For storing conversation messages in memory
from langchain_core.runnables.history import RunnableWithMessageHistory  # For adding memory capabilities to chains
from langchain_core.messages import HumanMessage, AIMessage  # For manual memory management
import sys

def main():
    # Check if user wants to see debug information (raw streaming chunks)
    debug_mode = "--debug" in sys.argv
    
    # Try to connect to AWS Bedrock - this might fail if credentials aren't set up
    try:
        bedrock_client = boto3.client('bedrock-runtime')
        print("✓ Successfully connected to AWS Bedrock")
    except Exception as e:
        print(f"❌ Error connecting to AWS Bedrock: {e}")
        print("Make sure your AWS credentials are configured with 'aws configure'")
        return  # Exit the program if we can't connect
    
    # Create the language model with streaming enabled
    # streaming=True means responses come back word-by-word instead of all at once
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",  # AWS's Nova Pro model
        model_kwargs={
            "max_tokens": 1000,    # Maximum response length
            "temperature": 0.7     # Creativity level (0=focused, 1=creative)
        },
        streaming=True  # This enables word-by-word streaming
    )
    
    # Create a prompt template that includes:
    # 1. System message (tells AI how to behave)
    # 2. Chat history (remembers previous conversation)
    # 3. Current user input
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AWS assistant. Keep responses concise but informative."),
        MessagesPlaceholder(variable_name="history"),  # This gets filled with chat history
        ("human", "{input}")  # This gets filled with user's current message
    ])
    
    # Chain the prompt and language model together
    # The | operator means "pipe" - send prompt output to LLM
    chain = prompt | llm
    
    # Set up memory to remember conversation history
    # This dictionary will store chat history for different users/sessions
    store = {}
    
    def get_session_history(session_id: str):
        """
        Get or create chat history for a specific session.
        Each user/session gets their own memory.
        """
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
    
    # Wrap our chain with memory capabilities
    # This automatically saves user messages and AI responses
    conversational_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",      # Where to find user input
        history_messages_key="history"   # Where to put chat history
    )
    
    # Create a unique session ID for this conversation
    session_id = "streaming_user"
    
    # Print welcome message
    print("=== Streaming AWS Assistant ===")
    print("Type 'quit', 'exit', or 'q' to exit")
    if debug_mode:
        print("🐛 Debug mode enabled - will show raw streaming chunks")
    print("Responses will stream in real-time...\n")
    
    # Main conversation loop - keeps running until user quits
    while True:
        try:
            # Get user input and remove extra whitespace
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or Ctrl+D gracefully
            print("\nGoodbye!")
            break
        
        # Check if user wants to quit (multiple ways to exit)
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        # Skip empty messages
        if not user_input:
            print("Please enter a message.")
            continue
        
        # Start the bot response (print without newline)
        print("Bot: ", end="", flush=True)
        
        try:
            # Initialize variables for streaming
            raw_chunks = [] if debug_mode else None
            full_response = ""  # Collect full response for memory
            
            # Get session history for manual memory management
            session_history = get_session_history(session_id)
            
            # Add user message to memory
            session_history.add_message(HumanMessage(content=user_input))
            
            # Stream the response from the AI using just the chain (not conversational_chain)
            # We'll handle memory manually since streaming doesn't auto-save
            for chunk in chain.stream({
                "input": user_input,
                "history": session_history.messages[:-1]  # All messages except the one we just added
            }):
                # Save raw chunk for debug display only if in debug mode
                if debug_mode:
                    raw_chunks.append(str(chunk))
                
                # Extract text content from the streaming chunk
                if hasattr(chunk, 'content') and chunk.content:
                    # Handle different chunk content formats
                    content = chunk.content
                    if isinstance(content, list) and len(content) > 0:
                        # Extract text from list format: [{'type': 'text', 'text': 'Hello', 'index': 0}]
                        for item in content:
                            if isinstance(item, dict) and 'text' in item:
                                text = item['text']
                                print(text, end="", flush=True)
                                full_response += text
                    elif isinstance(content, str):
                        # Handle simple string content
                        print(content, end="", flush=True)
                        full_response += content
            
            # Add AI response to memory
            if full_response:
                session_history.add_message(AIMessage(content=full_response))
            
            # Add newline after streaming is complete
            print("\n")
            
            # Show debug information if requested
            if debug_mode and raw_chunks:
                print("\n--- Raw Streaming Chunks (Debug Mode) ---")
                for i, chunk in enumerate(raw_chunks):
                    print(f"Chunk {i+1}: {chunk}")
                print("--- End Debug Info ---\n")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C during streaming
            print("\n[Response interrupted by user]")
            continue
        except Exception as e:
            # Handle any other errors during streaming
            print(f"\nError generating response: {e}")
            if debug_mode:
                # Show full error details in debug mode
                import traceback
                traceback.print_exc()

# This runs the main function only if the script is run directly
# (not if it's imported as a module)
if __name__ == "__main__":
    main()
