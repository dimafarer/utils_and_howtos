# Implementation Plan

- [x] 1. Set up project structure and basic conversation functions
  - Create main chatbot.py file with basic imports (boto3, json, datetime, uuid)
  - Implement create_new_conversation() function that returns empty conversation dictionary
  - Implement add_message_to_conversation() function that adds messages to conversation list
  - Add educational print statements to show conversation state changes
  - _Requirements: 1.1, 4.1, 6.1_

- [x] 2. Implement JSON visibility and educational display functions
  - Create print_conversation_state() function that pretty-prints conversation JSON
  - Implement conversation_to_json() function for formatted JSON output
  - Add print_state_change() function to show before/after conversation states
  - Include debug_conversation_state() helper for step-by-step visibility
  - _Requirements: 1.2, 2.3, 6.2, 6.4_

- [x] 3. Create simple Bedrock client setup function
  - Implement create_bedrock_client() function that returns boto3.client('bedrock-runtime')
  - Add basic educational print statements showing client creation
  - Keep it simple - assume AWS credentials are already configured
  - _Requirements: 5.1, 5.2_

- [x] 4. Implement Bedrock API request preparation functions
  - Create prepare_bedrock_request() function to format conversation for Nova Lite API
  - Convert conversation messages to Nova Lite's required format with content arrays
  - Add inferenceConfig with maxTokens, temperature, and topP parameters
  - Include print_api_request() function to show outgoing JSON payload
  - _Requirements: 2.1, 2.2, 5.3_

- [x] 5. Implement Bedrock API communication functions
  - Create send_to_bedrock() function that makes API calls to amazon.nova-lite-v1:0
  - Add comprehensive logging of request and response for educational purposes
  - Implement extract_response_content() to parse Nova Lite response format
  - Include print_api_response() function to show incoming JSON response
  - _Requirements: 2.1, 2.2, 5.1, 5.3_

- [x] 6. Create conversation processing and state management functions
  - Implement process_conversation_turn() function that orchestrates complete interaction
  - Show conversation state before user input, after user input, and after LLM response
  - Demonstrate JSON data flow through each step with educational print statements
  - Add debug pause points for step-by-step debugging sessions
  - _Requirements: 1.1, 1.3, 6.2, 6.3_

- [x] 7. Implement main chatbot loop with educational features
  - Create main() function with simple while loop for continuous conversation
  - Add clear prompts and instructions for students
  - Include conversation state display after each exchange
  - Implement graceful exit and conversation summary
  - _Requirements: 1.1, 4.2, 6.1_

- [x] 8. Create demonstration showing LLM statelessness
  - Add clear examples of how conversation history is included in each API call
  - Show that each API call must include the full conversation history
  - Include educational commentary explaining why this proves LLMs have no memory
  - _Requirements: 3.1, 3.2, 3.3, 3.4_