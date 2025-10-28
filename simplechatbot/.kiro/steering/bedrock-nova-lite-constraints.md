---
inclusion: always
---

# Bedrock Nova Lite Technical Constraints

## Model Specifications
- **Model ID**: `amazon.nova-lite-v1:0` (exact string required)
- **Student Environment**: Nova Lite is the ONLY model available to students
- **Development Environment**: All Bedrock models available, but use Nova Lite for consistency

## API Configuration Requirements

### Client Setup
```python
# Simple boto3 client configuration for students
client = boto3.client('bedrock-runtime')
# Region and timeouts will be configured via environment variables
```

### Request Format
Nova Lite requires specific message structure:
```python
request = {
    "messages": [
        {
            "role": "user",
            "content": [{"text": "message text here"}]
        }
    ],
    "inferenceConfig": {
        "maxTokens": 1000,
        "temperature": 0.7,
        "topP": 0.9
    }
}
```

### Response Format
Nova Lite returns responses in this structure:
```python
response = {
    "output": {
        "message": {
            "role": "assistant",
            "content": [{"text": "response text here"}]
        }
    },
    "usage": {
        "inputTokens": 10,
        "outputTokens": 15,
        "totalTokens": 25
    }
}
```

## Authentication Requirements
- **Student Environment**: AWS credentials must be configured for Nova Lite access
- **No hardcoded credentials** in educational code
- **Environment variables** or AWS CLI configuration preferred
- **Clear setup instructions** needed for student environments

## Performance Considerations
- **Token Limits**: Nova Lite has approximately 5K token context window
- **Response Time**: Can take up to 60 minutes (hence timeout configuration)
- **Rate Limiting**: Handle gracefully with educational explanations
- **Conversation Truncation**: Implement for long conversations

## Error Handling Priorities
1. **Simple error messages** - basic print statements only
2. **Assume AWS is configured** - don't overcomplicate setup
3. **No mock responses** - keep it real and simple
4. **Basic troubleshooting** - just point to AWS CLI setup