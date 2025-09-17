from strands import Agent
from strands.models import BedrockModel
"""
Now we are using the explisit Strand's Bedrock Model class so we can set our own parameters 
including the model we want to use
"""
# Create a Bedrock model instance
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-premier-v1:0",
    temperature=0.3,
    top_p=0.8,
)

agent = Agent(model=bedrock_model)
response = agent("What is the capital of France?")
# print(response)