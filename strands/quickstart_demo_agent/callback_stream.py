from strands import Agent
from strands_tools import calculator

def streaming_handler(**kwargs):
    if "data" in kwargs:
        print(kwargs["data"], end="", flush=True)
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        print(f"\n[Tool use: {kwargs['current_tool_use']['name']}]")

# Agent with callback handler
agent = Agent(
    tools=[calculator],
    callback_handler=streaming_handler
)

# Simple synchronous call - handler processes events automatically
response = agent("What is 25 * 48 and explain the calculation")
