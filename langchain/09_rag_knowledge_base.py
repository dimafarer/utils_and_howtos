#!/usr/bin/env python3
"""
Retrieval Augmented Generation (RAG) Knowledge Base Tutorial

This is the TENTH file in the learning progression (after 08_callbacks_monitoring.py).
It teaches how to build AI systems that can search through documents and use that information
to answer questions, creating intelligent knowledge bases and document-aware AI assistants.

What this file demonstrates:
1. RAG (Retrieval Augmented Generation) architecture and concepts
2. Creating and managing document collections for AI search
3. Vector embeddings and semantic search with FAISS
4. Combining document retrieval with AI generation
5. Building intelligent knowledge bases that can answer questions about documents
6. Production patterns for document-based AI systems

Prerequisites:
- Run 08_callbacks_monitoring.py first to understand production AI patterns
- Understand chains, prompts, and LangChain fundamentals
- Basic understanding of search and databases (helpful)

Next step: Run 10_async_operations.py to learn about scaling AI applications
"""

# Import required libraries
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock, BedrockEmbeddings  # LangChain's wrappers for Bedrock models and embeddings
from langchain_core.prompts import ChatPromptTemplate  # For creating prompt templates
from langchain_core.output_parsers import StrOutputParser  # For parsing AI responses
from langchain_community.vectorstores import FAISS  # Vector database for semantic search
from langchain_core.documents import Document  # For representing documents with content and metadata
from langchain_core.runnables import RunnablePassthrough  # For passing data through chains

def create_sample_knowledge_base():
    """
    Create a sample knowledge base with AWS service information.
    
    This demonstrates how to structure documents for RAG systems.
    Each document should have:
    - page_content: The actual text content to search through
    - metadata: Additional information about the document (source, category, etc.)
    
    Returns:
        List[Document]: A collection of documents for the knowledge base
    """
    print("=== 1. Creating Sample Knowledge Base ===")
    
    # Create documents with comprehensive AWS service information
    # In a real application, these would come from files, databases, or APIs
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
    
    print(f"✅ Created knowledge base with {len(aws_docs)} documents")
    print("💡 Each document contains:")
    print("   - page_content: The searchable text")
    print("   - metadata: Additional information (service, category)")
    print()
    
    # Show example document structure
    print("📄 Example document structure:")
    example_doc = aws_docs[0]
    print(f"   Content: {example_doc.page_content[:100]}...")
    print(f"   Metadata: {example_doc.metadata}")
    print()
    
    return aws_docs

def setup_vector_store(docs):
    """
    Set up a vector store for semantic search using FAISS and Bedrock embeddings.
    
    This demonstrates the core RAG components:
    1. Embeddings: Convert text to numerical vectors
    2. Vector Store: Store and search through document vectors
    3. Semantic Search: Find relevant documents based on meaning, not just keywords
    
    Args:
        docs: List of documents to index
        
    Returns:
        FAISS: The vector store ready for searching
    """
    print("=== 2. Setting Up Vector Store for Semantic Search ===")
    
    # Initialize Bedrock embeddings
    # Embeddings convert text into numerical vectors that capture semantic meaning
    bedrock_client = boto3.client('bedrock-runtime')
    embeddings = BedrockEmbeddings(
        client=bedrock_client,
        model_id="amazon.titan-embed-text-v1"  # AWS's embedding model
    )
    print("✅ Created Bedrock embeddings model")
    
    print("🔄 Converting documents to vectors...")
    print("   This process:")
    print("   1. Takes each document's text content")
    print("   2. Converts it to a numerical vector (embedding)")
    print("   3. Stores vectors in FAISS for fast similarity search")
    
    # Create FAISS vector store from documents
    # FAISS (Facebook AI Similarity Search) is a library for efficient similarity search
    vectorstore = FAISS.from_documents(docs, embeddings)
    
    print("✅ Vector store created with FAISS")
    print("💡 Benefits of vector search:")
    print("   - Semantic understanding (finds meaning, not just keywords)")
    print("   - Fast similarity search across large document collections")
    print("   - Handles synonyms and related concepts automatically")
    print()
    
    return vectorstore

def format_docs(docs):
    """
    Format retrieved documents for inclusion in AI prompts.
    
    This helper function takes the documents found by the vector search
    and formats them in a way that's useful for the AI to read and understand.
    
    Args:
        docs: List of retrieved documents
        
    Returns:
        str: Formatted text combining all document content
    """
    # Combine document content with service information
    # This gives the AI context about where each piece of information comes from
    formatted_text = "\n\n".join([
        f"Service: {doc.metadata['service']}\n{doc.page_content}" 
        for doc in docs
    ])
    return formatted_text

def demonstrate_semantic_search(vectorstore):
    """
    Demonstrate semantic search capabilities of the vector store.
    
    This shows how vector search finds relevant documents based on
    meaning rather than exact keyword matches.
    
    Args:
        vectorstore: The FAISS vector store to search
    """
    print("=== 3. Demonstrating Semantic Search ===")
    
    # Test queries that demonstrate semantic understanding
    test_queries = [
        "serverless computing",  # Should find Lambda
        "file storage",         # Should find S3
        "NoSQL database",       # Should find DynamoDB
        "REST API management"   # Should find API Gateway
    ]
    
    print("🔍 Testing semantic search with various queries:")
    
    for query in test_queries:
        print(f"\n📝 Query: '{query}'")
        
        # Search for relevant documents
        # k=2 means return the top 2 most relevant documents
        relevant_docs = vectorstore.similarity_search(query, k=2)
        
        print("📋 Most relevant documents:")
        for i, doc in enumerate(relevant_docs, 1):
            service = doc.metadata.get('service', 'Unknown')
            content_preview = doc.page_content[:100] + "..."
            print(f"   {i}. {service}: {content_preview}")
    
    print("\n💡 Notice how semantic search finds relevant documents")
    print("   even when the exact words don't match the query!")
    print()

def create_rag_chain(vectorstore):
    """
    Create a complete RAG (Retrieval Augmented Generation) chain.
    
    This combines document retrieval with AI generation to create
    a system that can answer questions using information from documents.
    
    The RAG process:
    1. User asks a question
    2. System searches documents for relevant information
    3. AI generates answer using both the question and retrieved documents
    
    Args:
        vectorstore: The vector store for document retrieval
        
    Returns:
        Chain: Complete RAG chain ready for question answering
    """
    print("=== 4. Building Complete RAG Chain ===")
    
    # Initialize the AI model for generation
    bedrock_client = boto3.client('bedrock-runtime')
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 1000, "temperature": 0.7}
    )
    print("✅ Created AI model for answer generation")
    
    # Create a prompt template that includes both context and question
    # This is crucial for RAG - the AI needs both the retrieved documents and the user's question
    prompt = ChatPromptTemplate.from_template("""
Answer the question based on the following context from AWS documentation:

Context:
{context}

Question: {question}

Answer: Provide a comprehensive answer based on the context above. If the context doesn't contain enough information, say so.
""")
    print("✅ Created RAG prompt template")
    
    # Create the retriever from the vector store
    # This will automatically find relevant documents for any question
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}  # Retrieve top 3 most relevant documents
    )
    print("✅ Created document retriever")
    
    # Build the complete RAG chain using LCEL (LangChain Expression Language)
    # This chain: retrieves documents → formats them → generates answer
    rag_chain = (
        {
            "context": retriever | format_docs,  # Retrieve and format relevant documents
            "question": RunnablePassthrough()     # Pass the question through unchanged
        }
        | prompt      # Combine context and question in prompt
        | llm         # Generate answer with AI
        | StrOutputParser()  # Parse response to clean string
    )
    
    print("✅ Created complete RAG chain")
    print("🔗 RAG Chain Flow:")
    print("   Question → Document Retrieval → Context Formatting → AI Generation → Answer")
    print()
    
    return rag_chain

def demonstrate_rag_qa(rag_chain):
    """
    Demonstrate the RAG system answering questions using document knowledge.
    
    This shows how the system can answer questions by finding and using
    relevant information from the knowledge base.
    
    Args:
        rag_chain: The complete RAG chain
    """
    print("=== 5. RAG Question Answering Demo ===")
    
    # Test questions that require information from different documents
    test_questions = [
        "What is AWS Lambda and what languages does it support?",
        "How durable is S3 storage and what storage classes are available?",
        "What type of database is DynamoDB and what are its performance characteristics?",
        "How does API Gateway help with API management?"
    ]
    
    print("🤖 Testing RAG system with knowledge-based questions:")
    
    try:
        for i, question in enumerate(test_questions, 1):
            print(f"\n❓ Question {i}: {question}")
            
            # Get answer from RAG system
            # The system will automatically:
            # 1. Search for relevant documents
            # 2. Use that information to generate an answer
            answer = rag_chain.invoke(question)
            
            print(f"🎯 RAG Answer: {answer}")
            print("-" * 80)
        
        print("\n✅ RAG demonstration completed!")
        print("💡 Notice how the AI uses specific information from the documents")
        print("   to provide accurate, detailed answers!")
        
    except Exception as e:
        print(f"❌ Error during RAG demonstration: {e}")
        print("🔧 Check your AWS credentials and Bedrock model access")

def demonstrate_production_patterns():
    """
    Demonstrate production patterns and best practices for RAG systems.
    
    This covers important considerations for deploying RAG systems
    in real-world applications.
    """
    print("\n=== 6. Production RAG Patterns ===")
    
    print("🏭 Production Best Practices:")
    print("   1. ✅ Document preprocessing and chunking")
    print("   2. ✅ Efficient vector storage and indexing")
    print("   3. ✅ Relevance scoring and filtering")
    print("   4. ✅ Caching for frequently asked questions")
    print("   5. ✅ Monitoring retrieval quality")
    print("   6. ✅ Regular knowledge base updates")
    
    print("\n📊 Key Metrics to Monitor:")
    print("   - Retrieval accuracy (are the right documents found?)")
    print("   - Answer quality (are responses helpful and accurate?)")
    print("   - Response time (how fast is the system?)")
    print("   - User satisfaction (are users getting what they need?)")
    
    print("\n🔧 Optimization Strategies:")
    print("   - Chunk documents appropriately (not too big, not too small)")
    print("   - Use metadata filtering for better relevance")
    print("   - Implement hybrid search (vector + keyword)")
    print("   - Cache embeddings to reduce costs")
    print("   - Use re-ranking for better results")

def main():
    """
    Main function demonstrating complete RAG system implementation.
    
    This walks through building a production-ready RAG system
    from document creation to question answering.
    """
    print("=== RAG (Retrieval Augmented Generation) Tutorial ===")
    print("Learning how to build AI systems that can search and use documents!\n")
    
    try:
        # Step 1: Create sample knowledge base
        print("📚 Creating knowledge base...")
        docs = create_sample_knowledge_base()
        
        # Step 2: Set up vector store for semantic search
        vectorstore = setup_vector_store(docs)
        
        # Step 3: Demonstrate semantic search capabilities
        demonstrate_semantic_search(vectorstore)
        
        # Step 4: Build complete RAG chain
        rag_chain = create_rag_chain(vectorstore)
        
        # Step 5: Demonstrate question answering
        demonstrate_rag_qa(rag_chain)
        
        # Step 6: Show production patterns
        demonstrate_production_patterns()
        
        print("\n🎉 Tutorial Complete!")
        print("You now understand how to build intelligent document-based AI systems!")
        print("\n📚 Key Concepts Learned:")
        print("   ✅ RAG (Retrieval Augmented Generation) architecture")
        print("   ✅ Vector embeddings and semantic search")
        print("   ✅ Document indexing and retrieval")
        print("   ✅ Combining search with AI generation")
        print("   ✅ Building intelligent knowledge bases")
        print("   ✅ Production RAG patterns and best practices")
        
        print("\nNext step: Run 10_async_operations.py to learn about scaling AI applications!")
        
    except Exception as e:
        print(f"❌ Error during RAG tutorial: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Check your AWS credentials are configured")
        print("2. Verify Bedrock model access (both LLM and embeddings)")
        print("3. Ensure you have proper IAM permissions")
        print("4. Check that FAISS is properly installed")

# This runs the main function only if this file is run directly
if __name__ == "__main__":
    main()
