# Requirements Document

## Introduction

This feature is an educational chatbot built with Python, boto3, and Amazon Bedrock's Nova Lite model. The primary purpose is to demonstrate to programming learners how conversation state is managed by the application, not the LLM itself. The chatbot will serve as a hands-on example of JSON data transfer between systems and help students understand that LLMs are reasoning machines without inherent memory capabilities.

## Requirements

### Requirement 1

**User Story:** As a programming student, I want to interact with a chatbot that shows me how conversation history is built and maintained, so that I can understand how applications manage state when working with LLMs.

#### Acceptance Criteria

1. WHEN a user sends a message to the chatbot THEN the system SHALL display the current conversation object in JSON format before processing
2. WHEN the system receives a response from the LLM THEN it SHALL show how the conversation object is updated with the new exchange
3. WHEN using a debugger THEN students SHALL be able to step through line-by-line execution to see conversation state changes
4. WHEN the conversation grows THEN the JSON structure SHALL clearly show the accumulation of message history

### Requirement 2

**User Story:** As a programming instructor, I want the chatbot to demonstrate JSON data transfer between systems, so that students can see practical examples of data serialization and API communication.

#### Acceptance Criteria

1. WHEN the system communicates with Bedrock THEN it SHALL log the JSON payload being sent to the API
2. WHEN receiving responses from Bedrock THEN it SHALL display the raw JSON response structure
3. WHEN conversation data is processed THEN the system SHALL show JSON parsing and manipulation operations
4. WHEN data is stored or retrieved THEN students SHALL see JSON serialization and deserialization in action

### Requirement 3

**User Story:** As a programming learner, I want to understand that the LLM has no memory of previous conversations, so that I can grasp the concept that memory is an application-level responsibility.

#### Acceptance Criteria

1. WHEN starting a new conversation THEN the system SHALL demonstrate that the LLM receives no prior context
2. WHEN continuing a conversation THEN the system SHALL explicitly show how previous messages are included in each API call
3. WHEN the application restarts THEN students SHALL see that conversation history must be restored from application storage, not the LLM
4. IF conversation history is cleared THEN the LLM SHALL have no knowledge of previous interactions

### Requirement 4

**User Story:** As a student learning to code, I want a simple, well-commented codebase using standard Python libraries, so that I can easily follow and understand the implementation.

#### Acceptance Criteria

1. WHEN examining the code THEN it SHALL use only Python, boto3, and standard libraries for core functionality
2. WHEN reading the code THEN each function SHALL have clear docstrings explaining its purpose
3. WHEN following the execution flow THEN variable names SHALL be descriptive and self-documenting
4. WHEN debugging THEN the code SHALL include strategic print statements and logging for educational visibility

### Requirement 5

**User Story:** As an educator, I want the chatbot to use Amazon Bedrock's Nova Lite model specifically, so that students can work with the model available in their learning environment and understand real AI service integration.

#### Acceptance Criteria

1. WHEN making API calls THEN the system SHALL use the Nova Lite model identifier as it is the only model available in the student environment
2. WHEN configuring the client THEN it SHALL properly authenticate with AWS credentials
3. WHEN handling responses THEN the system SHALL parse Nova Lite's specific response format
4. IF API calls fail THEN the system SHALL provide clear error messages for debugging
5. WHEN students deploy the code THEN it SHALL work within their restricted AWS environment that only has Nova Lite access

### Requirement 6

**User Story:** As a programming student, I want to see the conversation object structure evolve in real-time, so that I can understand how data structures grow and change during program execution.

#### Acceptance Criteria

1. WHEN a conversation starts THEN the system SHALL show an empty or minimal conversation object
2. WHEN each message is added THEN the system SHALL display the before and after states of the conversation object
3. WHEN using debugging tools THEN students SHALL be able to inspect the conversation object at any breakpoint
4. WHEN the conversation contains multiple exchanges THEN the JSON structure SHALL clearly show the chronological message flow