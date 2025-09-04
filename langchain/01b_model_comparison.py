#!/usr/bin/env python3

import boto3
from langchain_aws import ChatBedrock
import time

# Model configurations
MODELS = {
    "Nova Pro": {
        "id": "us.amazon.nova-pro-v1:0",
        "config": {"max_tokens": 1000, "temperature": 0.7}
    },
    "Nova Lite": {
        "id": "us.amazon.nova-lite-v1:0", 
        "config": {"max_tokens": 1000, "temperature": 0.7}
    },
    "Claude Sonnet": {
        "id": "anthropic.claude-3-5-sonnet-20241022-v2:0",
        "config": {"max_tokens": 1000, "temperature": 0.7}
    }
}

def test_model(model_name, model_info, prompt):
    """Test a single model and return response with timing."""
    try:
        bedrock_client = boto3.client('bedrock-runtime')
        
        chat = ChatBedrock(
            client=bedrock_client,
            model_id=model_info["id"],
            model_kwargs=model_info["config"]
        )
        
        start_time = time.time()
        response = chat.invoke(prompt)
        end_time = time.time()
        
        return {
            "success": True,
            "response": response.content,
            "time": round(end_time - start_time, 2),
            "tokens": len(response.content.split())  # Rough token estimate
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "time": 0,
            "tokens": 0
        }

def main():
    prompt = "Explain AWS Lambda in exactly 50 words."
    
    print("=== Bedrock Model Comparison ===")
    print(f"Prompt: {prompt}\n")
    
    results = {}
    
    for model_name, model_info in MODELS.items():
        print(f"Testing {model_name}...")
        result = test_model(model_name, model_info, prompt)
        results[model_name] = result
        
        if result["success"]:
            print(f"✅ {model_name} ({result['time']}s, ~{result['tokens']} tokens)")
        else:
            print(f"❌ {model_name}: {result['error']}")
        print()
    
    # Display responses
    print("=== Responses ===")
    for model_name, result in results.items():
        if result["success"]:
            print(f"\n{model_name}:")
            print(f"{result['response']}")
            print(f"Time: {result['time']}s | Tokens: ~{result['tokens']}")
    
    # Performance summary
    successful = {k: v for k, v in results.items() if v["success"]}
    if successful:
        fastest = min(successful.items(), key=lambda x: x[1]["time"])
        print(f"\n🏆 Fastest: {fastest[0]} ({fastest[1]['time']}s)")

if __name__ == "__main__":
    main()
