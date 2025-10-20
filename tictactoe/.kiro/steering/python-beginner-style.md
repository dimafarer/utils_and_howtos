# Python Style Guide for Week 3 Learners

## Purpose
This style guide ensures consistent, beginner-friendly Python code that reinforces fundamental concepts without introducing complexity that might confuse new learners.

## Allowed Python Features

### Variables and Data Types
```python
# Strings - use single or double quotes consistently
player_name = 'Alice'
game_title = "Tic-Tac-Toe"

# Numbers - integers and floats
position = 5
score = 0.0

# Booleans - always use True/False (not 1/0)
game_over = True
valid_input = False

# Lists - for collections of items
board_row = ['X', 'O', '3']
all_rows = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# Dictionaries - for key-value pairs
board_positions = {1: 'X', 2: 'O', 3: '3'}
```

### Control Structures
```python
# If statements - use clear conditions
if current_player == 'X':
    print("Player X's turn")
elif current_player == 'O':
    print("Player O's turn")
else:
    print("Unknown player")

# While loops - for repeating until condition changes
while not game_over:
    # game logic here
    pass

# For loops - for iterating over collections
for row in board:
    for cell in row:
        print(cell)

# Range loops - for counting
for i in range(3):
    print(f"Row {i}")
```

### Input/Output
```python
# Getting user input
player_input = input("Enter your move: ")

# Printing output
print("Welcome to Tic-Tac-Toe!")
print(f"Current player: {current_player}")

# Printing without newline
print("X", end=" ")
```

## Forbidden Features (Too Advanced)

### Functions and Classes
```python
# DON'T USE - too advanced for week 3
def check_winner():
    pass

class Game:
    pass
```

### Advanced Data Structures
```python
# DON'T USE - confusing for beginners
board = [[cell for cell in row] for row in initial_board]  # List comprehension
positions = {i: str(i) for i in range(1, 10)}  # Dict comprehension
```

### Advanced Control Flow
```python
# DON'T USE - too complex
try:
    position = int(input())
except ValueError as e:
    print(f"Error: {e}")  # Exception handling with variables

# DON'T USE - confusing syntax
result = "Win" if check_win() else "Continue"  # Ternary operator
```

## Naming Conventions

### Variables
- Use lowercase with underscores: `current_player`, `game_over`
- Be descriptive: `position_number` not `pos`
- Include data type hints in name when helpful: `board_list`, `player_dict`

### Constants
- Use ALL_CAPS for values that never change: `BOARD_SIZE = 3`
- Include descriptive comments: `MAX_MOVES = 9  # Maximum moves in tic-tac-toe`

## Code Organization

### File Structure
```python
# ============================================
# GAME SETUP
# ============================================
# All variable initialization here

# ============================================
# MAIN GAME LOOP  
# ============================================
# Primary game logic here

# ============================================
# GAME END
# ============================================
# Final messages and cleanup here
```

### Spacing and Layout
```python
# Good spacing around operators
position = row * 3 + column + 1
is_valid = position >= 1 and position <= 9

# Blank lines to separate logical sections
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
current_player = 'X'

while not game_over:
    # Display board code here
    pass
```

## Comment Style

### Inline Comments
```python
position = int(player_input)  # Convert string to number
board[row][col] = current_player  # Place X or O on board
```

### Block Comments
```python
# This section checks if there are three X's or O's in a row
# We need to check all possible winning combinations:
# - Three rows (horizontal wins)
# - Three columns (vertical wins)  
# - Two diagonals (diagonal wins)
```

### Variable Documentation
```python
# current_player: string, either 'X' or 'O'
# Keeps track of whose turn it is to play
current_player = 'X'

# board: list of lists, 3x3 grid
# Each inner list represents one row of the game board
# Values are either '1'-'9' (empty) or 'X'/'O' (occupied)
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
```

## Error Handling (Beginner Level)

### Simple Try-Except
```python
# Keep it simple - just catch the error and give helpful message
try:
    position = int(player_input)
except:
    print("Please enter a number, not letters")
    position = 0  # Set to invalid value
```

### Input Validation
```python
# Use clear, step-by-step validation
valid_input = False

# First check: is it a number?
try:
    position = int(player_input)
    # If we get here, it's a number
    
    # Second check: is it in range?
    if position >= 1 and position <= 9:
        # Third check: is the position empty?
        if board_position_is_empty(position):
            valid_input = True
        else:
            print("That position is already taken")
    else:
        print("Please enter a number between 1 and 9")
except:
    print("Please enter a number, not letters or symbols")
```

## Output Formatting

### Board Display
```python
# Create clear, consistent board layout
print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
print("-----------")
print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
print("-----------")
print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
```

### User Messages
```python
# Clear, helpful messages
print("Welcome to Tic-Tac-Toe!")
print("Enter a number from 1-9 to place your mark")
print(f"Player {current_player}, it's your turn")
print("Game Over! Thanks for playing!")
```

## Best Practices for Educational Code

### Consistency
- Use the same patterns throughout the code
- If you use `for i in range(3):` once, use it everywhere
- Keep variable naming patterns consistent

### Explicitness
- Don't use shortcuts that might confuse beginners
- Write out full conditions: `if game_over == True:` instead of `if game_over:`
- Use parentheses to make order of operations clear: `(row * 3) + column`

### Repetition for Learning
- It's okay to repeat similar code blocks
- Repetition helps reinforce patterns
- Don't worry about "DRY" (Don't Repeat Yourself) at this level

### Progressive Building
- Start with the simplest version that works
- Add features one at a time
- Test each addition before moving on
- Keep earlier, simpler versions as reference