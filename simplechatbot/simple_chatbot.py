"""
Simple Chatbot - Minimal LLM conversation loop

A bare-bones chatbot that demonstrates:
- User input loop
- Conversation memory in a list
- Real API calls to Nova Lite
- No tests, demos, or educational features
"""

import boto3
import json


def main():
    """Simple chatbot loop"""
    # Setup
    client = boto3.client('bedrock-runtime')
    conversation = []
    
    print("Simple Chatbot (type 'quit' to exit)")
    
    # Main loop
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Exit check
        if user_input.lower() in ['quit', 'exit']:
            break
            
        if not user_input:
            continue
        
        # Add user message to conversation
        conversation.append({"role": "user", "content": [{"text": user_input}]})
        
        # Prepare API request
        request = {
            "messages": conversation,
            "inferenceConfig": {
                "maxTokens": 1000,
                "temperature": 0.7
            }
        }
        
        # Call Nova Lite via inference profile
        response = client.invoke_model(
            modelId="us.amazon.nova-lite-v1:0",
            body=json.dumps(request)
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        assistant_message = response_body['output']['message']
        
        # Add assistant response to conversation
        conversation.append(assistant_message)
        
        # Show response
        print(f"Assistant: {assistant_message['content'][0]['text']}")


if __name__ == "__main__":
    main()