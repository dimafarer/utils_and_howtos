---
inclusion: always
---

# Conversation State Demonstration Requirements

## Core Educational Message
**The LLM has NO memory. All conversation history is managed by the application.**

## Required Demonstrations

### 1. Conversation Object Growth
- **Show empty conversation** at start
- **Display conversation after each message** is added
- **Highlight new additions** to the conversation structure
- **Use JSON pretty-printing** to make structure visible

### 2. API Call Transparency
- **Log outgoing requests** to show full conversation history being sent
- **Log incoming responses** to show only current response
- **Demonstrate** that each API call includes ALL previous messages
- **Show** that LLM response contains no reference to previous context

### 3. State Management Visibility
```python
# Example of required visibility
print("=== BEFORE adding user message ===")
print(json.dumps(conversation, indent=2))

# Add user message
conversation = add_message_to_conversation(conversation, "user", user_input)

print("=== AFTER adding user message ===")
print(json.dumps(conversation, indent=2))

print("=== SENDING TO BEDROCK ===")
request_data = prepare_bedrock_request(conversation)
print(json.dumps(request_data, indent=2))
```

### 4. Memory Reset Demonstration
- **Show** that restarting the program loses all conversation history
- **Demonstrate** that LLM has no knowledge of previous sessions
- **Explain** that persistence requires application-level storage

## Debugging Integration

### Strategic Breakpoints
- **Before API calls** - inspect conversation state
- **After API responses** - see how conversation grows
- **During JSON operations** - understand data transformation

### Variable Inspection Points
- **conversation dictionary** - show structure evolution
- **request_data** - demonstrate API payload construction
- **response_data** - show API response parsing

### Educational Print Statements
```python
def debug_conversation_state(conversation, step_name):
    print(f"\n=== CONVERSATION STATE: {step_name} ===")
    print(f"Total messages: {len(conversation['messages'])}")
    print(f"Last message: {conversation['messages'][-1] if conversation['messages'] else 'None'}")
    print("Full conversation:")
    print(json.dumps(conversation, indent=2))
    print("=" * 50)
```

## JSON Learning Objectives

### Data Transfer Concepts
- **Serialization**: Converting Python dict to JSON string for API
- **Deserialization**: Converting JSON response back to Python dict
- **Structure Preservation**: Show how nested data maintains relationships
- **Human Readability**: Demonstrate JSON as communication format

### Practical Examples
- **API Request**: Show conversation dict → JSON string → Bedrock
- **API Response**: Show Bedrock JSON → Python dict → conversation update
- **State Persistence**: Show conversation dict → JSON file → reload dict
- **Debug Output**: Show dict → pretty JSON → student understanding