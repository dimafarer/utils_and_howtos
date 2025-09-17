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



# /home/wsluser/projects/strands/agentcore_agent
# /home/wsluser/projects/strands/venv/bin/agentcore invoke '{"prompt": "Your message here"}'