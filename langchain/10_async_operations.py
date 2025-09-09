#!/usr/bin/env python3
"""
Asynchronous and Concurrent AI Operations Tutorial

This is the FINAL file in the learning progression (after 09_rag_knowledge_base.py).
It teaches how to scale AI applications using asynchronous programming patterns,
enabling concurrent processing and better performance for production systems.

What this file demonstrates:
1. Async/await patterns for AI operations
2. Concurrent processing of multiple AI requests
3. Performance optimization through parallelization
4. Batch processing and rate limiting
5. Error handling in concurrent environments
6. Production scaling patterns for AI applications

Prerequisites:
- Run 09_rag_knowledge_base.py first to understand document-based AI systems
- Complete understanding of all previous LangChain concepts
- Basic knowledge of async programming in Python (helpful)

Congratulations: This is the final file in the series - you'll be a LangChain expert!
"""

# Import required libraries
import asyncio  # Python's async programming library
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock models
from langchain_core.prompts import ChatPromptTemplate  # For creating prompt templates
from langchain_core.output_parsers import StrOutputParser  # For parsing AI responses
import time  # For measuring performance differences
from typing import List, Dict, Any  # For type hints

async def async_llm_call(llm, prompt_template, input_data, call_id):
    """
    Make an asynchronous AI model call.
    
    This demonstrates the basic pattern for async AI operations.
    The 'async' keyword makes this function non-blocking, allowing
    other operations to run while waiting for the AI response.
    
    Args:
        llm: The AI model instance
        prompt_template: The prompt template to use
        input_data: Data to fill the template
        call_id: Unique identifier for this call
        
    Returns:
        Dict containing call results and metadata
    """
    try:
        start_time = time.time()
        
        # Create chain (same pattern as synchronous version)
        chain = prompt_template | llm | StrOutputParser()
        
        # Make async call using ainvoke instead of invoke
        # The 'await' keyword waits for the result without blocking other operations
        response = await chain.ainvoke(input_data)
        
        end_time = time.time()
        duration = end_time - start_time
        
        return {
            "call_id": call_id,
            "success": True,
            "response": response,
            "duration": round(duration, 2),
            "input": input_data
        }
        
    except Exception as e:
        return {
            "call_id": call_id,
            "success": False,
            "error": str(e),
            "duration": 0,
            "input": input_data
        }

def demonstrate_sync_vs_async_performance():
    """
    Demonstrate the performance difference between synchronous and asynchronous operations.
    
    This shows why async programming is crucial for scaling AI applications
    when you need to process multiple requests.
    """
    print("=== 1. Synchronous vs Asynchronous Performance ===")
    
    print("🐌 Synchronous Processing:")
    print("   Request 1 → Wait → Complete → Request 2 → Wait → Complete → Request 3 → Wait → Complete")
    print("   Total time: Sum of all individual wait times")
    print()
    
    print("⚡ Asynchronous Processing:")
    print("   Request 1 → Start waiting")
    print("   Request 2 → Start waiting  } All happen")
    print("   Request 3 → Start waiting  } concurrently")
    print("   All complete around the same time")
    print("   Total time: Approximately the time of the longest individual request")
    print()
    
    print("💡 Performance Benefits:")
    print("   - Process multiple AI requests simultaneously")
    print("   - Better resource utilization")
    print("   - Improved user experience (faster overall response)")
    print("   - Essential for high-throughput applications")
    print()

async def demonstrate_concurrent_processing():
    """
    Demonstrate concurrent processing of multiple AI requests.
    
    This shows how to process multiple AI calls at the same time
    instead of waiting for each one to complete sequentially.
    """
    print("=== 2. Concurrent AI Processing Demo ===")
    
    # Initialize Bedrock client and model
    bedrock_client = boto3.client('bedrock-runtime')
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 200, "temperature": 0.7}
    )
    print("✅ Created async-capable AI model")
    
    # Create prompt template for AWS service explanations
    prompt = ChatPromptTemplate.from_template(
        "Explain {service} in exactly 2 sentences. Be concise and informative."
    )
    print("✅ Created prompt template")
    
    # Define multiple AI tasks to process concurrently
    tasks_data = [
        {"service": "AWS Lambda", "call_id": "lambda_call"},
        {"service": "Amazon S3", "call_id": "s3_call"},
        {"service": "Amazon DynamoDB", "call_id": "dynamodb_call"},
        {"service": "Amazon API Gateway", "call_id": "apigateway_call"},
        {"service": "AWS CloudFormation", "call_id": "cloudformation_call"}
    ]
    
    print(f"🚀 Processing {len(tasks_data)} AI requests concurrently...")
    
    # Measure concurrent processing time
    start_time = time.time()
    
    # Create async tasks for all AI calls
    # asyncio.gather runs all tasks concurrently and waits for all to complete
    tasks = [
        async_llm_call(llm, prompt, {"service": task["service"]}, task["call_id"])
        for task in tasks_data
    ]
    
    # Execute all tasks concurrently
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    total_duration = end_time - start_time
    
    print(f"✅ All {len(tasks_data)} requests completed in {total_duration:.2f} seconds")
    print()
    
    # Display results
    print("📋 Concurrent Processing Results:")
    successful_calls = 0
    total_individual_time = 0
    
    for result in results:
        if result["success"]:
            successful_calls += 1
            total_individual_time += result["duration"]
            service = result["input"]["service"]
            response_preview = result["response"][:100] + "..." if len(result["response"]) > 100 else result["response"]
            print(f"   ✅ {service}: {response_preview}")
            print(f"      Individual time: {result['duration']}s")
        else:
            print(f"   ❌ {result['call_id']}: {result['error']}")
    
    print(f"\n📊 Performance Analysis:")
    print(f"   Successful calls: {successful_calls}/{len(tasks_data)}")
    print(f"   Total concurrent time: {total_duration:.2f}s")
    print(f"   Sum of individual times: {total_individual_time:.2f}s")
    print(f"   Time saved: {total_individual_time - total_duration:.2f}s")
    print(f"   Efficiency gain: {(total_individual_time / total_duration):.1f}x faster")
    print()

async def demonstrate_batch_processing_with_limits():
    """
    Demonstrate batch processing with rate limiting.
    
    This shows how to process large numbers of requests efficiently
    while respecting API rate limits and avoiding overwhelming the system.
    """
    print("=== 3. Batch Processing with Rate Limiting ===")
    
    # Initialize components
    bedrock_client = boto3.client('bedrock-runtime')
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 100, "temperature": 0.7}
    )
    
    prompt = ChatPromptTemplate.from_template(
        "What is the main benefit of {service}? Answer in one sentence."
    )
    
    # Simulate a large batch of requests
    large_batch = [
        {"service": "AWS Lambda"},
        {"service": "Amazon S3"},
        {"service": "Amazon DynamoDB"},
        {"service": "Amazon RDS"},
        {"service": "Amazon EC2"},
        {"service": "Amazon VPC"},
        {"service": "AWS IAM"},
        {"service": "Amazon CloudWatch"},
        {"service": "AWS CloudTrail"},
        {"service": "Amazon SNS"}
    ]
    
    print(f"📦 Processing batch of {len(large_batch)} requests")
    
    # Process in smaller batches to respect rate limits
    batch_size = 3  # Process 3 requests at a time
    print(f"⚡ Using batch size of {batch_size} for rate limiting")
    
    all_results = []
    
    for i in range(0, len(large_batch), batch_size):
        batch = large_batch[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        
        print(f"\n🔄 Processing batch {batch_num} ({len(batch)} requests)...")
        
        # Process current batch concurrently
        tasks = [
            async_llm_call(llm, prompt, item, f"batch_{batch_num}_item_{j}")
            for j, item in enumerate(batch)
        ]
        
        batch_results = await asyncio.gather(*tasks)
        all_results.extend(batch_results)
        
        # Show batch completion
        successful_in_batch = sum(1 for r in batch_results if r["success"])
        print(f"   ✅ Batch {batch_num} completed: {successful_in_batch}/{len(batch)} successful")
        
        # Add delay between batches to respect rate limits
        if i + batch_size < len(large_batch):  # Don't delay after the last batch
            print("   ⏳ Waiting 1 second before next batch (rate limiting)...")
            await asyncio.sleep(1)
    
    # Summary
    total_successful = sum(1 for r in all_results if r["success"])
    print(f"\n📊 Batch Processing Summary:")
    print(f"   Total requests: {len(large_batch)}")
    print(f"   Successful: {total_successful}")
    print(f"   Batch size: {batch_size}")
    print(f"   Total batches: {(len(large_batch) + batch_size - 1) // batch_size}")
    print()

async def demonstrate_error_handling_patterns():
    """
    Demonstrate error handling patterns in concurrent AI operations.
    
    This shows how to handle errors gracefully when processing
    multiple AI requests concurrently.
    """
    print("=== 4. Error Handling in Concurrent Operations ===")
    
    print("🛡️ Error Handling Strategies:")
    print("   1. ✅ Individual error isolation (one failure doesn't stop others)")
    print("   2. ✅ Retry logic for transient failures")
    print("   3. ✅ Graceful degradation (partial results are still useful)")
    print("   4. ✅ Comprehensive error logging")
    print("   5. ✅ Circuit breaker patterns for system protection")
    print()
    
    # Initialize components
    bedrock_client = boto3.client('bedrock-runtime')
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 100, "temperature": 0.7}
    )
    
    prompt = ChatPromptTemplate.from_template("Explain {topic} briefly.")
    
    # Mix of valid and potentially problematic requests
    mixed_requests = [
        {"topic": "AWS Lambda"},  # Valid
        {"topic": ""},  # Empty topic (might cause issues)
        {"topic": "Amazon S3"},  # Valid
        {"topic": "A" * 1000},  # Very long topic (might cause issues)
        {"topic": "DynamoDB"}  # Valid
    ]
    
    print("🧪 Testing error handling with mixed request types...")
    
    # Process all requests, handling errors individually
    tasks = [
        async_llm_call(llm, prompt, request, f"error_test_{i}")
        for i, request in enumerate(mixed_requests)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Analyze results
    successful = []
    failed = []
    
    for result in results:
        if isinstance(result, dict) and result.get("success"):
            successful.append(result)
        else:
            failed.append(result)
    
    print(f"📊 Error Handling Results:")
    print(f"   Successful requests: {len(successful)}")
    print(f"   Failed requests: {len(failed)}")
    print(f"   Success rate: {len(successful) / len(mixed_requests) * 100:.1f}%")
    print()
    
    print("💡 Key Benefits of Async Error Handling:")
    print("   - Individual failures don't block other requests")
    print("   - Partial results are still valuable")
    print("   - Better user experience (some results vs no results)")
    print("   - Easier to identify and fix specific issues")
    print()

def demonstrate_production_patterns():
    """
    Demonstrate production patterns for scaling AI applications.
    
    This covers best practices for deploying async AI systems
    in real-world, high-traffic environments.
    """
    print("=== 5. Production Scaling Patterns ===")
    
    print("🏭 Production Best Practices:")
    print("   1. ✅ Connection pooling for efficient resource usage")
    print("   2. ✅ Request queuing and prioritization")
    print("   3. ✅ Circuit breakers to prevent cascade failures")
    print("   4. ✅ Monitoring and alerting for async operations")
    print("   5. ✅ Graceful shutdown and cleanup")
    print("   6. ✅ Load balancing across multiple AI endpoints")
    
    print("\n📈 Scaling Strategies:")
    print("   - Horizontal scaling: Multiple AI service instances")
    print("   - Vertical scaling: More powerful hardware")
    print("   - Caching: Store results for common requests")
    print("   - Rate limiting: Protect against overload")
    print("   - Batch optimization: Group similar requests")
    
    print("\n🚨 Monitoring Metrics:")
    print("   - Concurrent request count")
    print("   - Average response time")
    print("   - Error rates by request type")
    print("   - Queue depth and processing lag")
    print("   - Resource utilization (CPU, memory)")
    
    print("\n⚡ Performance Optimization Tips:")
    print("   - Use appropriate batch sizes for your use case")
    print("   - Implement request deduplication")
    print("   - Cache embeddings and common responses")
    print("   - Use streaming for long responses")
    print("   - Implement smart retry logic with exponential backoff")

async def main():
    """
    Main async function demonstrating all concurrent AI patterns.
    
    This brings together all the concepts to show how to build
    scalable, production-ready AI applications.
    """
    print("=== Asynchronous and Concurrent AI Operations Tutorial ===")
    print("Learning how to scale AI applications for production!\n")
    
    try:
        # Step 1: Explain sync vs async benefits
        demonstrate_sync_vs_async_performance()
        
        # Step 2: Demonstrate concurrent processing
        await demonstrate_concurrent_processing()
        
        # Step 3: Show batch processing with rate limiting
        await demonstrate_batch_processing_with_limits()
        
        # Step 4: Demonstrate error handling
        await demonstrate_error_handling_patterns()
        
        # Step 5: Show production patterns
        demonstrate_production_patterns()
        
        print("\n🎉 CONGRATULATIONS! Tutorial Series Complete! 🎉")
        print("You've mastered LangChain and are ready for production AI development!")
        print("\n🏆 What You've Accomplished:")
        print("   ✅ Environment setup and basic AI connections")
        print("   ✅ Prompt engineering and template mastery")
        print("   ✅ Conversational AI with memory")
        print("   ✅ Real-time streaming applications")
        print("   ✅ Multi-step AI workflows and chaining")
        print("   ✅ Advanced prompt patterns and structured outputs")
        print("   ✅ Production monitoring and observability")
        print("   ✅ Document-based AI systems (RAG)")
        print("   ✅ Asynchronous and concurrent AI operations")
        
        print("\n🚀 You're Now Ready For:")
        print("   - Building production AI applications")
        print("   - Scaling AI systems for high traffic")
        print("   - Advanced LangChain patterns and integrations")
        print("   - Contributing to AI/ML projects")
        print("   - Exploring cutting-edge AI technologies")
        
        print("\n📚 Continue Your Journey:")
        print("   - Explore LangChain's advanced features")
        print("   - Build your own AI applications")
        print("   - Contribute to open-source AI projects")
        print("   - Stay updated with the latest AI developments")
        
    except Exception as e:
        print(f"❌ Error during async tutorial: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Check your AWS credentials are configured")
        print("2. Verify Bedrock model access")
        print("3. Ensure you have proper IAM permissions")
        print("4. Check your Python async/await syntax")

# Entry point for the async application
# We need to use asyncio.run() to execute the async main function
if __name__ == "__main__":
    # Run the async main function
    # This is the standard pattern for async Python applications
    asyncio.run(main())
