# How to Convert Your Strands Agent to Amazon Bedrock AgentCore

This guide will walk you through converting a local Strands agent into a cloud-deployed agent running on Amazon Bedrock AgentCore Runtime. We'll use a step-by-step approach that's perfect for beginning developers.

## What is Amazon Bedrock AgentCore?

Amazon Bedrock AgentCore Runtime is a serverless platform that lets you deploy and scale AI agents in the cloud. Think of it as a hosting service specifically designed for AI agents - it handles all the infrastructure, scaling, and security so you can focus on building your agent's functionality.

**Key Benefits:**
- **Serverless**: No servers to manage
- **Scalable**: Automatically handles thousands of users
- **Secure**: Built-in security and session isolation
- **Cost-effective**: Pay only for what you use

## Prerequisites

Before we start, make sure you have:

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **Python 3.10+**: Your development environment should have Python 3.10 or higher
3. **AWS CLI configured**: Your AWS credentials should be set up
4. **Existing Strands Agent**: A working local Strands agent (we'll use `03agent.py` as our example)

## Step 1: Understanding the Original Agent

Let's first look at what we're converting. Here's our original `03agent.py`:

```python
from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import shell

# Define a custom tool
@tool
def letter_counter(word: str, letter: str) -> int:
    """Count occurrences of a specific letter in a word."""
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")
    return word.lower().count(letter.lower())

# Create model and agent
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-pro-v1:0",
    temperature=0.3,
    top_p=0.8,
)

agent = Agent(
    system_prompt="You are a helpful agent.",
    model=bedrock_model,
    tools=[shell, letter_counter],
)

# Run the agent
message = "What Operating System am I using? How many letter a's are in 'banana'?"
response = agent(message)
print(response)
```

**What this agent does:**
- Uses Amazon Bedrock's Nova Pro model
- Has access to shell commands (via `shell` tool)
- Has a custom `letter_counter` tool
- Runs locally and prints results

## Step 2: Create the Project Structure

First, let's create a new directory for our AgentCore version:

```bash
mkdir agentcore_agent
cd agentcore_agent
```

Your project should have this structure:
```
agentcore_agent/
├── agent_example.py     # Main agent code (AgentCore compatible)
├── requirements.txt     # Python dependencies
└── __init__.py         # Makes directory a Python package
```

## Step 3: Install Required Packages

Install the AgentCore packages in your virtual environment:

```bash
# Assuming you're using the same venv as your other agents
/path/to/your/venv/bin/pip install bedrock-agentcore bedrock-agentcore-starter-toolkit
```

## Step 4: Convert Your Agent Code

Now we'll convert the original agent to work with AgentCore. The key changes are:

### 4.1 Add Required Imports

```python
import os  # For environment variables
from bedrock_agentcore.runtime import BedrockAgentCoreApp  # AgentCore wrapper
```

### 4.2 Set Environment Variable for Tool Consent

Some tools (like `shell`) require user approval by default. For automated deployment, we bypass this:

```python
# Set environment variable to bypass tool consent
os.environ["BYPASS_TOOL_CONSENT"] = "true"
```

**Why this is needed:** The `shell` tool can execute system commands, which could be dangerous. In development/testing, we bypass the confirmation prompt.

### 4.3 Initialize AgentCore App

```python
# Initialize AgentCore app
app = BedrockAgentCoreApp()
```

**What this does:** Creates the web server wrapper that AgentCore needs to communicate with your agent.

### 4.4 Move Agent Initialization Inside the Entrypoint

This is the most important change. Instead of creating the agent at module level, we create it inside a function:

```python
@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    # Create model and agent INSIDE the function
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-pro-v1:0",
        temperature=0.3,
        top_p=0.8,
    )

    agent = Agent(
        system_prompt="You are a helpful agent.",
        model=bedrock_model,
        tools=[shell, letter_counter],
    )
    
    # Get user message from payload
    user_message = payload.get("prompt", "Hello! I'm a helpful agent.")
    
    # Run the agent
    result = agent(user_message)
    
    # Return result in expected format
    return {"result": str(result.message)}
```

**Why move it inside:** AgentCore calls this function for each request. Creating the agent inside ensures fresh initialization and proper resource management.

### 4.5 Complete Converted Code

Here's the full `agent_example.py`:

```python
import os
from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import shell
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Set environment variable to bypass tool consent
os.environ["BYPASS_TOOL_CONSENT"] = "true"

# Initialize AgentCore app
app = BedrockAgentCoreApp()

# Define a custom tool as a Python function using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())

@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    # Create a Bedrock model instance
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-pro-v1:0",
        temperature=0.3,
        top_p=0.8,
    )

    # Initialize agent inside the entrypoint
    agent = Agent(
        system_prompt="You are a helpful agent.",
        model=bedrock_model,
        tools=[shell, letter_counter],
    )
    
    user_message = payload.get("prompt", "Hello! I'm a helpful agent with shell access and custom tools.")
    result = agent(user_message)
    return {"result": str(result.message)}

if __name__ == "__main__":
    app.run()
```

## Step 5: Create Supporting Files

### 5.1 Create requirements.txt

```txt
strands-agents
strands-agents-tools
bedrock-agentcore
```

**What each package does:**
- `strands-agents`: Core Strands framework
- `strands-agents-tools`: Pre-built tools like `shell`
- `bedrock-agentcore`: AgentCore integration

### 5.2 Create __init__.py

```python
# AgentCore Agent Package
```

**Why needed:** Makes the directory a Python package, required by AgentCore.

## Step 6: Configure the Agent

Use the AgentCore CLI to configure your agent:

```bash
cd agentcore_agent
/path/to/your/venv/bin/agentcore configure --entrypoint agent_example.py
```

**What this does:**
- Analyzes your agent code
- Sets up AWS resources (IAM roles, ECR repository)
- Creates configuration files
- Prepares for deployment

**You'll be prompted for:**
- **Execution Role**: Press Enter to auto-create
- **ECR Repository**: Press Enter to auto-create  
- **Dependencies**: Press Enter to use `requirements.txt`
- **Authorization**: Press Enter for default IAM

## Step 7: Deploy to AWS

Deploy your agent to the cloud:

```bash
/path/to/your/venv/bin/agentcore launch
```

**What happens during deployment:**
1. **CodeBuild Setup**: Creates a cloud build environment
2. **Container Building**: Builds an ARM64 Docker container
3. **ECR Push**: Uploads container to Amazon ECR
4. **AgentCore Deployment**: Deploys to AgentCore Runtime
5. **Endpoint Creation**: Creates a callable endpoint

**Expected output:**
```
🚀 Launching Bedrock AgentCore (codebuild mode - RECOMMENDED)...
✅ CodeBuild Deployment Successful!

Agent Details:
Agent Name: agent_example
Agent ARN: arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/agent_example-ABC123
```

## Step 8: Test Your Deployed Agent

Test your agent with a sample request:

```bash
/path/to/your/venv/bin/agentcore invoke '{"prompt": "What operating system are you running on and how many letter a are in banana?"}'
```

**Expected response:**
```json
{
  "result": "The operating system you are running on is Linux. The word 'banana' contains 3 occurrences of the letter 'a'."
}
```

## Key Differences: Local vs AgentCore

| Aspect | Local Agent | AgentCore Agent |
|--------|-------------|-----------------|
| **Execution** | Runs on your machine | Runs in AWS cloud |
| **Scaling** | Single instance | Auto-scales to thousands |
| **Initialization** | At module level | Inside entrypoint function |
| **Input/Output** | Direct function calls | HTTP requests/responses |
| **Infrastructure** | Your responsibility | Managed by AWS |
| **Cost** | Your compute costs | Pay-per-use |

## Understanding the AgentCore Architecture

```
User Request → AgentCore Runtime → Your Container → Strands Agent → Response
```

1. **User sends request** to AgentCore endpoint
2. **AgentCore Runtime** receives and routes the request
3. **Your container** processes the request via the `invoke` function
4. **Strands Agent** executes with tools and model
5. **Response** flows back through the chain

## Common Issues and Solutions

### Issue 1: Agent Hangs During Local Testing
**Problem:** Running `python agent_example.py` hangs
**Solution:** This is expected! AgentCore agents are designed to run as web servers, not standalone scripts.

### Issue 2: Tool Consent Prompts
**Problem:** Agent waits for user approval for shell commands
**Solution:** Set `os.environ["BYPASS_TOOL_CONSENT"] = "true"` in your code

### Issue 3: Platform Mismatch Warning
**Problem:** Warning about linux/amd64 vs linux/arm64
**Solution:** This is normal. CodeBuild handles the ARM64 conversion automatically.

### Issue 4: Import Errors
**Problem:** Missing imports when deployed
**Solution:** Ensure all dependencies are in `requirements.txt`

## Monitoring Your Agent

### View Logs
```bash
aws logs tail /aws/bedrock-agentcore/runtimes/your-agent-name --follow
```

### Check Status
```bash
agentcore status
```

### View Metrics
- Go to AWS CloudWatch console
- Navigate to Application Signals (APM)
- Find your agent service

## Best Practices

### 1. Resource Management
- Create agents inside the entrypoint function
- Don't store state between requests
- Clean up resources properly

### 2. Error Handling
```python
@app.entrypoint
def invoke(payload):
    try:
        # Your agent code
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
```

### 3. Input Validation
```python
def invoke(payload):
    user_message = payload.get("prompt")
    if not user_message:
        return {"error": "No prompt provided"}
    # Continue with processing
```

### 4. Security
- Use IAM roles, not hardcoded credentials
- Validate all inputs
- Be cautious with shell access in production

## Next Steps

Now that you have a working AgentCore agent, you can:

1. **Add more tools** from `strands-agents-tools`
2. **Integrate MCP servers** for extended functionality
3. **Set up monitoring** with CloudWatch
4. **Create multiple agents** for different use cases
5. **Build a frontend** that calls your agent

## Conclusion

Converting a Strands agent to AgentCore involves:
1. Wrapping your agent with `BedrockAgentCoreApp`
2. Moving initialization inside the entrypoint function
3. Using the AgentCore CLI for deployment
4. Testing with the cloud-deployed version

The main benefit is transforming a local script into a scalable, production-ready service that can handle thousands of concurrent users while maintaining the same core functionality.

Your agent is now running in the cloud and ready to serve users worldwide! 🚀
