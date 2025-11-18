# Procedural vs Object-Oriented Programming: A Tic-Tac-Toe Comparison

## Introduction

This document compares three different implementations of tic-tac-toe, each representing a different programming paradigm and level of complexity. By studying these versions side-by-side, you'll understand how programming approaches evolve and when to use each one.

## The Three Versions

### 1. Procedural (No Functions/Classes)
**Files**: `tictactoe_lists.py`, `tictactoe_dict.py`
**Level**: Beginner (Week 3)
**Paradigm**: Procedural programming with global variables

### 2. Single-Class OOP
**File**: `tictactoe_oop.py`
**Level**: Intermediate (OOP Learners)
**Paradigm**: Object-oriented with one class

### 3. Multi-Class OOP
**File**: `tictactoe_multiclass.py`
**Level**: Advanced (OOP Architecture)
**Paradigm**: Object-oriented with multiple classes

---

## Visual Architecture Comparison

### Procedural Version (No Classes)

```
┌─────────────────────────────────────────────────────────┐
│                    GLOBAL SCOPE                          │
│                                                          │
│  Variables (scattered throughout):                      │
│  ├─ board = [['1','2','3'], ...]                       │
│  ├─ current_player = 'X'                               │
│  ├─ game_over = False                                  │
│  ├─ winner = None                                      │
│  └─ moves_made = 0                                     │
│                                                          │
│  Code (linear, top to bottom):                          │
│  ├─ Initialize variables                               │
│  ├─ Display welcome message                            │
│  ├─ WHILE not game_over:                               │
│  │   ├─ Display board (inline code)                    │
│  │   ├─ Get input (inline code)                        │
│  │   ├─ Validate move (inline code)                    │
│  │   ├─ Update board (inline code)                     │
│  │   ├─ Check winner (inline code)                     │
│  │   └─ Switch player (inline code)                    │
│  └─ Display result                                      │
│                                                          │
│  Characteristics:                                        │
│  • Everything in one file, one scope                    │
│  • No functions, no classes                             │
│  • Code runs top to bottom                              │
│  • Variables accessible everywhere                      │
└─────────────────────────────────────────────────────────┘
```

### Single-Class OOP Version

```
┌─────────────────────────────────────────────────────────┐
│                  TicTacToeGame Class                     │
│                                                          │
│  Instance Variables (encapsulated):                     │
│  ├─ self.board                                          │
│  ├─ self.current_player                                │
│  ├─ self.game_over                                     │
│  ├─ self.winner                                        │
│  └─ self.moves_made                                    │
│                                                          │
│  Methods (organized behavior):                          │
│  ├─ __init__()           # Initialize game             │
│  ├─ display_board()      # Show board                  │
│  ├─ make_move()          # Process move                │
│  ├─ check_winner()       # Detect wins                 │
│  ├─ switch_player()      # Change turns                │
│  └─ play()               # Main game loop              │
│                                                          │
│  Characteristics:                                        │
│  • All game logic in one class                          │
│  • Data and behavior bundled together                   │
│  • Methods operate on self.data                         │
│  • Can create multiple game instances                   │
└─────────────────────────────────────────────────────────┘

Usage:
game = TicTacToeGame()  # Create instance
game.play()              # Run the game
```

### Multi-Class OOP Version

```
┌──────────────────────────────────────────────────────────┐
│                      Game Class                           │
│                   (Orchestrator)                          │
│                                                           │
│  Composed Objects:                                        │
│  ├─ self.board (Board instance)                          │
│  ├─ self.player_x (Player instance)                      │
│  └─ self.player_o (Player instance)                      │
│                                                           │
│  Responsibilities:                                        │
│  ├─ Coordinate gameplay                                  │
│  ├─ Manage turns                                         │
│  ├─ Handle user input                                    │
│  └─ Display messages                                     │
│                                                           │
│  Methods:                                                 │
│  ├─ __init__()                                           │
│  ├─ play()                                               │
│  ├─ switch_player()                                      │
│  ├─ get_player_input()                                   │
│  ├─ display_welcome()                                    │
│  └─ display_result()                                     │
└───────────┬──────────────────────┬──────────────────────┘
            │                      │
            │ HAS-A                │ HAS-A (2)
            ▼                      ▼
┌───────────────────────┐  ┌──────────────────────┐
│     Board Class       │  │    Player Class      │
│   (Grid Manager)      │  │   (Data Holder)      │
│                       │  │                      │
│  Data:                │  │  Data:               │
│  ├─ self.size         │  │  ├─ self.mark        │
│  └─ self.grid         │  │  └─ self.name        │
│                       │  │                      │
│  Responsibilities:    │  │  Responsibilities:   │
│  ├─ Manage grid       │  │  ├─ Store identity   │
│  ├─ Display board     │  │  └─ Provide info     │
│  ├─ Validate moves    │  │                      │
│  ├─ Place marks       │  │  Methods:            │
│  └─ Detect wins       │  │  ├─ get_mark()       │
│                       │  │  ├─ get_name()       │
│  Methods:             │  │  └─ __str__()        │
│  ├─ __init__()        │  │                      │
│  ├─ display()         │  │                      │
│  ├─ is_valid_move()   │  │                      │
│  ├─ place_mark()      │  │                      │
│  ├─ check_winner()    │  │                      │
│  └─ (private helpers) │  │                      │
└───────────────────────┘  └──────────────────────┘

Characteristics:
• Separated responsibilities across classes
• Composition: Game contains Board and Players
• Each class has one clear purpose
• Easy to test and extend independently
```

---

## Code Organization Comparison

### How Data is Stored

#### Procedural Version
```python
# Global variables - accessible everywhere
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
current_player = 'X'
game_over = False
winner = None

# Problem: Any code can modify these variables
# No protection or organization
```

#### Single-Class OOP
```python
class TicTacToeGame:
    def __init__(self):
        # Instance variables - belong to this object
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

# Benefit: Data is encapsulated in the object
# Each game instance has its own data
```

#### Multi-Class OOP
```python
class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = []  # Managed internally
        # Initialize grid...

class Player:
    def __init__(self, mark, name=None):
        self.mark = mark
        self.name = name or mark

class Game:
    def __init__(self, board_size=3):
        # Composition: Game contains other objects
        self.board = Board(board_size)
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.current_player = self.player_x

# Benefit: Responsibilities are separated
# Each class manages its own data
# Easy to modify one without affecting others
```

---

## How Operations are Performed

### Displaying the Board

#### Procedural Version
```python
# Inline code in the main loop
for i in range(3):
    for j in range(3):
        print(board[i][j], end=' | ')
    print()
    if i < 2:
        print("-" * 11)

# Problem: Code is repeated or scattered
# Hard to reuse or modify
```

#### Single-Class OOP
```python
class TicTacToeGame:
    def display_board(self):
        # Method encapsulates the logic
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' | ')
            print()
            if i < 2:
                print("-" * 11)

# Usage:
game.display_board()

# Benefit: Reusable, organized, clear
```

#### Multi-Class OOP
```python
class Board:
    def display(self):
        # Board is responsible for displaying itself
        for row in range(self.size):
            for col in range(self.size):
                cell = self.grid[row][col].ljust(2)
                print(f" {cell} ", end='')
                if col < self.size - 1:
                    print("|", end='')
            print()
            if row < self.size - 1:
                separator = "-" * (4 * self.size + (self.size - 1))
                print(separator)

# Usage:
game.board.display()

# Benefit: Board knows how to display itself
# Game doesn't need to know board internals
# Works with any board size automatically
```

---

## Data Flow Comparison

### Making a Move

#### Procedural Version
```
User Input
    ↓
Validate input (inline code)
    ↓
Check if position valid (inline code)
    ↓
Update global board variable
    ↓
Check winner (inline code)
    ↓
Update global current_player variable

Problem: Everything happens in one place
All logic is intertwined
```

#### Single-Class OOP
```
User Input
    ↓
game.make_move(position)
    ├─→ Validate using self._is_valid_move()
    ├─→ Update self.board
    ├─→ Check winner using self.check_winner()
    └─→ Switch player using self._switch_player()

Benefit: Logic is organized into methods
Clear flow through method calls
```

#### Multi-Class OOP
```
User Input
    ↓
game.get_player_input()
    ↓
game.board.is_valid_move(coord)
    ├─→ Board validates internally
    └─→ Returns True/False
    ↓
game.board.place_mark(coord, mark)
    ├─→ Board updates its own grid
    └─→ Returns success
    ↓
game.board.check_winner()
    ├─→ Board checks its own grid
    └─→ Returns winner or None
    ↓
game.switch_player()
    └─→ Game manages player turns

Benefit: Each class handles its own responsibility
Clear separation of concerns
Easy to test each component independently
```

---

## Scalability Comparison

### Changing Board Size

#### Procedural Version
```python
# Hardcoded for 3x3
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# To change to 4x4, you must modify:
# - Board initialization
# - Display code (loop ranges)
# - Win detection (hardcoded checks)
# - Position validation
# - Many other places

# Difficulty: HIGH - requires changes throughout the code
```

#### Single-Class OOP
```python
class TicTacToeGame:
    def __init__(self):
        # Still hardcoded for 3x3
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.board_size = 3

# To change to 4x4:
# - Modify initialization
# - Update display method
# - Update win detection
# - Several methods need changes

# Difficulty: MEDIUM - changes localized to one class
```

#### Multi-Class OOP
```python
# Configuration constant
BOARD_SIZE = 3  # Change this ONE value

class Board:
    def __init__(self, size=3):
        self.size = size
        # Everything adapts automatically
        self.grid = [[f"{r}{c}" for c in range(size)] 
                     for r in range(size)]

# To change to 4x4:
# - Change BOARD_SIZE = 4
# - That's it! Everything adapts automatically

# Difficulty: VERY LOW - one constant change
```

---

## Complexity vs Capability Matrix

```
                    Procedural    Single-Class    Multi-Class
                    ─────────────────────────────────────────
Lines of Code       ~200          ~250            ~300
Number of Classes   0             1               3
Complexity          Low           Medium          High
Reusability         Low           Medium          High
Testability         Low           Medium          High
Maintainability     Low           Medium          High
Extensibility       Low           Medium          Very High
Scalability         Low           Low             High
Best For            Learning      Small projects  Production
```

---

## When to Use Each Approach

### Use Procedural (No Classes) When:
✅ You're just learning programming basics
✅ The program is very small (< 100 lines)
✅ It's a one-time script
✅ You need something quick and simple
✅ You're practicing loops and conditionals

❌ Don't use when:
- The program will grow larger
- You need to reuse code
- Multiple people will work on it
- You need to test components independently

### Use Single-Class OOP When:
✅ You've learned OOP basics
✅ The program has related data and behavior
✅ You want better organization than procedural
✅ You need multiple instances
✅ The problem fits naturally into one entity

❌ Don't use when:
- The class becomes too large (> 500 lines)
- Responsibilities are mixed
- You need high flexibility
- The system has multiple distinct components

### Use Multi-Class OOP When:
✅ The system has multiple distinct responsibilities
✅ You need high flexibility and extensibility
✅ Multiple developers will work on different parts
✅ You need to test components independently
✅ The system will grow and evolve
✅ You want production-quality architecture

❌ Don't use when:
- The problem is very simple
- You're just learning OOP basics
- Over-engineering would slow development

---

## Real-World Analogy

### Procedural: Cooking Without a Recipe
- All ingredients on the counter
- Do everything step by step
- No organization or structure
- Works for simple meals
- Hard to repeat or scale

### Single-Class OOP: Recipe Card
- Ingredients list (data)
- Instructions (methods)
- Everything for one dish in one place
- Easy to follow and repeat
- Good for standard recipes

### Multi-Class OOP: Professional Kitchen
- Prep station (Board class)
- Cooking station (Game class)
- Plating station (Player class)
- Each station has specific responsibilities
- Stations work together
- Easy to modify one without affecting others
- Scales to complex meals

---

## Evolution Path

```
┌─────────────────┐
│   Procedural    │  Start here: Learn basics
│   (Week 3)      │  • Variables, loops, conditionals
└────────┬────────┘  • Linear thinking
         │           • Simple problems
         ▼
┌─────────────────┐
│ Single-Class    │  Next step: Learn OOP
│ OOP             │  • Classes and objects
└────────┬────────┘  • Methods and self
         │           • Encapsulation
         ▼
┌─────────────────┐
│ Multi-Class     │  Advanced: Learn architecture
│ OOP             │  • Separation of concerns
└─────────────────┘  • Composition
                     • Design patterns
                     • Scalable systems
```

---

## Key Takeaways

### Procedural Programming
**Strength**: Simple, direct, easy to understand
**Weakness**: Doesn't scale, hard to maintain
**Best for**: Learning, small scripts

### Single-Class OOP
**Strength**: Organized, reusable, better than procedural
**Weakness**: Can become bloated, limited flexibility
**Best for**: Medium projects, learning OOP

### Multi-Class OOP
**Strength**: Flexible, maintainable, professional
**Weakness**: More complex initially, requires planning
**Best for**: Large projects, production code, teams

---

## Conclusion

All three approaches solve the same problem, but they represent different levels of software engineering maturity:

1. **Procedural**: Gets the job done, good for learning
2. **Single-Class OOP**: Better organization, good for practice
3. **Multi-Class OOP**: Professional architecture, good for real projects

The best approach depends on:
- Your skill level
- Project size and complexity
- Whether the code will be maintained
- Whether it needs to scale or extend

Start with procedural to learn basics, move to single-class OOP to learn object-oriented thinking, and use multi-class OOP when you're ready for professional software architecture.
