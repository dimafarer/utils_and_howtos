import logging
import boto3 # type: ignore
import os
from dotenv import load_dotenv # type: ignore
# from strands import logger # type: ignore
from strands import Agent, tool # type: ignore
from strands_tools import calculator, current_time, shell # type: ignore
from strands.models import BedrockModel # type: ignore

# Load environment variables from local .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
MODEL_ID = os.getenv("MODEL_ID")
if not MODEL_ID:
    raise ValueError("MODEL_ID environment variable is required")

# # Enables Strands debug log level 
# logging.getLogger("strands").setLevel(logging.DEBUG)
# logging.getLogger("strands").setLevel(logging.INFO)
# # # Sets the logging format and streams logs to stderr
# logging.basicConfig(
#     format="%(levelname)s | %(name)s | %(message)s",
#     handlers=[logging.StreamHandler()]
# )
# # agent logger
# logger = logging.getLogger("quickstart_agent")



# # OTHER HANDLERS OPTIONS
# # Send to a file instead
# handlers=[logging.FileHandler('app.log')]

# # Send to both console and file
# handlers=[
#     logging.StreamHandler(),           # Console
#     logging.FileHandler('debug.log')   # File
# ]

# # Send to stdout instead of stderr
# handlers=[logging.StreamHandler(sys.stdout)]





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


# Create a BedrockModel
bedrock_model = BedrockModel(
    model_id=MODEL_ID,
    region_name="us-west-2",
    temperature=0.3,
)

# callback handler for agent
# Define a simple callback handler that logs instead of printing
tool_use_ids = []
def callback_handler(**kwargs):
    if "data" in kwargs:
        # Print the streamed data chunks
        print(kwargs["data"], end="")
    elif "current_tool_use" in kwargs:
        tool = kwargs["current_tool_use"]
        if tool["toolUseId"] not in tool_use_ids:
            # Print the tool use
            print(f"\n[Using tool: {tool.get('name')}]")
            tool_use_ids.append(tool["toolUseId"])

# Create an agent with tools from the community-driven strands-tools package
# as well as our custom letter_counter tool
agent = Agent(
    model=bedrock_model,
    tools=[calculator, current_time, shell, letter_counter],
    callback_handler=callback_handler
    )
print(agent.model.config) # type: ignore # get model ID


# Ask the agent a question that uses the available tools
message = """
I have 4 requests:

1. What is the time right now?
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓
4. What Operating System am I using?
"""

result = agent(message)
# print(result.metrics.get_summary())





