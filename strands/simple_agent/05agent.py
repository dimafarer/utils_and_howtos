from mcp import StdioServerParameters, stdio_client
from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import shell
from strands.tools.mcp import MCPClient

"""
Agent with existing functionality plus access to Strands documentation search via MCP server
"""

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

# Create MCP client for strands-agents server
stdio_mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="uvx", 
        args=["awslabs.aws-documentation-mcp-server@latest"]
    )
))


# Create a Bedrock model instance
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-pro-v1:0",
    temperature=0.3,
    top_p=0.8,
)

with stdio_mcp_client:
    # Get the tools from the MCP server
    tools = stdio_mcp_client.list_tools_sync()
    print(f"TOOLS:  {tools}")
    # Create an agent with these tools
    agent = Agent(tools=tools)
    agent("tell me about bedrock agent builder")



# https://github.com/modelcontextprotocol/servers
# https://github.com/modelcontextprotocol/python-sdk
# https://modelcontextprotocol.io/docs/getting-started/intro