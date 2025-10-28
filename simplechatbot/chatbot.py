"""
Educational Chatbot - Demonstrating LLM State Management

This chatbot teaches students how conversation state is managed by the application,
not the LLM itself. It shows how JSON is used for data transfer and how LLMs
are stateless reasoning engines.

Learning Objectives:
1. LLMs have no memory - all conversation history is managed by the application
2. JSON is used to transfer data between systems
3. Applications maintain conversation state through data structures
4. Debugging shows how conversation objects grow over time
"""

# Basic imports - only essential libraries for beginner programmers
import boto3
import json
import datetime
import uuid


def create_new_conversation():
    """
    Creates a new, empty conversation dictionary.
    
    This function demonstrates that conversations start empty - the LLM has no
    prior knowledge or memory. All conversation history must be maintained
    by the application.
    
    Returns:
        dict: Empty conversation dictionary with basic structure
    """
    print("\n=== CREATING NEW CONVERSATION ===")
    print("Starting with empty conversation - LLM has no memory!")
    
    # Create unique conversation ID
    conversation_id = str(uuid.uuid4())
    current_time = datetime.datetime.now().isoformat()
    
    # Build the conversation dictionary structure
    new_conversation = {
        "conversation_id": conversation_id,
        "created_at": current_time,
        "messages": [],  # Empty list - no messages yet!
        "metadata": {
            "model": "amazon.nova-lite-v1:0",
            "total_messages": 0
        }
    }
    
    print("New conversation created:")
    print(json.dumps(new_conversation, indent=2))
    print("Notice: messages list is empty - this proves LLM starts with no memory!")
    print("=" * 50)
    
    return new_conversation


def add_message_to_conversation(conversation, role, message):
    """
    Adds a new message to the conversation dictionary.
    
    This function shows how the application manages conversation state by
    adding each message to the conversation history. Students can see
    how the conversation object grows with each interaction.
    
    Args:
        conversation (dict): The conversation dictionary to update
        role (str): Either "user" or "assistant" 
        message (str): The message content to add
        
    Returns:
        dict: Updated conversation dictionary with new message
    """
    print(f"\n=== ADDING {role.upper()} MESSAGE ===")
    print("BEFORE adding message:")
    print(f"Total messages: {len(conversation['messages'])}")
    
    # Show the conversation state before adding the message
    if conversation['messages']:
        print("Current conversation:")
        print(json.dumps(conversation, indent=2))
    else:
        print("Conversation is still empty")
    
    # Create the new message with timestamp
    current_time = datetime.datetime.now().isoformat()
    new_message = {
        "role": role,
        "content": message,
        "timestamp": current_time
    }
    
    # Add the message to the conversation
    conversation['messages'].append(new_message)
    conversation['metadata']['total_messages'] = len(conversation['messages'])
    
    print(f"\nAFTER adding {role} message:")
    print(f"Total messages: {len(conversation['messages'])}")
    print("Updated conversation:")
    print(json.dumps(conversation, indent=2))
    print(f"Notice: The conversation object now contains {len(conversation['messages'])} message(s)")
    print("This shows how the APPLICATION maintains conversation history!")
    print("=" * 50)
    
    return conversation


def print_conversation_state(conversation):
    """
    Pretty-prints the conversation dictionary in JSON format for educational visibility.
    
    This function helps students see the exact structure of the conversation object
    and understand how it's organized as a Python dictionary that can be converted to JSON.
    
    Args:
        conversation (dict): The conversation dictionary to display
    """
    print("\n=== CONVERSATION STATE ===")
    print("Current conversation as JSON:")
    print(json.dumps(conversation, indent=2))
    print(f"Total messages in conversation: {len(conversation['messages'])}")
    print(f"Conversation ID: {conversation['conversation_id']}")
    print(f"Created at: {conversation['created_at']}")
    print("=" * 30)


def conversation_to_json(conversation):
    """
    Converts the conversation dictionary to a formatted JSON string.
    
    This function demonstrates JSON serialization - converting a Python dictionary
    into a JSON string that can be sent over networks or saved to files.
    
    Args:
        conversation (dict): The conversation dictionary to convert
        
    Returns:
        str: Formatted JSON string representation of the conversation
    """
    print("\n=== JSON SERIALIZATION DEMO ===")
    print("Converting Python dictionary to JSON string...")
    
    # Convert dictionary to JSON string
    json_string = json.dumps(conversation, indent=2)
    
    print("Python dict → JSON string conversion complete!")
    print("JSON string length:", len(json_string), "characters")
    print("This JSON can now be:")
    print("- Sent to APIs (like Bedrock)")
    print("- Saved to files")
    print("- Transmitted over networks")
    print("- Parsed by other systems")
    print("=" * 35)
    
    return json_string


def json_to_conversation(json_string):
    """
    Converts a JSON string back to a conversation dictionary.
    
    This function demonstrates JSON deserialization - converting a JSON string
    back into a Python dictionary that our application can work with.
    
    Args:
        json_string (str): JSON string to convert back to dictionary
        
    Returns:
        dict: Conversation dictionary parsed from JSON
    """
    print("\n=== JSON DESERIALIZATION DEMO ===")
    print("Converting JSON string back to Python dictionary...")
    
    # Parse JSON string back to dictionary
    conversation_dict = json.loads(json_string)
    
    print("JSON string → Python dict conversion complete!")
    print("This shows how we can:")
    print("- Receive JSON responses from APIs")
    print("- Load conversation data from files")
    print("- Parse data from other systems")
    print("- Convert back to Python objects we can use")
    print("=" * 40)
    
    return conversation_dict


def print_state_change(before_conversation, after_conversation):
    """
    Shows the before and after states of a conversation to highlight changes.
    
    This function helps students understand how the conversation object evolves
    by showing exactly what changed between two states.
    
    Args:
        before_conversation (dict): Conversation state before the change
        after_conversation (dict): Conversation state after the change
    """
    print("\n=== CONVERSATION STATE CHANGE ===")
    
    before_count = len(before_conversation['messages'])
    after_count = len(after_conversation['messages'])
    
    print(f"BEFORE: {before_count} messages")
    if before_count > 0:
        print("Last message before:")
        print(json.dumps(before_conversation['messages'][-1], indent=2))
    else:
        print("No messages yet")
    
    print(f"\nAFTER: {after_count} messages")
    if after_count > 0:
        print("Last message after:")
        print(json.dumps(after_conversation['messages'][-1], indent=2))
    
    print(f"\nCHANGE: Added {after_count - before_count} new message(s)")
    print("This shows how the APPLICATION manages conversation growth!")
    print("=" * 40)


def debug_conversation_state(conversation, step_name):
    """
    Educational helper function for step-by-step debugging visibility.
    
    This function provides detailed information about the conversation state
    at any point in the program, perfect for debugging sessions with students.
    
    Args:
        conversation (dict): The conversation dictionary to inspect
        step_name (str): Description of the current step for context
    """
    print(f"\n=== DEBUG: {step_name.upper()} ===")
    print(f"Step: {step_name}")
    print(f"Conversation ID: {conversation['conversation_id']}")
    print(f"Total messages: {len(conversation['messages'])}")
    print(f"Model being used: {conversation['metadata']['model']}")
    
    if conversation['messages']:
        print("Message history:")
        for i, message in enumerate(conversation['messages']):
            print(f"  {i+1}. [{message['role']}]: {message['content'][:50]}...")
    else:
        print("No messages yet - conversation is empty")
    
    print("\nFull conversation structure:")
    print(json.dumps(conversation, indent=2))
    print("=" * 50)
    
    # Pause for debugging (students can set breakpoints here)
    # This is where students would inspect variables in their debugger


def create_bedrock_client():
    """
    Creates a simple boto3 Bedrock runtime client for Nova Lite.
    
    This function shows students how to set up AWS API clients. The client
    is just a tool for making HTTP requests to AWS services and has no
    memory or conversation state.
    
    Returns:
        boto3.client: Bedrock runtime client
    """
    print("\n=== CREATING BEDROCK CLIENT ===")
    print("Setting up AWS Bedrock client for Nova Lite model...")
    
    # Create the Bedrock runtime client (assumes AWS credentials are configured)
    client = boto3.client('bedrock-runtime')
    
    print("✓ Bedrock client created!")
    print("- Service: bedrock-runtime")
    print("- Target model: amazon.nova-lite-v1:0")
    print("\nIMPORTANT: This client has NO memory of previous conversations!")
    print("Each API call must include the full conversation history.")
    print("=" * 40)
    
    return client


def prepare_bedrock_request(conversation):
    """
    Converts our conversation dictionary to Nova Lite API request format.
    
    This function shows students how to transform application data into the
    specific JSON format required by the Nova Lite API. It demonstrates
    that we must send the ENTIRE conversation history with each request.
    
    Args:
        conversation (dict): Our conversation dictionary
        
    Returns:
        dict: Request dictionary formatted for Nova Lite API
    """
    print("\n=== PREPARING BEDROCK API REQUEST ===")
    print("Converting conversation to Nova Lite API format...")
    
    # Start with empty messages list for the API
    api_messages = []
    
    # Convert each message in our conversation to Nova Lite format
    for message in conversation['messages']:
        api_message = {
            "role": message['role'],
            "content": [{"text": message['content']}]  # Nova Lite requires content in this format
        }
        api_messages.append(api_message)
    
    # Build the complete API request
    bedrock_request = {
        "messages": api_messages,
        "inferenceConfig": {
            "maxTokens": 1000,
            "temperature": 0.7,
            "topP": 0.9
        }
    }
    
    print(f"✓ Converted {len(conversation['messages'])} messages to API format")
    print("IMPORTANT: Notice we're sending ALL previous messages!")
    print("This proves the LLM gets the full conversation history each time.")
    print("=" * 45)
    
    return bedrock_request


def print_api_request(request_data):
    """
    Displays the outgoing API request in a clear, educational format.
    
    This function helps students see exactly what JSON data is being sent
    to the Nova Lite API, making the communication transparent.
    
    Args:
        request_data (dict): The API request dictionary to display
    """
    print("\n=== OUTGOING API REQUEST ===")
    print("This is the JSON we're sending to Nova Lite:")
    print(json.dumps(request_data, indent=2))
    
    message_count = len(request_data['messages'])
    print(f"\nRequest contains {message_count} message(s)")
    
    if message_count > 0:
        print("Message summary:")
        for i, msg in enumerate(request_data['messages']):
            role = msg['role']
            content = msg['content'][0]['text'][:50] + "..." if len(msg['content'][0]['text']) > 50 else msg['content'][0]['text']
            print(f"  {i+1}. [{role}]: {content}")
    
    print("\nThis shows that the LLM receives ALL conversation history!")
    print("The LLM has no memory - we must provide everything each time.")
    print("=" * 35)


def send_to_bedrock(client, request_data):
    """
    Sends the API request to Nova Lite and returns the response.
    
    This function makes the actual API call to Amazon Bedrock's Nova Lite model.
    It shows students how HTTP requests work with cloud services and demonstrates
    that the LLM processes our request and returns a response.
    
    Args:
        client: The boto3 Bedrock client
        request_data (dict): The API request dictionary
        
    Returns:
        dict: The response from Nova Lite
    """
    print("\n=== SENDING REQUEST TO NOVA LITE ===")
    print("Making API call to amazon.nova-lite-v1:0...")
    
    # Convert request dictionary to JSON string for the API
    request_json = json.dumps(request_data)
    print(f"Request size: {len(request_json)} characters")
    
    # Make the API call to Nova Lite
    response = client.invoke_model(
        modelId="us.amazon.nova-lite-v1:0",
        body=request_json
    )
    
    # Parse the response
    response_body = json.loads(response['body'].read())
    
    print("✓ Received response from Nova Lite!")
    print("The LLM processed our request and generated a response.")
    print("IMPORTANT: The LLM had no memory - it only saw what we sent!")
    print("=" * 40)
    
    return response_body


def extract_response_content(bedrock_response):
    """
    Extracts the message text from Nova Lite's response format.
    
    This function shows students how to parse API responses and extract
    the actual message content from the nested JSON structure.
    
    Args:
        bedrock_response (dict): The response from Nova Lite
        
    Returns:
        str: The assistant's message text
    """
    print("\n=== EXTRACTING RESPONSE CONTENT ===")
    print("Parsing Nova Lite response to get the message...")
    
    # Navigate the Nova Lite response structure
    message = bedrock_response['output']['message']
    content_list = message['content']
    message_text = content_list[0]['text']
    
    print("✓ Successfully extracted message from response!")
    print(f"Response length: {len(message_text)} characters")
    print("This shows how we parse JSON responses from APIs.")
    print("=" * 40)
    
    return message_text


def print_api_response(response):
    """
    Displays the incoming API response in a clear, educational format.
    
    This function helps students see the raw JSON response from Nova Lite
    and understand the structure of API responses.
    
    Args:
        response (dict): The API response dictionary to display
    """
    print("\n=== INCOMING API RESPONSE ===")
    print("This is the JSON response from Nova Lite:")
    print(json.dumps(response, indent=2))
    
    # Show key information from the response
    if 'output' in response and 'message' in response['output']:
        message_text = response['output']['message']['content'][0]['text']
        print(f"\nAssistant's response: {message_text}")
    
    if 'usage' in response:
        usage = response['usage']
        print(f"\nToken usage:")
        print(f"- Input tokens: {usage.get('inputTokens', 'N/A')}")
        print(f"- Output tokens: {usage.get('outputTokens', 'N/A')}")
        print(f"- Total tokens: {usage.get('totalTokens', 'N/A')}")
    
    print("\nThis response contains ONLY the current reply!")
    print("The LLM doesn't store or remember this conversation.")
    print("=" * 35)


def process_conversation_turn(conversation, user_input, bedrock_client):
    """
    Orchestrates a complete conversation turn with the LLM.
    
    This function demonstrates the full cycle of LLM interaction:
    1. Show current conversation state
    2. Add user message to conversation
    3. Prepare API request with full history
    4. Send request to Nova Lite
    5. Process response and add to conversation
    6. Show updated conversation state
    
    Args:
        conversation (dict): Current conversation dictionary
        user_input (str): The user's message
        bedrock_client: The boto3 Bedrock client
        
    Returns:
        dict: Updated conversation dictionary with new exchange
    """
    print("\n" + "="*60)
    print("PROCESSING COMPLETE CONVERSATION TURN")
    print("="*60)
    
    # Step 1: Show conversation state BEFORE user input
    print("\n=== STEP 1: CONVERSATION STATE BEFORE USER INPUT ===")
    print_conversation_state(conversation)
    
    # Step 2: Add user message to conversation
    print("\n=== STEP 2: ADDING USER MESSAGE ===")
    conversation = add_message_to_conversation(conversation, "user", user_input)
    
    # Step 3: Prepare API request (includes ALL conversation history)
    print("\n=== STEP 3: PREPARING API REQUEST ===")
    api_request = prepare_bedrock_request(conversation)
    print_api_request(api_request)
    
    # Step 4: Send request to Nova Lite
    print("\n=== STEP 4: SENDING TO NOVA LITE ===")
    bedrock_response = send_to_bedrock(bedrock_client, api_request)
    
    # Step 5: Process response
    print("\n=== STEP 5: PROCESSING RESPONSE ===")
    print_api_response(bedrock_response)
    assistant_message = extract_response_content(bedrock_response)
    
    # Step 6: Add assistant response to conversation
    print("\n=== STEP 6: ADDING ASSISTANT RESPONSE ===")
    conversation = add_message_to_conversation(conversation, "assistant", assistant_message)
    
    # Step 7: Show final conversation state
    print("\n=== STEP 7: FINAL CONVERSATION STATE ===")
    print_conversation_state(conversation)
    
    print("\n=== CONVERSATION TURN COMPLETE ===")
    print("Key observations:")
    print("1. We sent the ENTIRE conversation history to the LLM")
    print("2. The LLM had no memory of previous exchanges")
    print("3. Our application maintained all conversation state")
    print("4. The conversation object grew with the new exchange")
    print("=" * 50)
    
    return conversation


def main():
    """
    Main chatbot loop that provides an interactive conversation experience.
    
    This function creates a continuous conversation loop where students can
    interact with Nova Lite while seeing all the educational features:
    - Conversation state management
    - JSON data transformations
    - API communication transparency
    - LLM statelessness demonstration
    """
    print("="*70)
    print("EDUCATIONAL CHATBOT - INTERACTIVE MODE")
    print("="*70)
    print("This chatbot demonstrates how conversation state is managed!")
    print("\nKey Learning Points:")
    print("• LLMs have NO memory - each request includes full conversation history")
    print("• Applications manage ALL conversation state")
    print("• JSON is used for data transfer between systems")
    print("• You can see all data transformations in real-time")
    print("\nInstructions:")
    print("• Type your messages and press Enter")
    print("• Type 'quit' or 'exit' to end the conversation")
    print("• Watch how the conversation object grows with each exchange")
    print("• Use a debugger to step through the code line by line")
    print("="*70)
    
    # Initialize the chatbot
    print("\n=== INITIALIZING CHATBOT ===")
    conversation = create_new_conversation()
    bedrock_client = create_bedrock_client()
    
    print("\n✓ Chatbot ready! Starting conversation loop...")
    print("✓ Remember: The LLM starts with NO knowledge of previous conversations!")
    
    # Main conversation loop
    while True:
        print("\n" + "-"*50)
        
        # Get user input
        try:
            user_input = input("\nYou: ").strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thanks for learning about LLM state management!")
            break
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print("\nEnding conversation...")
            break
        
        # Skip empty inputs
        if not user_input:
            print("Please enter a message or 'quit' to exit.")
            continue
        
        # Process the conversation turn
        try:
            conversation = process_conversation_turn(conversation, user_input, bedrock_client)
            
            # Show conversation summary after each turn
            print(f"\n=== CONVERSATION SUMMARY ===")
            print(f"Total exchanges: {len(conversation['messages']) // 2}")
            print(f"Total messages: {len(conversation['messages'])}")
            print("Latest exchange:")
            if len(conversation['messages']) >= 2:
                user_msg = conversation['messages'][-2]
                assistant_msg = conversation['messages'][-1]
                print(f"  You: {user_msg['content'][:60]}...")
                print(f"  Assistant: {assistant_msg['content'][:60]}...")
            
        except Exception as error:
            print(f"\n❌ Error during conversation turn: {error}")
            print("This might be an AWS configuration issue.")
            print("Make sure your AWS credentials are set up correctly.")
            break
    
    # Show final conversation state
    print("\n" + "="*70)
    print("FINAL CONVERSATION SUMMARY")
    print("="*70)
    print_conversation_state(conversation)
    
    print("\n=== EDUCATIONAL SUMMARY ===")
    print("What you experienced:")
    print("1. The conversation started completely empty")
    print("2. Each message was added to the conversation object")
    print("3. Every API call included the full conversation history")
    print("4. The LLM had no memory between requests")
    print("5. All conversation state was managed by this application")
    print("6. JSON was used to transfer data to/from the LLM")
    
    if len(conversation['messages']) > 0:
        print(f"\nYour conversation grew to {len(conversation['messages'])} messages!")
        print("All of this state was maintained by the APPLICATION, not the LLM.")
    
    print("\nThanks for learning about LLM state management! 🤖")


def demonstrate_llm_statelessness():
    """
    Demonstrates that LLMs have no memory by showing how conversation
    history must be included in every API call.
    
    This function provides clear examples and educational commentary
    to help students understand LLM statelessness.
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: LLM STATELESSNESS")
    print("="*70)
    print("This demonstration proves that LLMs have NO memory!")
    print("\nKey Concept: Each API call is completely independent.")
    print("The LLM has no knowledge of previous conversations.")
    print("="*70)
    
    # Create a simple conversation to demonstrate with
    conversation = create_new_conversation()
    bedrock_client = create_bedrock_client()
    
    print("\n=== EXAMPLE 1: FIRST API CALL ===")
    print("Let's start with a simple question...")
    
    # Add first message
    conversation = add_message_to_conversation(conversation, "user", "My name is Alice. What's your name?")
    
    # Show what we're sending to the LLM
    api_request = prepare_bedrock_request(conversation)
    print("\nWhat we're sending to Nova Lite:")
    print("- Number of messages in request:", len(api_request['messages']))
    print("- Message 1:", api_request['messages'][0]['content'][0]['text'])
    print("\nIMPORTANT: This is the LLM's first time seeing ANY message!")
    
    # Make the API call
    response = send_to_bedrock(bedrock_client, api_request)
    assistant_message = extract_response_content(response)
    conversation = add_message_to_conversation(conversation, "assistant", assistant_message)
    
    print("\n=== EXAMPLE 2: SECOND API CALL ===")
    print("Now let's ask a follow-up question...")
    
    # Add second message
    conversation = add_message_to_conversation(conversation, "user", "Do you remember my name?")
    
    # Show what we're sending now
    api_request = prepare_bedrock_request(conversation)
    print("\nWhat we're sending to Nova Lite:")
    print("- Number of messages in request:", len(api_request['messages']))
    print("- Message 1:", api_request['messages'][0]['content'][0]['text'])
    print("- Message 2:", api_request['messages'][1]['content'][0]['text'])
    print("- Message 3:", api_request['messages'][2]['content'][0]['text'])
    
    print("\nCRITICAL OBSERVATION:")
    print("We had to send ALL 3 previous messages!")
    print("If we only sent the new question, the LLM wouldn't know about Alice!")
    
    # Make the second API call
    response = send_to_bedrock(bedrock_client, api_request)
    assistant_message = extract_response_content(response)
    conversation = add_message_to_conversation(conversation, "assistant", assistant_message)
    
    print("\n=== EXAMPLE 3: WHAT IF WE DON'T SEND HISTORY? ===")
    print("Let's see what happens if we only send the latest message...")
    
    # Create a request with ONLY the latest message (simulating no memory)
    no_history_request = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": "Do you remember my name?"}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 1000,
            "temperature": 0.7,
            "topP": 0.9
        }
    }
    
    print("\nRequest with NO conversation history:")
    print("- Number of messages:", len(no_history_request['messages']))
    print("- Only message:", no_history_request['messages'][0]['content'][0]['text'])
    
    print("\nSending request without history...")
    response = send_to_bedrock(bedrock_client, no_history_request)
    no_history_message = extract_response_content(response)
    
    print(f"\nLLM Response WITHOUT history: {no_history_message}")
    print(f"LLM Response WITH history: {assistant_message}")
    
    print("\n=== PROOF OF STATELESSNESS ===")
    print("Compare the two responses above!")
    print("• WITH history: LLM knows about Alice")
    print("• WITHOUT history: LLM has no idea who Alice is")
    print("\nThis PROVES that:")
    print("1. LLMs have NO memory between API calls")
    print("2. Applications MUST send full conversation history")
    print("3. Each API call is completely independent")
    print("4. Conversation continuity is an APPLICATION responsibility")
    
    print("\n=== MEMORY RESET DEMONSTRATION ===")
    print("What happens when we restart the application?")
    print("\nIf you restart this program:")
    print("• The conversation object will be empty again")
    print("• The LLM will have no knowledge of previous sessions")
    print("• All conversation history is lost unless saved by the application")
    print("• This proves memory is managed by the APPLICATION, not the LLM")
    
    print("\n" + "="*70)
    print("CONCLUSION: LLMs ARE STATELESS REASONING ENGINES")
    print("="*70)
    print("✓ LLMs process input and generate output")
    print("✓ LLMs have NO memory of previous interactions")
    print("✓ Applications manage ALL conversation state")
    print("✓ Full conversation history must be sent with each request")
    print("✓ Conversation continuity is an application feature, not an LLM feature")
    print("\nThis is why your chatbot application is so important!")
    print("It provides the memory that the LLM doesn't have! 🧠")


# Test the basic functions when this file is run directly
if __name__ == "__main__":
    import sys
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "interactive":
            # Run the interactive chatbot
            main()
        elif sys.argv[1] == "stateless":
            # Run the statelessness demonstration
            demonstrate_llm_statelessness()
        else:
            print("Usage:")
            print("  python chatbot.py           # Run educational demo")
            print("  python chatbot.py interactive  # Run interactive chatbot")
            print("  python chatbot.py stateless    # Run statelessness demo")
    else:
        # Run the educational demo
        print("Educational Chatbot - Complete Demo")
        print("=" * 60)
        print("Running educational demonstration...")
        print("To run interactive chatbot, use: python chatbot.py interactive")
        print("=" * 60)
    
    # Demonstrate creating a new conversation
    conversation = create_new_conversation()
    
    # Create Bedrock client early so it's available for API calls
    bedrock_client = create_bedrock_client()
    
    # Show initial state using new display functions
    print_conversation_state(conversation)
    debug_conversation_state(conversation, "Initial empty conversation")
    
    # Demonstrate JSON serialization
    json_string = conversation_to_json(conversation)
    
    # Demonstrate adding messages with state change visibility
    print("\n" + "="*60)
    print("DEMONSTRATING CONVERSATION GROWTH")
    print("="*60)
    
    # Save state before first message
    before_state = conversation.copy()
    before_state['messages'] = conversation['messages'].copy()
    
    # Add first message
    conversation = add_message_to_conversation(conversation, "user", "Hello, chatbot!")
    
    # Show the state change
    print_state_change(before_state, conversation)
    debug_conversation_state(conversation, "After first user message")
    
    # Save state before second message
    before_state = conversation.copy()
    before_state['messages'] = conversation['messages'].copy()
    
    # Make real API call to get assistant response
    api_request = prepare_bedrock_request(conversation)
    print_api_request(api_request)
    
    bedrock_response = send_to_bedrock(bedrock_client, api_request)
    print_api_response(bedrock_response)
    assistant_message = extract_response_content(bedrock_response)
    
    conversation = add_message_to_conversation(conversation, "assistant", assistant_message)
    
    # Show the state change
    print_state_change(before_state, conversation)
    debug_conversation_state(conversation, "After assistant response")
    
    # Add one more exchange to show continued growth
    before_state = conversation.copy()
    before_state['messages'] = conversation['messages'].copy()
    
    conversation = add_message_to_conversation(conversation, "user", "Can you explain how you remember our conversation?")
    print_state_change(before_state, conversation)
    
    # Final demonstration of JSON conversion
    print("\n" + "="*60)
    print("JSON ROUND-TRIP DEMONSTRATION")
    print("="*60)
    
    # Serialize to JSON
    final_json = conversation_to_json(conversation)
    
    # Deserialize back from JSON
    restored_conversation = json_to_conversation(final_json)
    
    # Show that we got the same data back
    print("\n=== VERIFYING JSON ROUND-TRIP ===")
    print("Original conversation messages:", len(conversation['messages']))
    print("Restored conversation messages:", len(restored_conversation['messages']))
    print("Data integrity check:", "PASSED" if conversation == restored_conversation else "FAILED")
    print("This proves JSON preserves all our conversation data!")
    
    print_conversation_state(conversation)
    
    print("\n=== KEY LEARNING POINTS ===")
    print("1. The conversation started empty (LLM has no memory)")
    print("2. Each message was added by the APPLICATION")
    print("3. We can see the conversation grow step-by-step")
    print("4. Python dictionaries convert easily to JSON")
    print("5. JSON is the format used to communicate with APIs")
    print("6. The LLM will receive this ENTIRE history on each API call")
    print("7. All conversation memory is managed by OUR application!")
    
    print(f"\nFinal conversation contains {len(conversation['messages'])} messages")
    
    # Demonstrate Bedrock client setup
    print("\n" + "="*60)
    print("BEDROCK CLIENT SETUP DEMONSTRATION")
    print("="*60)
    
    # Client already created above - show it's ready
    print("✓ Bedrock client already created and ready for use!")
    
    # Demonstrate API request preparation
    print("\n" + "="*60)
    print("API REQUEST PREPARATION DEMONSTRATION")
    print("="*60)
    
    # Prepare API request from our conversation
    api_request = prepare_bedrock_request(conversation)
    
    # Show the API request format
    print_api_request(api_request)
    
    # Demonstrate how the request grows with conversation
    print("\n=== DEMONSTRATING REQUEST GROWTH ===")
    print("Let's see what happens when we add more messages...")
    
    # Make another real API call to show how the request grows
    larger_api_request = prepare_bedrock_request(conversation)
    print_api_request(larger_api_request)
    
    # Demonstrate real API communication with Nova Lite
    print("\n" + "="*60)
    print("REAL API COMMUNICATION WITH NOVA LITE")
    print("="*60)
    
    # Make actual API call to Nova Lite
    bedrock_response = send_to_bedrock(bedrock_client, larger_api_request)
    
    # Show the raw API response
    print_api_response(bedrock_response)
    
    # Extract the assistant's message
    assistant_message = extract_response_content(bedrock_response)
    
    # Add the assistant's response to our conversation
    conversation = add_message_to_conversation(conversation, "assistant", assistant_message)
    
    print("\n=== DEMONSTRATING COMPLETE CONVERSATION TURN ===")
    print("Now let's see a complete conversation turn in action...")
    
    # Demonstrate a complete conversation turn
    conversation = process_conversation_turn(
        conversation, 
        "What happens when I restart this program?", 
        bedrock_client
    )
    
    print("\n=== READY FOR FULL CHATBOT ===")
    print("✓ Conversation state management: READY")
    print("✓ JSON serialization/deserialization: READY") 
    print("✓ Bedrock client: READY")
    print("✓ API request preparation: READY")
    print("✓ API communication: READY")
    print("✓ Response processing: READY")
    print("\nNext step: Create the main chatbot loop!")
    
    print("\n=== EDUCATIONAL SUMMARY ===")
    print("What we've learned:")
    print("1. LLMs have no memory - conversations start empty")
    print("2. Applications manage all conversation state")
    print("3. JSON is used for data transfer between systems")
    print("4. AWS clients are just tools for making API calls")
    print("5. Each API call must include full conversation history")
    print("6. API requests grow larger as conversations get longer")
    print("7. We transform our data format to match API requirements")
    print("8. API responses contain only the current reply")
    print("9. We parse responses and add them to our conversation state")
    print("10. The conversation object grows with each exchange")
    
    print("\n" + "="*60)
    print("DEMO COMPLETE - TRY INTERACTIVE MODE!")
    print("="*60)
    print("You've seen all the core concepts in action!")
    print("\nNext steps:")
    print("  python chatbot.py interactive  # Interactive chatbot")
    print("  python chatbot.py stateless    # LLM statelessness demo")
    print("\nInteractive mode: Have real conversations with Nova Lite")
    print("Stateless demo: See proof that LLMs have no memory")
    print("\nBoth modes show conversation state management in action!")
    print("Use a debugger to step through the code line by line.")
    print("\nHappy learning! 🚀")