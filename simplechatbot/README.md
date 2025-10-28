# Educational Chatbot

An educational demonstration of how conversation state is managed when working with Large Language Models (LLMs). This project teaches students that LLMs are stateless reasoning engines and all conversation memory is managed by the application.

## Learning Objectives

1. **LLMs have no memory** - All conversation history is managed by the application
2. **JSON data transfer** - See how data moves between systems
3. **State management** - Understand how applications maintain conversation history
4. **API integration** - Learn real-world service interaction patterns

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- AWS credentials configured for Bedrock access
- Access to Amazon Nova Lite model

### Quick Setup
1. Run the setup script:
   ```bash
   ./setup.sh
   ```

### Manual Setup
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Chatbot

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run the educational demo:
   ```bash
   python chatbot.py
   ```

3. Run the interactive chatbot:
   ```bash
   python chatbot.py interactive
   ```

4. Run the LLM statelessness demonstration:
   ```bash
   python chatbot.py stateless
   ```

## Educational Features

- **Visible JSON structures** - See conversation objects grow in real-time
- **Step-by-step logging** - Understand each operation
- **Debugger-friendly code** - Perfect for line-by-line debugging
- **Simple functions only** - No complex classes or advanced Python features

## Key Concepts Demonstrated

### 1. LLM Statelessness
The chatbot clearly shows that:
- Conversations start empty (no prior memory)
- Each API call must include full conversation history
- The LLM has no knowledge of previous sessions

### 2. Application State Management
Students will see how:
- Python dictionaries store conversation data
- Messages are added to conversation history
- State changes are visible through JSON output

### 3. JSON Data Transfer
The code demonstrates:
- Converting Python objects to JSON for API calls
- Parsing JSON responses back to Python objects
- Using JSON as a communication format between systems

## Project Structure

```
educational-chatbot/
├── chatbot.py          # Main chatbot implementation
├── requirements.txt    # Python dependencies
├── setup.sh           # Setup script
├── README.md          # This file
└── venv/              # Virtual environment (created by setup)
```

## AWS Configuration

Make sure you have AWS credentials configured. You can do this by:

1. Using AWS CLI:
   ```bash
   aws configure
   ```

2. Or setting environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=us-east-1
   ```

## Debugging Tips

1. Use your IDE's debugger to step through the code line by line
2. Set breakpoints at key functions to inspect variables
3. Watch how the `conversation` dictionary grows with each message
4. Observe JSON transformations during API calls

## Educational Notes

This project is designed for **beginner programmers**. The code intentionally:
- Uses only simple functions (no classes)
- Includes extensive print statements for visibility
- Uses basic Python data structures (dictionaries and lists)
- Avoids advanced Python features

The goal is to make the concepts clear and accessible to students just starting their programming journey.