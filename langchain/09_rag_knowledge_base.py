#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock, BedrockEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough

def create_sample_knowledge_base():
    """Create a sample knowledge base with AWS service information."""
    
    aws_docs = [
        Document(
            page_content="AWS Lambda is a serverless compute service that runs code without provisioning servers. It automatically scales and charges only for compute time used. Supports multiple languages including Python, Node.js, Java, and Go.",
            metadata={"service": "Lambda", "category": "Compute"}
        ),
        Document(
            page_content="Amazon S3 is object storage with 99.999999999% durability. It offers multiple storage classes for different use cases: Standard, IA, Glacier, and Deep Archive. Supports versioning, encryption, and lifecycle policies.",
            metadata={"service": "S3", "category": "Storage"}
        ),
        Document(
            page_content="Amazon DynamoDB is a NoSQL database service with single-digit millisecond performance. It offers on-demand and provisioned billing modes. Supports global tables for multi-region replication.",
            metadata={"service": "DynamoDB", "category": "Database"}
        ),
        Document(
            page_content="Amazon API Gateway is a managed service for creating REST and WebSocket APIs. It handles authentication, throttling, caching, and monitoring. Integrates with Lambda, EC2, and other AWS services.",
            metadata={"service": "API Gateway", "category": "Networking"}
        ),
        Document(
            page_content="AWS CloudFormation is infrastructure as code service. It uses JSON or YAML templates to provision AWS resources. Supports rollback, change sets, and stack policies for safe deployments.",
            metadata={"service": "CloudFormation", "category": "Management"}
        )
    ]
    
    return aws_docs

def format_docs(docs):
    """Format retrieved documents for the prompt."""
    return "\n\n".join([f"Service: {doc.metadata['service']}\n{doc.page_content}" for doc in docs])

def main():
    print("=== RAG with AWS Knowledge Base ===")
    
    # Initialize Bedrock clients
    bedrock_client = boto3.client('bedrock-runtime')
    
    # Create embeddings model
    embeddings = BedrockEmbeddings(
        client=bedrock_client,
        model_id="amazon.titan-embed-text-v1"
    )
    
    # Create LLM
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 500, "temperature": 0.3}
    )
    
    print("📚 Creating knowledge base...")
    
    # Create and populate vector store
    docs = create_sample_knowledge_base()
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    
    # Create RAG prompt
    rag_prompt = ChatPromptTemplate.from_template("""
Use the following AWS service information to answer the question. If the information isn't in the context, say so.

Context:
{context}

Question: {question}

Answer:""")
    
    # Create RAG chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )
    
    print("✅ Knowledge base ready!\n")
    
    # Test questions
    test_questions = [
        "What is AWS Lambda and how does it work?",
        "Which storage service should I use for archival data?",
        "How does DynamoDB handle scaling?",
        "What is the difference between S3 and DynamoDB?",
        "Tell me about AWS Fargate"  # Not in knowledge base
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"--- Question {i} ---")
        print(f"Q: {question}")
        
        try:
            # Get relevant documents first (for demonstration)
            relevant_docs = retriever.get_relevant_documents(question)
            print(f"📖 Retrieved {len(relevant_docs)} relevant documents")
            
            # Get RAG response
            response = rag_chain.invoke(question)
            print(f"A: {response}\n")
            
        except Exception as e:
            print(f"Error: {e}\n")
    
    print("=== RAG Benefits ===")
    benefits = [
        "• Provides factual, up-to-date information",
        "• Reduces hallucinations by grounding responses",
        "• Allows querying private/custom knowledge",
        "• Maintains source attribution",
        "• Scales with document collection size"
    ]
    
    for benefit in benefits:
        print(benefit)

if __name__ == "__main__":
    main()
