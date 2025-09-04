#!/usr/bin/env python3

import asyncio
import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

async def async_llm_call(llm, prompt_template, input_data, call_id):
    """Make an async LLM call."""
    try:
        start_time = time.time()
        
        # Create chain
        chain = prompt_template | llm | StrOutputParser()
        
        # Make async call
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

async def parallel_processing_demo():
    """Demonstrate parallel processing of multiple LLM calls."""
    
    bedrock_client = boto3.client('bedrock-runtime')
    
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 200, "temperature": 0.7}
    )
    
    prompt = ChatPromptTemplate.from_template(
        "Explain {service} in AWS in exactly 30 words. Focus on {aspect}."
    )
    
    # Multiple tasks to process in parallel
    tasks_data = [
        {"service": "Lambda", "aspect": "cost benefits"},
        {"service": "S3", "aspect": "durability"},
        {"service": "DynamoDB", "aspect": "performance"},
        {"service": "API Gateway", "aspect": "security"},
        {"service": "CloudFormation", "aspect": "automation"}
    ]
    
    print("=== Parallel Processing Demo ===")
    print(f"Processing {len(tasks_data)} requests in parallel...\n")
    
    # Sequential timing (for comparison)
    print("🐌 Sequential Processing:")
    sequential_start = time.time()
    
    sequential_results = []
    for i, task_data in enumerate(tasks_data):
        result = await async_llm_call(llm, prompt, task_data, f"seq_{i}")
        sequential_results.append(result)
        if result["success"]:
            print(f"  ✅ {task_data['service']}: {result['duration']}s")
    
    sequential_total = time.time() - sequential_start
    print(f"Sequential total: {sequential_total:.2f}s\n")
    
    # Parallel processing
    print("🚀 Parallel Processing:")
    parallel_start = time.time()
    
    # Create all tasks
    tasks = [
        async_llm_call(llm, prompt, task_data, f"par_{i}")
        for i, task_data in enumerate(tasks_data)
    ]
    
    # Execute all tasks in parallel
    parallel_results = await asyncio.gather(*tasks)
    
    parallel_total = time.time() - parallel_start
    
    # Display results
    for result in parallel_results:
        if result["success"]:
            service = result["input"]["service"]
            print(f"  ✅ {service}: {result['duration']}s")
        else:
            print(f"  ❌ {result['call_id']}: {result['error']}")
    
    print(f"Parallel total: {parallel_total:.2f}s")
    
    # Performance comparison
    speedup = sequential_total / parallel_total if parallel_total > 0 else 0
    print(f"\n📊 Speedup: {speedup:.1f}x faster with parallel processing")
    
    return parallel_results

async def batch_processing_demo():
    """Demonstrate batch processing with rate limiting."""
    
    bedrock_client = boto3.client('bedrock-runtime')
    
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 100, "temperature": 0.5}
    )
    
    prompt = ChatPromptTemplate.from_template(
        "Rate {service} from 1-10 for {criteria}. Give only the number and one sentence why."
    )
    
    # Large batch of tasks
    services = ["Lambda", "S3", "DynamoDB", "EC2", "RDS", "CloudFront", "SQS", "SNS"]
    criteria = ["ease of use", "cost effectiveness", "scalability"]
    
    batch_tasks = [
        {"service": service, "criteria": criterion}
        for service in services
        for criterion in criteria
    ]
    
    print(f"\n=== Batch Processing Demo ===")
    print(f"Processing {len(batch_tasks)} tasks in batches of 3...\n")
    
    batch_size = 3
    all_results = []
    
    for i in range(0, len(batch_tasks), batch_size):
        batch = batch_tasks[i:i + batch_size]
        print(f"Processing batch {i//batch_size + 1}...")
        
        # Process batch in parallel
        batch_coroutines = [
            async_llm_call(llm, prompt, task_data, f"batch_{i + j}")
            for j, task_data in enumerate(batch)
        ]
        
        batch_results = await asyncio.gather(*batch_coroutines)
        all_results.extend(batch_results)
        
        # Small delay between batches to respect rate limits
        await asyncio.sleep(0.5)
    
    # Summary
    successful = [r for r in all_results if r["success"]]
    failed = [r for r in all_results if not r["success"]]
    
    print(f"\n📊 Batch Results:")
    print(f"  ✅ Successful: {len(successful)}")
    print(f"  ❌ Failed: {len(failed)}")
    
    if successful:
        avg_duration = sum(r["duration"] for r in successful) / len(successful)
        print(f"  ⏱️  Average duration: {avg_duration:.2f}s")

async def main():
    """Main async function."""
    print("=== Async LangChain Operations ===\n")
    
    # Run parallel processing demo
    await parallel_processing_demo()
    
    # Run batch processing demo
    await batch_processing_demo()
    
    print("\n=== Async Benefits ===")
    benefits = [
        "• Improved throughput for multiple requests",
        "• Better resource utilization",
        "• Reduced total processing time",
        "• Handles I/O-bound operations efficiently",
        "• Enables batch processing with rate limiting"
    ]
    
    for benefit in benefits:
        print(benefit)

if __name__ == "__main__":
    asyncio.run(main())
