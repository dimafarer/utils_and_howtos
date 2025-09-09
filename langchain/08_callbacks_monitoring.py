#!/usr/bin/env python3
"""
Production Monitoring and Callbacks Tutorial

This is the NINTH file in the learning progression (after 07_advanced_prompts.py).
It teaches how to monitor AI applications in production using LangChain's callback system
for tracking performance, usage, costs, and debugging.

What this file demonstrates:
1. Custom callback handlers for monitoring AI usage
2. Tracking metrics like response time, token usage, and costs
3. Logging and debugging AI applications
4. Production observability patterns
5. Performance monitoring and optimization
6. Building dashboards and alerts for AI systems

Prerequisites:
- Run 07_advanced_prompts.py first to understand production-ready AI patterns
- Understand chains, prompts, and basic LangChain concepts
- Basic knowledge of logging and monitoring concepts (helpful)

Next step: Run 09_rag_knowledge_base.py to learn about document-based AI systems
"""

# Import required libraries
import boto3  # AWS SDK for Python - connects to Bedrock service
from langchain_aws import ChatBedrock  # LangChain's wrapper for AWS Bedrock models
from langchain_core.prompts import ChatPromptTemplate  # For creating prompt templates
from langchain_core.output_parsers import StrOutputParser  # For parsing AI responses
from langchain_core.callbacks import BaseCallbackHandler  # Base class for custom callbacks
from typing import Dict, Any, List  # For type hints in callback methods
import time  # For measuring response times
import json  # For formatting structured logs

class MetricsCallback(BaseCallbackHandler):
    """
    Custom callback handler to track AI model usage metrics.
    
    Callbacks in LangChain are called at specific points during AI execution:
    - on_llm_start: When the AI model starts processing
    - on_llm_end: When the AI model finishes processing
    - on_llm_error: When the AI model encounters an error
    
    This allows us to monitor performance, costs, and usage patterns.
    """
    
    def __init__(self):
        """
        Initialize the metrics tracking system.
        
        We'll track various metrics that are important for production AI:
        - Total number of AI calls
        - Total tokens used (affects costs)
        - Total processing time
        - Individual call details for analysis
        """
        self.metrics = {
            "total_calls": 0,        # How many times we've called the AI
            "total_tokens": 0,       # Total tokens used (for cost calculation)
            "total_time": 0,         # Total processing time in seconds
            "calls": []              # Detailed log of each AI call
        }
        self.start_time = None       # Track when each call starts
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs) -> None:
        """
        Called when the AI model starts processing a request.
        
        This is where we start timing the request and log the input details.
        
        Args:
            serialized: Information about the AI model being used
            prompts: The prompts being sent to the AI
            **kwargs: Additional information about the request
        """
        self.start_time = time.time()
        self.metrics["total_calls"] += 1
        
        # Log the start of processing with useful debugging info
        print(f"🚀 LLM call started - Prompt length: {len(prompts[0])} chars")
        
        # In production, you might log this to a monitoring system
        # like CloudWatch, DataDog, or your internal logging system
        if len(prompts[0]) > 1000:
            print("⚠️  Warning: Long prompt detected - may increase costs and latency")
    
    def on_llm_end(self, response, **kwargs) -> None:
        """
        Called when the AI model finishes processing a request.
        
        This is where we calculate metrics like response time, token usage,
        and estimated costs for the completed request.
        
        Args:
            response: The AI's response object
            **kwargs: Additional information about the response
        """
        # Calculate how long this request took
        end_time = time.time()
        duration = end_time - self.start_time if self.start_time else 0
        self.metrics["total_time"] += duration
        
        # Extract response details for metrics
        response_text = ""
        if hasattr(response, 'generations') and response.generations:
            response_text = response.generations[0][0].text
        
        # Estimate token usage (rough approximation)
        # In production, you'd get actual token counts from the model
        estimated_tokens = len(response_text.split()) * 1.3  # Rough estimate
        self.metrics["total_tokens"] += estimated_tokens
        
        # Log completion with performance metrics
        print(f"✅ LLM call completed - Duration: {duration:.2f}s, Est. tokens: {int(estimated_tokens)}")
        
        # Store detailed call information for analysis
        call_details = {
            "timestamp": time.time(),
            "duration": duration,
            "estimated_tokens": int(estimated_tokens),
            "response_length": len(response_text),
            "estimated_cost": estimated_tokens * 0.0001  # Rough cost estimate
        }
        self.metrics["calls"].append(call_details)
        
        # Alert on performance issues
        if duration > 10:  # If response takes more than 10 seconds
            print("⚠️  Performance Alert: Slow response detected!")
        
        if estimated_tokens > 500:  # If response is very long
            print("💰 Cost Alert: High token usage detected!")
    
    def on_llm_error(self, error: Exception, **kwargs) -> None:
        """
        Called when the AI model encounters an error.
        
        This helps us track and debug issues in production.
        
        Args:
            error: The exception that occurred
            **kwargs: Additional error context
        """
        print(f"❌ LLM Error: {error}")
        
        # Log error details for debugging
        error_details = {
            "timestamp": time.time(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "duration": time.time() - self.start_time if self.start_time else 0
        }
        
        # In production, you'd send this to your error tracking system
        print(f"🐛 Error logged: {json.dumps(error_details, indent=2)}")
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of all metrics collected.
        
        This provides insights into AI usage patterns, performance,
        and costs for monitoring and optimization.
        
        Returns:
            Dict containing comprehensive usage statistics
        """
        if self.metrics["total_calls"] == 0:
            return {"message": "No AI calls made yet"}
        
        # Calculate average metrics
        avg_duration = self.metrics["total_time"] / self.metrics["total_calls"]
        avg_tokens = self.metrics["total_tokens"] / self.metrics["total_calls"]
        estimated_total_cost = self.metrics["total_tokens"] * 0.0001
        
        return {
            "total_calls": self.metrics["total_calls"],
            "total_time": round(self.metrics["total_time"], 2),
            "total_tokens": int(self.metrics["total_tokens"]),
            "average_duration": round(avg_duration, 2),
            "average_tokens": int(avg_tokens),
            "estimated_total_cost": round(estimated_total_cost, 4),
            "calls_per_minute": round(self.metrics["total_calls"] / (self.metrics["total_time"] / 60), 2) if self.metrics["total_time"] > 0 else 0
        }

def demonstrate_callback_setup():
    """
    Demonstrate how to set up and use callbacks with LangChain.
    
    This shows the basic pattern for adding monitoring to any LangChain application.
    """
    print("=== 1. Setting Up Production Monitoring ===")
    
    # Create our custom metrics callback
    metrics_callback = MetricsCallback()
    print("✅ Created custom metrics callback")
    
    # Initialize Bedrock connection
    bedrock_client = boto3.client('bedrock-runtime')
    
    # Create ChatBedrock instance
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 500, "temperature": 0.7},
        callbacks=[metrics_callback]  # This is where we add monitoring!
    )
    print("✅ Created monitored AI model with callback")
    
    # Create a simple chain for testing
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful AWS assistant. Answer this question: {question}"
    )
    
    chain = prompt | llm | StrOutputParser()
    print("✅ Created monitored chain")
    
    print("\n💡 Key Monitoring Benefits:")
    print("   - Track performance and response times")
    print("   - Monitor token usage and costs")
    print("   - Debug issues and errors")
    print("   - Optimize AI application performance")
    print("   - Set up alerts for production issues")
    print()
    
    return chain, metrics_callback

def demonstrate_monitoring_in_action(chain, metrics_callback):
    """
    Demonstrate monitoring in action with multiple AI calls.
    
    This shows how the callback system tracks metrics across
    multiple AI interactions.
    
    Args:
        chain: The monitored LangChain chain
        metrics_callback: The metrics callback instance
    """
    print("=== 2. Monitoring AI Calls in Action ===")
    
    # Test questions of varying complexity to show different metrics
    test_questions = [
        "What is AWS Lambda?",
        "Explain the differences between S3 storage classes in detail",
        "How do I set up a complete serverless web application with authentication?"
    ]
    
    print("🧪 Running test questions to demonstrate monitoring...")
    print()
    
    try:
        for i, question in enumerate(test_questions, 1):
            print(f"📝 Question {i}: {question}")
            
            # Make the AI call - the callback will automatically track metrics
            response = chain.invoke({"question": question})
            
            print(f"🤖 Response: {response[:100]}..." if len(response) > 100 else f"🤖 Response: {response}")
            print()
        
        print("✅ All test questions completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        print("The callback system captured this error for debugging")

def demonstrate_metrics_analysis(metrics_callback):
    """
    Demonstrate how to analyze collected metrics for insights.
    
    This shows how to use the monitoring data for optimization
    and production decision-making.
    
    Args:
        metrics_callback: The metrics callback with collected data
    """
    print("=== 3. Analyzing Performance Metrics ===")
    
    # Get comprehensive metrics summary
    summary = metrics_callback.get_summary()
    
    print("📊 Performance Summary:")
    for key, value in summary.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    print("\n💡 Insights for Production Optimization:")
    
    # Provide actionable insights based on metrics
    if summary.get("average_duration", 0) > 5:
        print("   ⚠️  Consider optimizing prompts - responses are slow")
    else:
        print("   ✅ Response times are good")
    
    if summary.get("average_tokens", 0) > 300:
        print("   💰 Consider shorter prompts to reduce costs")
    else:
        print("   ✅ Token usage is reasonable")
    
    if summary.get("calls_per_minute", 0) > 10:
        print("   📈 High usage detected - consider rate limiting")
    else:
        print("   ✅ Usage patterns are normal")
    
    print(f"\n💵 Estimated monthly cost (if this usage continues): ${summary.get('estimated_total_cost', 0) * 30 * 24 * 60:.2f}")

def demonstrate_production_patterns():
    """
    Demonstrate production monitoring patterns and best practices.
    
    This shows how to implement comprehensive monitoring
    for real-world AI applications.
    """
    print("\n=== 4. Production Monitoring Patterns ===")
    
    print("🏭 Production Best Practices:")
    print("   1. ✅ Always use callbacks for monitoring")
    print("   2. ✅ Track costs, performance, and errors")
    print("   3. ✅ Set up alerts for anomalies")
    print("   4. ✅ Log detailed metrics for analysis")
    print("   5. ✅ Monitor token usage to control costs")
    print("   6. ✅ Track user patterns and usage trends")
    
    print("\n📈 Metrics to Monitor in Production:")
    print("   - Response time (latency)")
    print("   - Token usage (costs)")
    print("   - Error rates")
    print("   - Request volume")
    print("   - User satisfaction")
    print("   - Model performance")
    
    print("\n🚨 Alerts to Set Up:")
    print("   - Response time > 10 seconds")
    print("   - Error rate > 5%")
    print("   - Daily costs > budget threshold")
    print("   - Unusual usage patterns")
    print("   - Model availability issues")

def main():
    """
    Main function demonstrating production monitoring for AI applications.
    
    This shows how to implement comprehensive monitoring that's
    essential for running AI applications in production.
    """
    print("=== Production Monitoring and Callbacks Tutorial ===")
    print("Learning how to monitor AI applications like a pro!\n")
    
    # Step 1: Set up monitoring
    chain, metrics_callback = demonstrate_callback_setup()
    
    # Step 2: Monitor AI calls in action
    demonstrate_monitoring_in_action(chain, metrics_callback)
    
    # Step 3: Analyze the collected metrics
    demonstrate_metrics_analysis(metrics_callback)
    
    # Step 4: Show production patterns
    demonstrate_production_patterns()
    
    print("\n🎉 Tutorial Complete!")
    print("You now understand how to monitor AI applications in production!")
    print("\n📚 Key Concepts Learned:")
    print("   ✅ Custom callback handlers for monitoring")
    print("   ✅ Performance and cost tracking")
    print("   ✅ Error monitoring and debugging")
    print("   ✅ Production observability patterns")
    print("   ✅ Metrics analysis and optimization")
    print("   ✅ Alert and monitoring best practices")
    
    print("\nNext step: Run 09_rag_knowledge_base.py to learn about document-based AI systems!")

# This runs the main function only if this file is run directly
if __name__ == "__main__":
    main()
