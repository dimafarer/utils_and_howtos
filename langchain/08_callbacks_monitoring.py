#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.callbacks import BaseCallbackHandler
from typing import Dict, Any, List
import time
import json

class MetricsCallback(BaseCallbackHandler):
    """Custom callback to track model usage metrics."""
    
    def __init__(self):
        self.metrics = {
            "total_calls": 0,
            "total_tokens": 0,
            "total_time": 0,
            "calls": []
        }
        self.start_time = None
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs) -> None:
        """Called when LLM starts running."""
        self.start_time = time.time()
        print(f"🚀 LLM call started - Prompt length: {len(prompts[0])} chars")
    
    def on_llm_end(self, response, **kwargs) -> None:
        """Called when LLM ends running."""
        end_time = time.time()
        duration = end_time - self.start_time if self.start_time else 0
        
        # Estimate tokens (rough approximation)
        response_text = str(response.generations[0][0].text)
        estimated_tokens = len(response_text.split())
        
        self.metrics["total_calls"] += 1
        self.metrics["total_tokens"] += estimated_tokens
        self.metrics["total_time"] += duration
        
        call_data = {
            "duration": round(duration, 2),
            "tokens": estimated_tokens,
            "timestamp": time.time()
        }
        self.metrics["calls"].append(call_data)
        
        print(f"✅ LLM call completed - Duration: {duration:.2f}s, Tokens: ~{estimated_tokens}")
    
    def on_llm_error(self, error: Exception, **kwargs) -> None:
        """Called when LLM encounters an error."""
        print(f"❌ LLM error: {error}")
    
    def get_summary(self):
        """Get metrics summary."""
        if self.metrics["total_calls"] == 0:
            return "No calls made yet"
        
        avg_time = self.metrics["total_time"] / self.metrics["total_calls"]
        avg_tokens = self.metrics["total_tokens"] / self.metrics["total_calls"]
        
        return {
            "total_calls": self.metrics["total_calls"],
            "total_tokens": self.metrics["total_tokens"],
            "total_time": round(self.metrics["total_time"], 2),
            "avg_time_per_call": round(avg_time, 2),
            "avg_tokens_per_call": round(avg_tokens, 1)
        }

def main():
    # Initialize callback
    metrics_callback = MetricsCallback()
    
    bedrock_client = boto3.client('bedrock-runtime')
    
    llm = ChatBedrock(
        client=bedrock_client,
        model_id="us.amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 500, "temperature": 0.7},
        callbacks=[metrics_callback]  # Add callback
    )
    
    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in AWS in exactly {word_count} words."
    )
    
    chain = prompt | llm | StrOutputParser()
    
    print("=== LangChain Callbacks & Monitoring Demo ===\n")
    
    # Test multiple calls to demonstrate monitoring
    test_topics = [
        {"topic": "Lambda", "word_count": "30"},
        {"topic": "S3", "word_count": "25"},
        {"topic": "DynamoDB", "word_count": "35"}
    ]
    
    for i, test_case in enumerate(test_topics, 1):
        print(f"--- Call {i}: {test_case['topic']} ---")
        
        try:
            response = chain.invoke(test_case)
            print(f"Response: {response}\n")
            
        except Exception as e:
            print(f"Error: {e}\n")
    
    # Display metrics summary
    print("=== Metrics Summary ===")
    summary = metrics_callback.get_summary()
    
    if isinstance(summary, dict):
        print(json.dumps(summary, indent=2))
        
        # Performance insights
        if summary["avg_time_per_call"] > 3:
            print("\n⚠️  Average response time is high (>3s)")
        if summary["avg_tokens_per_call"] > 100:
            print("💰 High token usage - consider shorter prompts")
    else:
        print(summary)

if __name__ == "__main__":
    main()
