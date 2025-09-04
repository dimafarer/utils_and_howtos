#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def main():
    # Initialize Bedrock client
    bedrock_client = boto3.client('bedrock-runtime')
    
    # Create ChatBedrock instance
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 1000, "temperature": 0.7}
    )
    
    # Create prompt with message history placeholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AWS assistant. Keep responses concise."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    # Create chain
    chain = prompt | llm | StrOutputParser()
    
    # Store for conversation history
    store = {}
    
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
    
    # Create conversational chain with memory
    conversational_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    # Simulate conversation
    session_id = "user123"
    
    print("=== Conversational Chatbot Demo ===")
    
    # First message
    response1 = conversational_chain.invoke(
        {"input": "What is AWS Lambda?"},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"User: What is AWS Lambda?")
    print(f"Bot: {response1}\n")
    
    # Follow-up message (should remember context)
    response2 = conversational_chain.invoke(
        {"input": "What are its pricing benefits?"},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"User: What are its pricing benefits?")
    print(f"Bot: {response2}")

if __name__ == "__main__":
    main()
