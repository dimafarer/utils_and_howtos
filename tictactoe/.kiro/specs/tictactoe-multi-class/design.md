# Design Document: Tic-Tac-Toe Multi-Class Version

## Overview

This design document describes an advanced object-oriented implementation of tic-tac-toe that demonstrates multi-class design, separation of concerns, and scalable architecture. Unlike the single-class OOP version, this implementation uses multiple cooperating classes, each with a single, well-defined responsibility.

The design prioritizes:
- **Separation of Concerns**: Each class has one clear responsibility
- **Composition**: Objects contain and coordinate other objects
- **Scalability**: Works with any board size without code changes
- **Extensibility**: Easy to add new features or modify behavior
- **Educational Value**: Clear demonstration of advanced OOP principles

## Architecture

### High-Level Class Structure

```
┌─────────────────────────────────────────────────────────────┐
│                         Game                                 │
│  (Orchestrates gameplay, coordinates other classes)          │
│                                                              │
│  Responsibilities:                                           │
│  - Manage game flow and turns                               │
│  - Coordinate between Board and Players                      │
│  - Handle user input and validation                          │
│  - Determine game state (ongoing, won, tied)                │
└────────────┬──────────────────────────┬─────────────────────┘
             │                          │
             │ HAS-A                    │ HAS-A (2)
             │ (Composition)            │ (Composition)
             ▼                          ▼
┌────────────────────────┐    ┌──────────────────────┐
│        Board           │    │       Player         │
│                        │    │                      │
│  Responsibilities:     │    │  Responsibilities:   │
│  - Manage grid state   │    │  - Store mark (X/O)  │
│  - Display board       │    │  - Store name        │
│  - Validate moves      │    │  - Provide identity  │
│  - Check win conditions│    │                      │
│  - Place marks         │    │                      │
└────────────────────────┘    └──────────────────────┘
```

### Object Relationship Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                    COMPOSITION RELATIONSHIPS                  │
└──────────────────────────────────────────────────────────────┘

Game Object
├── Contains: 1 Board object
│   └── The Game HAS-A Board
│       - Game creates the Board
│       - Game calls Board methods
│       - Game does NOT access Board's internal grid directly
│
└── Contains: 2 Player objects
    └── The Game HAS-A Player (actually has two)
        - Game creates Player objects
        - Game asks Players for their marks
        - Game alternates between Players

┌──────────────────────────────────────────────────────────────┐
│                    METHOD CALL FLOW                           │
└──────────────────────────────────────────────────────────────┘

User Input
    │
    ▼
Game.play()
    │
    ├──> Board.display()           # Show current state
    │
    ├──> get_player_input()        # Get coordinate from user
    │
    ├──> Board.is_valid_move()     # Check if move is legal
    │
    ├──> Board.place_mark()        # Place the mark
    │
    ├──> Board.check_winner()      # Check for win/tie
    │
    └──> Game.switch_player()      # Change current player
```

### Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      DATA FLOW                               │
└─────────────────────────────────────────────────────────────┘

1. Game Initialization:
   ┌──────┐
   │ Game │ creates ──> ┌───────┐
   └──────┘             │ Board │ (with size from constant)
      │                 └───────┘
      │
      └─── creates ──> ┌────────┐
                       │Player X│
                       └────────┘
                       ┌────────┐
                       │Player O│
                       └────────┘

2. During Gameplay:
   User enters "11"
        │
        ▼
   ┌──────────────┐
   │ Game.play()  │
   └──────┬───────┘
          │
          ├─> Board.is_valid_move("11") ──> returns True/False
          │
          ├─> current_player.get_mark() ──> returns 'X' or 'O'
          │
          ├─> Board.place_mark("11", 'X') ──> updates grid
          │
          └─> Board.check_winner() ──> returns 'X', 'O', 'Tie', or None

3. Information Flow:
   Board ──(grid state)──> Game ──(display)──> User
   Player ──(mark)──> Game ──(place mark)──> Board
   User ──(coordinate)──> Game ──(validate)──> Board
```


## Components and Interfaces

### Board Class

The Board class is responsible for all board-related operations. It encapsulates the grid structure and provides methods for board manipulation and analysis.

```python
class Board:
    """
    Manages the game board state and operations.
    
    This class demonstrates:
    - Encapsulation of data (the grid)
    - Single Responsibility Principle (only board operations)
    - Dynamic sizing based on configuration
    
    Attributes:
        size (int): The dimension of the square board
        grid (list): 2D list representing the board state
    """
    
    def __init__(self, size=3):
        """
        Initialize the board with the specified size.
        
        Args:
            size (int): Board dimension (default 3 for 3x3)
        """
        pass
    
    def display(self):
        """Display the current board state with coordinates."""
        pass
    
    def is_valid_move(self, coordinate):
        """
        Check if a move to the given coordinate is valid.
        
        Args:
            coordinate (str): Two-digit coordinate (e.g., "11")
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        pass
    
    def place_mark(self, coordinate, mark):
        """
        Place a mark at the specified coordinate.
        
        Args:
            coordinate (str): Two-digit coordinate
            mark (str): Player's mark ('X' or 'O')
            
        Returns:
            bool: True if placement successful
        """
        pass
    
    def check_winner(self):
        """
        Check if there's a winner or tie.
        
        Returns:
            str or None: 'X', 'O', 'Tie', or None if game continues
        """
        pass
    
    def is_full(self):
        """
        Check if the board is completely filled.
        
        Returns:
            bool: True if no empty cells remain
        """
        pass
    
    def _parse_coordinate(self, coordinate):
        """
        Parse a coordinate string into row and column indices.
        
        Args:
            coordinate (str): Two-digit coordinate (e.g., "11")
            
        Returns:
            tuple: (row, col) or None if invalid
        """
        pass
    
    def _check_rows(self):
        """Check all rows for a win."""
        pass
    
    def _check_columns(self):
        """Check all columns for a win."""
        pass
    
    def _check_diagonals(self):
        """Check both diagonals for a win."""
        pass
```

**Design Rationale**:
- Private methods (prefixed with `_`) handle internal logic
- Public methods provide a clean interface for the Game class
- All board operations are centralized in one class
- No hardcoded board size - everything adapts to `self.size`

### Player Class

The Player class represents a game player. It's a simple data class that demonstrates how to model entities as objects.

```python
class Player:
    """
    Represents a player in the game.
    
    This class demonstrates:
    - Modeling real-world entities as objects
    - Encapsulation of player-specific data
    - Simple data classes in OOP
    
    Attributes:
        mark (str): The player's mark ('X' or 'O')
        name (str): Optional player name
    """
    
    def __init__(self, mark, name=None):
        """
        Initialize a player with a mark and optional name.
        
        Args:
            mark (str): Player's mark ('X' or 'O')
            name (str): Optional player name (default: None)
        """
        pass
    
    def get_mark(self):
        """
        Get the player's mark.
        
        Returns:
            str: The player's mark ('X' or 'O')
        """
        pass
    
    def get_name(self):
        """
        Get the player's name or mark if no name set.
        
        Returns:
            str: Player's name or mark
        """
        pass
    
    def __str__(self):
        """
        String representation of the player.
        
        Returns:
            str: Player's name or mark
        """
        pass
```

**Design Rationale**:
- Simple class focusing on data storage
- Provides getter methods for encapsulation
- `__str__` method for easy display
- Could be extended with player statistics, AI logic, etc.

### Game Class

The Game class orchestrates the entire game. It coordinates between the Board and Players, manages game flow, and handles user interaction.

```python
class Game:
    """
    Orchestrates the tic-tac-toe game.
    
    This class demonstrates:
    - Composition (contains Board and Player objects)
    - Coordination between multiple classes
    - Separation of concerns (game logic vs board logic)
    - Dependency injection (receives objects it needs)
    
    Attributes:
        board (Board): The game board
        player_x (Player): Player using 'X'
        player_o (Player): Player using 'O'
        current_player (Player): The player whose turn it is
        game_over (bool): Whether the game has ended
        winner (str): The winner ('X', 'O', 'Tie', or None)
    """
    
    def __init__(self, board_size=3):
        """
        Initialize a new game.
        
        Args:
            board_size (int): Size of the board (default 3)
        """
        pass
    
    def play(self):
        """Run the main game loop."""
        pass
    
    def switch_player(self):
        """Switch to the other player."""
        pass
    
    def get_player_input(self):
        """
        Get and validate coordinate input from the current player.
        
        Returns:
            str: Valid coordinate string
        """
        pass
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        pass
    
    def display_result(self):
        """Display the game result."""
        pass
```

**Design Rationale**:
- Game doesn't know about board internals - uses Board's public interface
- Game doesn't manipulate player data - asks Players for information
- All user interaction happens in Game class
- Game coordinates but doesn't duplicate Board or Player logic

## Data Models

### Board Grid Structure

The board uses a 2D nested list where each cell contains either:
- A coordinate string (e.g., "00", "11", "22") if empty
- A player mark ('X' or 'O') if occupied

```python
# Example 3x3 board (initial state):
[
    ["00", "01", "02"],  # Row 0
    ["10", "11", "12"],  # Row 1
    ["20", "21", "22"]   # Row 2
]

# After some moves:
[
    ["X",  "01", "O" ],  # X at 00, O at 02
    ["10", "X",  "12"],  # X at 11
    ["20", "21", "22"]
]
```

**Coordinate System**:
- First digit: row index (0 to size-1)
- Second digit: column index (0 to size-1)
- Top-left is "00"
- Bottom-right is "22" (for 3x3), "33" (for 4x4), etc.

### Configuration Constant

A single constant controls board size:

```python
# At the top of the file
BOARD_SIZE = 3  # Change this to 4, 5, etc. for different sizes
```

All code adapts to this value:
- Board initialization
- Coordinate validation
- Win detection
- Display formatting

## Class Interaction Patterns

### Pattern 1: Composition

```
Game "has-a" Board
Game "has-a" Player (two of them)

┌──────────┐
│   Game   │
│          │
│  board ──┼──> Board object
│          │
│player_x ─┼──> Player object (X)
│          │
│player_o ─┼──> Player object (O)
└──────────┘
```

**Why Composition?**
- Game needs a Board to function
- Game needs Players to function
- These are "has-a" relationships, not "is-a"
- Allows independent testing of each class

### Pattern 2: Delegation

```
Game delegates board operations to Board:

Game.play() calls:
  ├─> Board.display()
  ├─> Board.is_valid_move()
  ├─> Board.place_mark()
  └─> Board.check_winner()

Game doesn't manipulate the grid directly!
```

**Why Delegation?**
- Game doesn't need to know how Board works internally
- Board can change implementation without affecting Game
- Clear separation of responsibilities

### Pattern 3: Encapsulation

```
Board encapsulates the grid:

Public Interface:          Private Implementation:
├─ display()              ├─ self.grid (hidden)
├─ is_valid_move()        ├─ _parse_coordinate()
├─ place_mark()           ├─ _check_rows()
├─ check_winner()         ├─ _check_columns()
└─ is_full()              └─ _check_diagonals()

External code uses public methods only!
```

**Why Encapsulation?**
- Hides complexity from users of the class
- Allows internal changes without breaking external code
- Provides a clean, simple interface


## Scalability Design

### Dynamic Board Size Implementation

All code must work with any board size. Here's how each component adapts:

#### Board Initialization
```python
def __init__(self, size=3):
    self.size = size
    self.grid = []
    
    # Create grid dynamically based on size
    for row in range(self.size):
        row_list = []
        for col in range(self.size):
            # Each cell shows its coordinate
            coordinate = f"{row}{col}"
            row_list.append(coordinate)
        self.grid.append(row_list)
```

#### Win Detection (Rows)
```python
def _check_rows(self):
    # Works for any board size!
    for row in range(self.size):
        first_cell = self.grid[row][0]
        
        # Skip if first cell is empty (still shows coordinate)
        if len(first_cell) == 2:  # Coordinate, not mark
            continue
        
        # Check if all cells in this row match
        all_match = True
        for col in range(self.size):
            if self.grid[row][col] != first_cell:
                all_match = False
                break
        
        if all_match:
            return first_cell  # Return the winner
    
    return None
```

#### Win Detection (Columns)
```python
def _check_columns(self):
    # Works for any board size!
    for col in range(self.size):
        first_cell = self.grid[0][col]
        
        if len(first_cell) == 2:  # Coordinate, not mark
            continue
        
        all_match = True
        for row in range(self.size):
            if self.grid[row][col] != first_cell:
                all_match = False
                break
        
        if all_match:
            return first_cell
    
    return None
```

#### Win Detection (Diagonals)
```python
def _check_diagonals(self):
    # Main diagonal (top-left to bottom-right)
    first_cell = self.grid[0][0]
    if len(first_cell) == 1:  # It's a mark, not coordinate
        all_match = True
        for i in range(self.size):
            if self.grid[i][i] != first_cell:
                all_match = False
                break
        if all_match:
            return first_cell
    
    # Anti-diagonal (top-right to bottom-left)
    first_cell = self.grid[0][self.size - 1]
    if len(first_cell) == 1:
        all_match = True
        for i in range(self.size):
            if self.grid[i][self.size - 1 - i] != first_cell:
                all_match = False
                break
        if all_match:
            return first_cell
    
    return None
```

### Coordinate Validation
```python
def _parse_coordinate(self, coordinate):
    # Validate format
    if len(coordinate) != 2:
        return None
    
    if not coordinate.isdigit():
        return None
    
    row = int(coordinate[0])
    col = int(coordinate[1])
    
    # Validate range (adapts to board size!)
    if row < 0 or row >= self.size:
        return None
    if col < 0 or col >= self.size:
        return None
    
    return (row, col)
```

## Error Handling

### Input Validation Layers

**Layer 1: Format Validation**
```python
# Check if input is two digits
if len(coordinate) != 2 or not coordinate.isdigit():
    print("Invalid format! Enter two digits (e.g., '11' for center)")
    return False
```

**Layer 2: Range Validation**
```python
# Check if coordinates are within board bounds
row, col = int(coordinate[0]), int(coordinate[1])
if row >= self.size or col >= self.size:
    print(f"Out of range! Valid coordinates: 00 to {self.size-1}{self.size-1}")
    return False
```

**Layer 3: Occupancy Validation**
```python
# Check if cell is already occupied
if len(self.grid[row][col]) == 1:  # Single character = mark
    print(f"Cell {coordinate} is already occupied by {self.grid[row][col]}")
    return False
```

### Error Messages

All error messages should be:
- **Specific**: Explain exactly what's wrong
- **Educational**: Help the user understand the coordinate system
- **Actionable**: Tell the user what to do instead

Examples:
- "Invalid format! Enter two digits like '00', '11', or '22'"
- "Out of range! For a 3x3 board, use coordinates from 00 to 22"
- "Cell 11 is already occupied by X. Choose an empty cell."

## Testing Strategy

### Unit Testing

**Board Class Tests**:
- Test board initialization for different sizes (3x3, 4x4, 5x5)
- Test coordinate parsing (valid and invalid)
- Test move validation (format, range, occupancy)
- Test mark placement
- Test win detection (rows, columns, diagonals) for different sizes
- Test tie detection

**Player Class Tests**:
- Test player creation with mark
- Test player creation with name
- Test getter methods
- Test string representation

**Game Class Tests**:
- Test game initialization
- Test player switching
- Test game flow coordination
- Test input handling

### Integration Testing

Test the complete game flow:
- Create game with different board sizes
- Play through complete games
- Test various winning scenarios
- Test tie scenarios
- Test error handling during gameplay

### Scalability Testing

Verify the code works with different board sizes:
- 3x3 (standard)
- 4x4 (larger)
- 5x5 (even larger)
- Ensure no hardcoded values break functionality

## Comparison with Single-Class Version

### Single-Class Version (tictactoe_oop.py)

```
┌─────────────────────────────────┐
│      TicTacToeGame              │
│                                 │
│  - board                        │
│  - current_player               │
│  - game_over                    │
│  - winner                       │
│  - moves_made                   │
│                                 │
│  + display_board()              │
│  + make_move()                  │
│  + check_winner()               │
│  + switch_player()              │
│  + play()                       │
│  + ... (all methods in one class)│
└─────────────────────────────────┘

Characteristics:
- Everything in one class
- Simpler for beginners
- Less flexible
- Harder to extend
```

### Multi-Class Version (tictactoe_multiclass.py)

```
┌──────────┐      ┌──────────┐      ┌──────────┐
│   Game   │─────>│  Board   │      │  Player  │
│          │      │          │      │          │
│ Manages  │      │ Manages  │      │ Stores   │
│ gameplay │      │ grid     │      │ identity │
└──────────┘      └──────────┘      └──────────┘

Characteristics:
- Separated responsibilities
- More complex initially
- Much more flexible
- Easy to extend
- Better for larger projects
```

### Key Differences

| Aspect | Single-Class | Multi-Class |
|--------|-------------|-------------|
| **Classes** | 1 | 3 |
| **Responsibilities** | Mixed | Separated |
| **Board Size** | Hardcoded 3x3 | Configurable |
| **Extensibility** | Limited | High |
| **Complexity** | Lower | Higher |
| **Best For** | Learning OOP basics | Learning OOP design |
| **Real-World** | Small scripts | Production code |

## Benefits of Multi-Class Design

### 1. Separation of Concerns
Each class has one job:
- Board: Manage the grid
- Player: Represent a player
- Game: Coordinate gameplay

### 2. Easier Testing
Test each class independently:
```python
# Test Board without Game
board = Board(3)
board.place_mark("11", 'X')
assert board.check_winner() == None

# Test Player without Game
player = Player('X', 'Alice')
assert player.get_mark() == 'X'
```

### 3. Easier Maintenance
Change one class without affecting others:
- Change board display format? Only modify Board class
- Add player statistics? Only modify Player class
- Change game rules? Only modify Game class

### 4. Easier Extension
Add new features by extending classes:
```python
# Add AI player
class AIPlayer(Player):
    def choose_move(self, board):
        # AI logic here
        pass

# Add different board types
class HexBoard(Board):
    # Hexagonal board implementation
    pass
```

### 5. Reusability
Use classes in different contexts:
```python
# Use Board in a different game
tournament_boards = [Board(3) for _ in range(10)]

# Use Player in a different game
player = Player('X', 'Alice')
# Can use this player in any game that needs players
```

## Implementation Notes

### File Structure
```python
"""
Tic-Tac-Toe Multi-Class Version

Demonstrates advanced OOP concepts:
- Multi-class design
- Separation of concerns
- Composition
- Scalable architecture
"""

# Configuration
BOARD_SIZE = 3  # Change this to modify board size

# ============================================
# BOARD CLASS
# ============================================
class Board:
    pass

# ============================================
# PLAYER CLASS
# ============================================
class Player:
    pass

# ============================================
# GAME CLASS
# ============================================
class Game:
    pass

# ============================================
# MAIN PROGRAM
# ============================================
if __name__ == "__main__":
    game = Game(BOARD_SIZE)
    game.play()
```

### Educational Comments

Every class and method should include:
- Purpose and responsibility
- How it relates to other classes
- Design patterns demonstrated
- Why this design choice was made

Example:
```python
class Board:
    """
    Manages the game board.
    
    This class demonstrates:
    - Encapsulation: Grid is private, accessed through methods
    - Single Responsibility: Only handles board operations
    - Scalability: Works with any board size
    
    The Board doesn't know about Players or Game rules.
    It just manages the grid and provides operations on it.
    This separation allows the Board to be reused in different
    games or contexts.
    """
```

## Summary

This multi-class design demonstrates advanced OOP principles:

1. **Separation of Concerns**: Each class has one responsibility
2. **Composition**: Game contains Board and Player objects
3. **Encapsulation**: Internal details are hidden
4. **Scalability**: Works with any board size
5. **Extensibility**: Easy to add new features
6. **Maintainability**: Changes are localized to specific classes

The design is more complex than the single-class version, but provides significant benefits for larger projects and demonstrates real-world OOP practices.
