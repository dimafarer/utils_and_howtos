from strands import Agent, tool #import the tool module
from strands.models import BedrockModel
from strands_tools import shell

"""
using a tool that is a function in the same script.
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



# Create a Bedrock model instance
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-pro-v1:0",
    temperature=0.3,
    top_p=0.8,
)

agent = Agent(
    system_prompt="You are a helpfull agent.",
    model=bedrock_model,
    tools=[shell, letter_counter],
)

message = """
Answers two questions

1. What Operating System am I using?
2. How manny letter a's are in "banana"
"""

response = agent(message)


# response = agent("What operating system am I using?")
# print(response)