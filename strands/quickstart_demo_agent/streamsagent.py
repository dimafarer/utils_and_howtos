import asyncio
from strands import Agent
from strands_tools import calculator

# Initialize our agent without a callback handler
agent = Agent(
    tools=[calculator],
    callback_handler=None  # Disable default callback handler
)

# Async function that iterates over streamed agent events
async def process_streaming_response():
    prompt = "What is 25 * 48 and explain the calculation"

    try:
        # Get an async iterator for the agent's response stream
        agent_stream = agent.stream_async(prompt)

        # Process events as they arrive
        async for event in agent_stream:
            if "data" in event:
                # Print text chunks as they're generated
                print(event["data"], end="", flush=True)
            elif "delta" in event:
                # Print raw delta content
                print(event["delta"], end="", flush=True)
            elif "current_tool_use" in event and event["current_tool_use"].get("name"):
                # Print tool usage information
                print(f"\n[Tool use delta for: {event['current_tool_use']['name']}]")
            elif "start" in event:
                print("\n[Agent cycle started]")
            elif "init_event_loop" in event:
                print("\n[Event loop initialized]")
            elif "start_event_loop" in event:
                print("\n[Event loop started]")
        
        print("\n")  # Clean ending newline
    
    except Exception as e:
        print(f"\nError during streaming: {e}")

# Run the agent with the async event processing
asyncio.run(process_streaming_response())
