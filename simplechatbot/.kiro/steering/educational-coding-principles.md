---
inclusion: always
---

# Educational Coding Principles

## Target Audience
This project is designed for **beginner programmers** who are new to coding. All code should be accessible and educational for students just starting their programming journey.

## Code Simplicity Requirements

### No Advanced Python Features
- **NO classes or objects** - Use only functions and simple data structures
- **NO decorators** - Keep function definitions simple
- **NO complex inheritance or OOP concepts**
- **NO advanced Python features** like generators, context managers, or metaclasses

### Use Simple Data Structures
- **Dictionaries and lists only** for data storage
- **No custom classes** - everything should be built-in Python types
- **JSON-serializable structures** to demonstrate data transfer concepts

### Function-Based Design
- **Pure functions** where possible - input parameters, return values
- **Clear function names** that describe exactly what they do
- **One responsibility per function** - keep functions focused and small
- **Minimal function parameters** - avoid complex parameter lists

## Educational Transparency

### Visible State Changes
- **Print statements** to show data transformations
- **Before/after comparisons** when data changes
- **JSON pretty-printing** to make data structures visible
- **Step-by-step logging** of what the program is doing

### Debugging-Friendly Code
- **Strategic print statements** for debugging sessions
- **Clear variable names** that explain their purpose
- **Breakpoint-friendly structure** for line-by-line debugging
- **Minimal nesting** to make code flow easy to follow

### Simplicity First
- **NO complex error handling** - basic try/except only when absolutely necessary
- **NO testing frameworks** - keep focus on core concepts
- **NO mock objects** - use real AWS calls or simple examples
- **NO complex validation** - trust that inputs are correct for learning
- **Assume happy path** - focus on demonstrating concepts, not edge cases

## Learning Objectives

### Demonstrate Key Concepts
1. **LLMs are stateless** - show that memory is application responsibility
2. **JSON data transfer** - make API communication visible
3. **State management** - show how applications maintain conversation history
4. **API integration** - demonstrate real-world service interaction

### Avoid Overwhelming Beginners
- **Minimal dependencies** - only essential libraries (boto3, json, datetime, uuid)
- **No complex error handling** - basic try/except only when necessary
- **Linear program flow** - avoid complex control structures
- **Clear separation of concerns** - each function has obvious purpose
- **No testing code** - focus on core functionality only
- **No mock objects** - keep it real and simple
- **Assume AWS works** - don't overcomplicate with connection testing