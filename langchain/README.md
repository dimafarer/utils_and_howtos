# LangChain + AWS Bedrock Learning Examples

Progressive examples for learning LangChain with AWS Bedrock, from basic concepts to advanced patterns.

## Setup

1. **Environment Check**
   ```bash
   python 00_environment_setup.py
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**
   - Ensure AWS credentials are configured via AWS CLI, environment variables, or IAM roles
   - Verify Bedrock model access in AWS console

## Learning Progression

### Foundation (Files 01-02)
- **01_langchain_bedrock_basic.py** - Basic Bedrock connection and simple invoke
- **01b_model_comparison.py** - Compare different Bedrock models (Nova, Claude)
- **02_langchain_prompts_chains.py** - Prompt templates and LCEL chains
- **02b_advanced_prompts.py** - Prompt composition, structured output, few-shot learning

### Conversational AI (Files 03-04)
- **03_conversational_memory_chatbot.py** - Add memory to conversations
- **04_interactive_cli_chatbot.py** - Interactive CLI implementation
- **04b_streaming_chatbot.py** - Real-time streaming responses

### Advanced Chaining (Files 05-06)
- **05_aws_architecture_chaining.py** - Multi-step architecture advisor
- **06_aws_troubleshooting_chaining.py** - Sequential troubleshooting chains

### Production Patterns (Files 07-10)
- **07_guardrails_safety.py** - Safety and content filtering
- **08_callbacks_monitoring.py** - Metrics, monitoring, and callbacks
- **09_rag_knowledge_base.py** - Retrieval Augmented Generation (RAG)
- **10_async_operations.py** - Async/parallel processing for performance

## Key Learning Concepts

### 1. Basic Patterns
- Bedrock client initialization
- Model configuration and parameters
- Simple invoke vs streaming
- Error handling best practices

### 2. Prompt Engineering
- Template composition
- System vs human messages
- Few-shot learning
- Structured output parsing

### 3. Memory & State
- Conversation history management
- Session-based memory
- Message placeholders

### 4. Advanced Chains
- Sequential processing
- Parallel execution
- Chain composition
- Error propagation

### 5. Production Features
- Safety guardrails
- Performance monitoring
- Token usage tracking
- Rate limiting

### 6. RAG Implementation
- Vector embeddings
- Document retrieval
- Context injection
- Source attribution

## Running Examples

Each file is self-contained and can be run independently:

```bash
# Basic examples
python 01_langchain_bedrock_basic.py
python 02_langchain_prompts_chains.py

# Interactive examples
python 04_interactive_cli_chatbot.py
python 04b_streaming_chatbot.py

# Advanced examples
python 09_rag_knowledge_base.py
python 10_async_operations.py
```

## Testing

Run comprehensive tests for all examples:

```bash
python test_all_examples.py
```

Tests include:
- Import validation
- Mock response handling
- Error scenario testing
- Configuration validation

## Best Practices Demonstrated

- ✅ Consistent error handling
- ✅ Modular code organization
- ✅ Configuration externalization
- ✅ Performance monitoring
- ✅ Safety considerations
- ✅ Async/parallel patterns
- ✅ Comprehensive testing

## Common Issues & Solutions

### Model Access Errors
- Verify model access in Bedrock console
- Check IAM permissions for Bedrock
- Ensure correct model IDs

### Rate Limiting
- Implement exponential backoff
- Use async processing for batches
- Monitor token usage

### Memory Issues
- Clear conversation history periodically
- Implement session timeouts
- Use appropriate storage backends

## Next Steps

After completing these examples, consider:
- Building custom tools and agents
- Integrating with AWS services (S3, DynamoDB)
- Implementing production monitoring
- Adding custom guardrails
- Exploring multi-modal capabilities
