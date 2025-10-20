# Educational Coding Standards for Beginner Python

## Purpose
This document defines coding standards specifically for educational Python code targeting week 3 learners who are just beginning to understand variables, loops, conditionals, and basic data structures.

## Core Principles

### 1. Clarity Over Efficiency
- Prioritize code readability and understanding over performance
- Break complex operations into multiple simple steps
- Use explicit, verbose approaches rather than clever shortcuts
- Avoid advanced Python features (list comprehensions, lambda functions, etc.)

### 2. No Functions or Classes
- Use only basic programming constructs: variables, loops, conditionals
- All code should be linear and procedural
- Avoid any abstraction that might confuse beginners
- Keep all logic in the main program flow

### 3. Extensive Documentation
- Every variable must have a comment explaining its purpose and data type
- Every loop must explain what it iterates over and why
- Every conditional must explain the logic being tested
- Complex operations must be broken down step-by-step

## Variable Naming Standards

### Use Descriptive Names
```python
# Good - clear and descriptive
current_player = 'X'
game_over = False
player_input = input("Enter position: ")

# Bad - too abbreviated or unclear
cp = 'X'
done = False
inp = input("Enter position: ")
```

### Include Data Type Context
```python
# Good - name suggests the data type
position_number = 5
board_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
player_dict = {1: 'X', 2: 'O'}

# Acceptable - clear from context
current_player = 'X'
winner = 'O'
```

## Comment Standards

### Variable Comments
```python
# current_player is a string that holds either 'X' or 'O'
# This tells us whose turn it is to play
current_player = 'X'

# game_over is a boolean (True/False) that tracks if the game has ended
# We start with False because the game just began
game_over = False
```

### Loop Comments
```python
# This loop goes through each row in our board
# i will be 0, then 1, then 2 (for the three rows)
for i in range(3):
    # This inner loop goes through each column in the current row
    # j will be 0, then 1, then 2 (for the three columns)
    for j in range(3):
        # board[i][j] gets the value at row i, column j
        print(board[i][j], end=' ')
```

### Conditional Comments
```python
# Check if the player entered a valid number
# We use try/except to catch errors if they enter letters or symbols
try:
    # int() converts the string input to a number
    position = int(player_input)
    
    # Check if the number is between 1 and 9 (valid positions)
    if position >= 1 and position <= 9:
        valid_move = True
    else:
        # The number is outside our valid range
        print("Please enter a number between 1 and 9")
        valid_move = False
except:
    # This runs if int() failed (they entered non-numbers)
    print("Please enter a number, not letters or symbols")
    valid_move = False
```

## Code Structure Standards

### Section Headers
Use clear comment headers to separate different parts of the code:

```python
# ============================================
# GAME SETUP - Initialize variables and board
# ============================================

# ============================================
# MAIN GAME LOOP - Keep playing until game ends
# ============================================

# ============================================
# INPUT VALIDATION - Check if move is valid
# ============================================

# ============================================
# WIN CHECKING - See if someone won the game
# ============================================
```

### Consistent Indentation
- Use 4 spaces for indentation (Python standard)
- Be consistent throughout the file
- Align related code at the same indentation level

### Logical Grouping
Group related operations together with blank lines:

```python
# Initialize the game board
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
current_player = 'X'
game_over = False

# Start the main game loop
while not game_over:
    # Display the current board
    # ... board display code ...
    
    # Get player input
    # ... input code ...
```

## Educational Considerations

### Progressive Complexity
- Start with simple variable assignments
- Introduce basic conditionals
- Add simple loops
- Build up to nested structures
- End with complete integration

### Concept Reinforcement
- Repeat similar patterns to reinforce learning
- Use consistent approaches across different parts
- Highlight when the same concept is used in different ways

### Error Prevention
- Use clear variable names to prevent confusion
- Add validation to prevent common beginner mistakes
- Provide helpful error messages that teach, not just inform

## Implementation Guidelines

### Data Structure Demonstration
When showing different approaches (lists vs dictionaries):
- Use identical variable names where possible
- Follow the same logical flow
- Highlight the differences in comments
- Ensure both produce identical output

### Testing Approach
- Include manual testing instructions
- Provide example inputs and expected outputs
- Document common errors and their solutions
- Create step-by-step debugging guides
## Develo
pment Environment

### Virtual Environment Usage
- Always use the project's virtual environment when testing code
- Use `python` command (not `python3`) when venv is activated
- Test all code implementations before marking tasks complete
- Ensure code runs without errors in the target environment