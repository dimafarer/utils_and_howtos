# LangChain + AWS Bedrock Learning Series

A comprehensive, beginner-friendly tutorial series for learning LangChain with AWS Bedrock. Each file builds on the previous concepts with hands-on examples and detailed explanations.

## 🎯 Learning Objectives

By completing this series, you'll learn:
- How to set up and use AWS Bedrock with LangChain
- Prompt engineering and template creation
- Building conversational AI with memory
- Advanced chaining patterns for complex workflows
- Real-time streaming responses
- Production-ready features like monitoring and safety

## 📚 File Progression

### Foundation (Start Here)
**00_environment_setup_check.py** - Environment Setup & Verification
- ✅ Verify Python version and dependencies
- ✅ Test AWS credentials and Bedrock access
- ✅ Validate all prerequisites are met
- **Prerequisites:** AWS account with Bedrock access
- **Next:** 01_langchain_bedrock_basic.py

**01_langchain_bedrock_basic.py** - Your First AI Chatbot
- 🤖 Connect to AWS Bedrock service
- 🤖 Create a ChatBedrock instance
- 🤖 Send messages and get AI responses
- 🤖 Handle errors and troubleshoot issues
- **Prerequisites:** 00_environment_setup_check.py
- **Next:** 02_langchain_prompts_chains.py

### Core Concepts
**02_langchain_prompts_chains.py** - Prompt Templates & Chains
- 📝 Why templates are better than hardcoded prompts
- 📝 Create flexible prompt templates with variables
- 📝 Use LCEL (LangChain Expression Language) for chaining
- 📝 Build reusable AI workflows with output parsers
- 📝 **7 hands-on examples** from basic to advanced
- **Prerequisites:** 01_langchain_bedrock_basic.py
- **Next:** 03_conversational_memory_chatbot.py

**03_conversational_memory_chatbot.py** - Conversational Memory
- 💭 Understand stateless vs stateful conversations
- 💭 Add memory to AI conversations
- 💭 Manage conversation history and context
- 💭 Handle multiple user sessions
- 💭 **6 comprehensive examples** with real conversations
- **Prerequisites:** 02_langchain_prompts_chains.py
- **Next:** 04_streaming_chatbot.py

**04_streaming_chatbot.py** - Real-time Streaming Responses
- ⚡ Stream AI responses in real-time
- ⚡ Build interactive chat interfaces
- ⚡ Handle streaming with memory
- ⚡ Debug mode and error handling
- **Prerequisites:** 03_conversational_memory_chatbot.py
- **Next:** 05_aws_architecture_chaining.py

### Advanced Patterns
**05_aws_architecture_chaining.py** - Multi-step Architecture Planning
- 🏗️ Chain multiple AI calls for complex tasks
- 🏗️ Analyze requirements → Suggest services → Design architecture
- 🏗️ Build AI-powered AWS consulting workflows
- **Prerequisites:** 04_streaming_chatbot.py
- **Next:** 06_aws_troubleshooting_chaining.py

**06_aws_troubleshooting_chaining.py** - Error Analysis Workflows
- 🔧 Parse AWS error messages automatically
- 🔧 Chain: Root cause → Solutions → Step-by-step fixes
- 🔧 Build AI-powered troubleshooting assistants
- **Prerequisites:** 05_aws_architecture_chaining.py
- **Next:** 07_advanced_prompts.py

### Production Features
**07_advanced_prompts.py** - Structured Outputs & Advanced Templates
- 🎯 Use Pydantic models for structured AI responses
- 🎯 Advanced prompt composition techniques
- 🎯 Type-safe AI outputs for production use
- **Prerequisites:** 06_aws_troubleshooting_chaining.py
- **Next:** 08_callbacks_monitoring.py

**08_callbacks_monitoring.py** - Production Monitoring
- 📊 Track AI usage metrics and performance
- 📊 Custom callbacks for logging and monitoring
- 📊 Production-ready observability
- **Prerequisites:** 07_advanced_prompts.py
- **Next:** 09_rag_knowledge_base.py

**09_rag_knowledge_base.py** - Retrieval Augmented Generation
- 🔍 Build AI that can search and use documents
- 🔍 Vector databases and semantic search
- 🔍 Create intelligent knowledge bases
- **Prerequisites:** 08_callbacks_monitoring.py
- **Next:** 10_async_operations.py

**10_async_operations.py** - Asynchronous & Concurrent AI
- ⚡ Handle multiple AI requests simultaneously
- ⚡ Async/await patterns for better performance
- ⚡ Scale AI applications efficiently
- **Prerequisites:** 09_rag_knowledge_base.py
- **Congratulations:** You've completed the series!

## 🚀 Quick Start

1. **Setup Environment:**
   ```bash
   cd langchain
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure AWS:**
   ```bash
   aws configure
   # Enter your AWS credentials with Bedrock access
   ```

3. **Start Learning:**
   ```bash
   python 00_environment_setup_check.py
   ```

## 📋 Prerequisites

- **Python 3.8+** with pip
- **AWS Account** with Bedrock service access
- **AWS CLI** configured with credentials
- **Basic Python knowledge** (variables, functions, imports)

## 🔧 Troubleshooting

**Common Issues:**
- **"No module named 'langchain_aws'"** → Run `pip install -r requirements.txt`
- **"AccessDenied" errors** → Check AWS credentials and Bedrock permissions
- **"Model not found"** → Request model access in AWS Bedrock console
- **Import errors** → Ensure you're in the virtual environment

**Getting Help:**
1. Run `00_environment_setup_check.py` to diagnose issues
2. Check AWS Bedrock console for model access
3. Verify IAM permissions include `bedrock:InvokeModel`

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_all_examples.py
```

**Test Coverage:**
- ✅ 21 functional tests
- ✅ Real AWS integration testing
- ✅ Error handling validation
- ✅ Chain composition verification

## 📖 Learning Tips

1. **Follow the order** - Each file builds on previous concepts
2. **Run the code** - Don't just read, execute and experiment
3. **Modify examples** - Change prompts and see what happens
4. **Read comments** - Detailed explanations are in the code
5. **Check tests** - See `test_all_examples.py` for usage patterns

## 🎉 What You'll Build

By the end of this series, you'll have built:
- ✅ Basic AI chatbots with AWS Bedrock
- ✅ Conversational AI with memory and context
- ✅ Multi-step AI workflows for complex tasks
- ✅ Production-ready AI applications with monitoring
- ✅ Knowledge-based AI systems with document search
- ✅ Scalable, asynchronous AI applications

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [AWS Bedrock User Guide](https://docs.aws.amazon.com/bedrock/)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/)

---

**Ready to start?** Run `python 00_environment_setup_check.py` and begin your LangChain journey!
