import json
from strands import Agent
from strands.models import BedrockModel

# Create a Bedrock model with guardrail configuration
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    guardrail_id="jdsfcyfinj12",         # Your Bedrock guardrail ID
    guardrail_version="1",                    # Guardrail version
    guardrail_trace="enabled",                # Enable trace info for debugging
)

# Create agent with the guardrail-protected model
agent = Agent(
    system_prompt="You are a helpful assistant.",
    model=bedrock_model,
)

# Use the protected agent for conversations
response = agent("Tell me about financial planning.")

# Handle potential guardrail interventions
if response.stop_reason == "guardrail_intervened":
    print("Content was blocked by guardrails, conversation context overwritten!")

print(f"Conversation: {json.dumps(agent.messages, indent=4)}")