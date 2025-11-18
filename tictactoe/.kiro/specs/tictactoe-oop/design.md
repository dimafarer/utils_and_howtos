# Design Document: Tic-Tac-Toe OOP Version

## Overview

This design document describes an object-oriented implementation of tic-tac-toe for students learning OOP concepts. The implementation will demonstrate key OOP principles including encapsulation, separation of concerns, and clean code organization while maintaining the educational clarity of the existing procedural versions.

The design prioritizes educational value by:
- Using clear, well-documented classes and methods
- Demonstrating proper OOP patterns (constructors, instance variables, methods)
- Maintaining consistency with existing versions for easy comparison
- Including extensive documentation to explain OOP concepts

## Architecture

### High-Level Structure

The application will use a class-based architecture with clear separation of concerns:

```
TicTacToeGame (Main Game Class)
├── Board state management
├── Player turn tracking
├── Game flow control
└── Win/tie detection

Helper Functions
├── display_board()
├── get_player_input()
└── display_welcome_message()

Main Program
└── Game instantiation and execution
```

### Design Approach

**Single Class Design**: We'll use one main `TicTacToeGame` class that encapsulates all game logic. This approach is appropriate for educational purposes because:
- It's simple enough for OOP beginners to understand
- It demonstrates core OOP concepts without overwhelming complexity
- It shows clear before/after comparison with procedural versions
- It keeps related functionality together

**Alternative Considered**: A multi-class design (Board, Player, GameLogic classes) would demonstrate more advanced OOP concepts but may be too complex for students just learning classes.

**Data Structure Choice**: We use nested lists instead of dictionaries because:
- Lists naturally represent 2D grids
- The implementation is easily scalable to larger boards (4x4, 5x5, NxN)
- Students learn important 2D array indexing concepts
- Row/column math (position conversion) is a valuable learning exercise
- Future extensions (variable board size) are straightforward

**Scalability Consideration**: While this version implements a standard 3x3 board, the design allows for easy extension to variable board sizes by:
- Parameterizing board_size in the constructor
- Using loops instead of hardcoded win conditions
- Converting position numbers based on board_size

## Components and Interfaces

### TicTacToeGame Class

The main class that encapsulates all game functionality.

```python
class TicTacToeGame:
    """
    Main game class for tic-tac-toe.
    
    Encapsulates all game state and behavior including board management,
    player turns, move validation, and win detection.
    """
    
    def __init__(self):
        """Initialize a new game."""
        
    def display_board(self):
        """Display the current board state."""
        
    def make_move(self, position):
        """
        Attempt to make a move at the specified position.
        
        Args:
            position (int): Board position 1-9
            
        Returns:
            bool: True if move was valid and made, False otherwise
        """
        
    def check_winner(self):
        """
        Check if there's a winner or tie.
        
        Returns:
            str or None: 'X', 'O', 'Tie', or None if game continues
        """
        
    def switch_player(self):
        """Switch to the other player."""
        
    def is_game_over(self):
        """
        Check if the game has ended.
        
        Returns:
            bool: True if game is over, False otherwise
        """
        
    def play(self):
        """Run the main game loop."""
```

### Helper Functions

Functions that support the game but don't need to be methods:

```python
def get_player_input(current_player):
    """
    Get and validate input from the player.
    
    Args:
        current_player (str): 'X' or 'O'
        
    Returns:
        int: Valid position 1-9
    """

def display_welcome_message():
    """Display game introduction and instructions."""

def display_game_over_message(winner):
    """
    Display the game over message.
    
    Args:
        winner (str): 'X', 'O', or 'Tie'
    """
```

## Data Models

### Board Representation

The board will be stored as a nested list (list of lists) representing a 3x3 grid:

```python
[
    ['1', '2', '3'],  # Row 0
    ['4', '5', '6'],  # Row 1
    ['7', '8', '9']   # Row 2
]
```

**Rationale**: Nested list approach is chosen because:
- Natural 2D representation of the game board
- Easily scalable to larger boards (4x4, 5x5, or even NxN)
- Demonstrates working with 2D data structures (important OOP concept)
- Consistent with one of the existing versions (easy comparison)
- Teaches row/column indexing with [row][col] notation
- More flexible for future extensions (different board sizes)

**Position Conversion**: User-facing positions (1-9) will be converted to row/column coordinates:
```python
# Position to coordinates
row = (position - 1) // 3  # Integer division
col = (position - 1) % 3   # Modulo operation

# Examples:
# Position 1 → row=0, col=0
# Position 5 → row=1, col=1
# Position 9 → row=2, col=2
```

### Game State

Instance variables that track game state:

```python
self.board: list          # 3x3 nested list of board positions and marks
self.board_size: int      # Size of board (3 for standard game, scalable)
self.current_player: str  # 'X' or 'O'
self.game_over: bool      # Whether game has ended
self.winner: str or None  # 'X', 'O', 'Tie', or None
self.moves_made: int      # Count of moves made
```

### Win Detection Approach

Win conditions will be checked systematically using loops:

**Row Wins**: Check each row using a loop
```python
for row in range(3):
    if board[row][0] == board[row][1] == board[row][2]:
        # Check if not empty and return winner
```

**Column Wins**: Check each column using a loop
```python
for col in range(3):
    if board[0][col] == board[1][col] == board[2][col]:
        # Check if not empty and return winner
```

**Diagonal Wins**: Check both diagonals explicitly
```python
# Main diagonal: [0][0], [1][1], [2][2]
# Anti-diagonal: [0][2], [1][1], [2][0]
```

**Scalability Note**: This approach can be easily extended to larger boards by changing the loop range and board size.


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Empty positions display their numbers

*For any* board state, when displaying the board, all empty positions (those not containing 'X' or 'O') should display their position number (1-9).
**Validates: Requirements 2.4**

### Property 2: Occupied positions display player marks

*For any* board state, when displaying the board, all occupied positions should display the player's mark ('X' or 'O') that occupies them.
**Validates: Requirements 2.5**

### Property 3: Invalid position range rejection

*For any* position value outside the range 1-9, attempting to make a move should be rejected (return False or raise an error).
**Validates: Requirements 3.1**

### Property 4: Occupied position rejection

*For any* board position that is already occupied by 'X' or 'O', attempting to make a move at that position should be rejected.
**Validates: Requirements 3.2**

### Property 5: Invalid moves return False

*For any* invalid move (out of range or occupied position), the make_move method should return False or raise an appropriate error.
**Validates: Requirements 3.3**

### Property 6: Valid moves return True

*For any* valid move (position 1-9 that is empty), the make_move method should return True.
**Validates: Requirements 3.4**

### Property 7: Valid moves update board

*For any* valid move at position P, after making the move, the board at position P should contain the current player's mark.
**Validates: Requirements 4.1**

### Property 8: Moves place correct player mark

*For any* valid move, the mark placed on the board should match the current player ('X' or 'O').
**Validates: Requirements 4.2**

### Property 9: Valid moves switch players

*For any* valid move when the game continues, the current player should switch from 'X' to 'O' or from 'O' to 'X'.
**Validates: Requirements 4.4**

### Property 10: Moves increment counter

*For any* valid move, the moves_made counter should increase by exactly 1.
**Validates: Requirements 4.5**

### Property 11: Horizontal wins detected

*For any* board state where three identical marks ('X' or 'O') occupy a complete row (positions 1-2-3, 4-5-6, or 7-8-9), check_winner should return that player as the winner.
**Validates: Requirements 5.1**

### Property 12: Vertical wins detected

*For any* board state where three identical marks ('X' or 'O') occupy a complete column (positions 1-4-7, 2-5-8, or 3-6-9), check_winner should return that player as the winner.
**Validates: Requirements 5.2**

### Property 13: Diagonal wins detected

*For any* board state where three identical marks ('X' or 'O') occupy a complete diagonal (positions 1-5-9 or 3-5-7), check_winner should return that player as the winner.
**Validates: Requirements 5.3**

### Property 14: Win sets game_over flag

*For any* winning board state (horizontal, vertical, or diagonal win), the game_over attribute should be True.
**Validates: Requirements 5.4**

### Property 15: Win sets winner attribute

*For any* winning board state, the winner attribute should be set to the winning player ('X' or 'O').
**Validates: Requirements 5.5**

### Property 16: Invalid moves preserve player turn

*For any* invalid move attempt, the current player should remain unchanged.
**Validates: Requirements 8.3**

## Error Handling

### Input Validation

The system will handle errors at multiple levels:

1. **Type Errors**: Non-numeric input will be caught using try-except blocks
   ```python
   try:
       position = int(user_input)
   except ValueError:
       print("Please enter a number, not letters or symbols")
   ```

2. **Range Errors**: Out-of-range positions (< 1 or > 9) will be validated
   ```python
   if position < 1 or position > 9:
       print("Please enter a number between 1 and 9")
       return False
   ```

3. **State Errors**: Occupied positions will be checked before moves
   ```python
   if self.board[position] in ['X', 'O']:
       print(f"Position {position} is already taken")
       return False
   ```

### Error Messages

All error messages will be:
- Clear and specific about what went wrong
- Educational, explaining why the input was invalid
- Helpful, suggesting what the user should do instead

Example error messages:
- "Please enter a number, not letters or symbols"
- "Please enter a number between 1 and 9"
- "Position 5 is already taken by X. Choose an empty position."

### Graceful Degradation

The game will never crash due to user input:
- All input will be validated before use
- Invalid input will result in re-prompting, not errors
- The game state will remain consistent even with invalid input

## Testing Strategy

### Unit Testing Approach

Unit tests will verify individual methods and behaviors:

**Initialization Tests**:
- Test that `__init__` creates correct initial board state
- Test that starting player is 'X'
- Test that game_over is False initially
- Test that winner is None initially

**Move Validation Tests**:
- Test valid moves (positions 1-9 on empty squares)
- Test invalid moves (out of range, occupied positions)
- Test that invalid moves don't change board state

**Win Detection Tests**:
- Test all 3 horizontal win conditions
- Test all 3 vertical win conditions
- Test both diagonal win conditions
- Test that non-winning states return None

**Tie Detection Tests**:
- Test full board with no winner returns 'Tie'
- Test partial board doesn't return 'Tie'

**Player Switching Tests**:
- Test that valid moves switch players
- Test that invalid moves don't switch players

### Property-Based Testing Approach

We will use **Hypothesis** as the property-based testing library for Python. Hypothesis will generate random test cases to verify our correctness properties.

**Configuration**: Each property-based test will run a minimum of 100 iterations to ensure thorough coverage.

**Property Test Examples**:

1. **Board Display Properties** (Properties 1-2):
   - Generate random board states
   - Verify empty positions show numbers
   - Verify occupied positions show marks

2. **Move Validation Properties** (Properties 3-6):
   - Generate random positions (valid and invalid)
   - Verify validation logic works correctly
   - Verify return values match expectations

3. **Game State Properties** (Properties 7-10):
   - Generate random valid moves
   - Verify board updates correctly
   - Verify player switching works
   - Verify move counter increments

4. **Win Detection Properties** (Properties 11-15):
   - Generate random winning board states
   - Verify all win conditions are detected
   - Verify game_over and winner are set correctly

5. **State Preservation Properties** (Property 16):
   - Generate random invalid moves
   - Verify game state remains unchanged

**Property Test Tagging**: Each property-based test will include a comment tag in this format:
```python
# Feature: tictactoe-oop, Property 1: Empty positions display their numbers
```

### Integration Testing

Integration tests will verify the complete game flow:
- Test a complete game from start to finish
- Test multiple games in sequence
- Test various winning scenarios
- Test tie game scenarios

### Test Organization

Tests will be organized in a single test file: `test_tictactoe_oop.py`

Structure:
```python
# Unit tests for initialization
class TestInitialization:
    pass

# Unit tests for move validation
class TestMoveValidation:
    pass

# Unit tests for win detection
class TestWinDetection:
    pass

# Property-based tests
class TestProperties:
    pass

# Integration tests
class TestGameFlow:
    pass
```

## Implementation Notes

### Educational Considerations

1. **Clear Method Names**: Use descriptive names that explain what each method does
   - `make_move()` instead of `move()`
   - `check_winner()` instead of `check()`
   - `display_board()` instead of `show()`

2. **Extensive Documentation**: Every class and method includes:
   - Docstring explaining purpose
   - Parameter descriptions
   - Return value descriptions
   - Example usage when helpful

3. **Step-by-Step Comments**: Complex logic includes inline comments explaining:
   - What the code does
   - Why it's done this way
   - How it relates to OOP concepts

4. **Comparison Comments**: Where appropriate, include comments comparing to procedural versions:
   ```python
   # In the procedural version, this was a global variable
   # In OOP, we use self.board to encapsulate it in the class
   self.board = {}
   ```

### Code Style

- Follow PEP 8 Python style guidelines
- Use 4 spaces for indentation
- Use descriptive variable names
- Keep methods focused on single responsibilities
- Limit method length to ~20 lines when possible

### File Structure

```python
"""
Tic-Tac-Toe Game - Object-Oriented Version

Educational implementation demonstrating OOP concepts.
"""

# ============================================
# CLASS DEFINITION
# ============================================

class TicTacToeGame:
    """Main game class."""
    pass

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_player_input(current_player):
    """Get player input."""
    pass

# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
```

## Comparison with Existing Versions

### Advantages of OOP Version

1. **Organization**: Related data and behavior are grouped together
2. **Reusability**: Game class can be instantiated multiple times
3. **Maintainability**: Changes to game logic are localized to methods
4. **Testability**: Methods can be tested independently
5. **Scalability**: Easy to extend with new features (undo, save/load, etc.)

### Similarities with Existing Versions

1. **Gameplay**: Identical user experience
2. **Board Display**: Same visual format
3. **Input Validation**: Same validation logic
4. **Win Detection**: Same win conditions
5. **Error Messages**: Similar helpful messages
6. **Data Structure**: Uses nested lists like the list version for easy comparison

### Key Difference: Lists vs Dictionary

**Why Lists Are Better for This OOP Version**:
- **Scalability**: Can easily change board size (3x3 → 4x4 → NxN)
- **2D Thinking**: Reinforces understanding of 2D data structures
- **Real-world Modeling**: Grids are naturally 2D, not 1D with keys
- **Future Extensions**: Easier to add features like board size selection
- **Educational Value**: Teaches coordinate conversion and 2D indexing

Students can compare:
- **Dictionary version** (direct position access) vs **List version** (row/col indexing)
- **Procedural list version** vs **OOP list version** (organization differences)
- See how the same data structure works in different paradigms

### Learning Progression

Students can compare:
- **Procedural (lists/dict)** → **OOP**: See how classes organize code
- **Global variables** → **Instance variables**: Understand encapsulation
- **Inline code** → **Methods**: See benefits of code organization
- **Repeated logic** → **Reusable methods**: Understand DRY principle
