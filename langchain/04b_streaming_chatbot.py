#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import sys

def main():
    bedrock_client = boto3.client('bedrock-runtime')
    
    # Enable streaming
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 1000, "temperature": 0.7},
        streaming=True
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AWS assistant. Keep responses concise but informative."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm
    
    # Memory setup
    store = {}
    
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
    
    conversational_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    session_id = "streaming_user"
    
    print("=== Streaming AWS Assistant ===")
    print("Type 'quit' to exit")
    print("Responses will stream in real-time...\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        print("Bot: ", end="", flush=True)
        
        try:
            # Stream the response
            full_response = ""
            for chunk in conversational_chain.stream(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            ):
                if hasattr(chunk, 'content'):
                    content = chunk.content
                    print(content, end="", flush=True)
                    full_response += content
            
            print("\n")  # New line after streaming completes
            
        except KeyboardInterrupt:
            print("\n[Interrupted]")
            continue
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
