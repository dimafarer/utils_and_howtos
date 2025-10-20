# Exercises and Extensions

## Introduction

This document provides hands-on exercises to help you practice and extend your understanding of the tic-tac-toe project. The exercises are organized by difficulty level, starting with simple modifications and building up to more complex features.

Each exercise includes:
- Clear instructions on what to implement
- Step-by-step hints to guide you
- Learning objectives for each task
- Solutions and explanations

## Getting Started

Before attempting these exercises:
1. Make sure you can run both game versions successfully
2. Read through the code and understand the basic structure
3. Try playing a few games to understand the user experience
4. Keep the documentation files handy for reference

## Beginner Exercises

These exercises focus on simple modifications that reinforce basic Python concepts.

### Exercise 1: Change the Starting Player

**Objective**: Modify the game so that 'O' goes first instead of 'X'

**What you'll learn**: Variable initialization and game flow

**Instructions**:
1. Open either `tictactoe_lists.py` or `tictactoe_dict.py`
2. Find where `current_player` is first set
3. Change it from 'X' to 'O'
4. Test your change by running the game

**Hints**:
- Look for the line that says `current_player = 'X'`
- This should be in the game setup section
- Make sure to update any welcome messages that mention X going first

**Expected result**: The game should now prompt "Player O, enter position (1-9):" for the first move

**Solution**:
```python
# Change this line:
current_player = 'X'
# To this:
current_player = 'O'

# Also update any messages like:
print("We start with 'O' because O goes first in this version")
```

**Extension**: Make it random who goes first each game

---

### Exercise 2: Add a Move Counter

**Objective**: Keep track of how many moves have been made and display it

**What you'll learn**: Variable tracking and string formatting

**Instructions**:
1. The game already has a `moves_made` variable
2. Display the current move number before each player's turn
3. Show the total moves at the end of the game

**Hints**:
- Find where `moves_made` is incremented
- Add a print statement before asking for player input
- Use f-strings to format the message nicely

**Expected result**: 
```
Move #1: Player X, enter position (1-9):
Move #2: Player O, enter position (1-9):
...
Game completed in 7 moves!
```

**Solution**:
```python
# Before asking for input, add:
print(f"Move #{moves_made + 1}: Player {current_player}, enter position (1-9): ", end="")
player_input = input()

# At game end, add:
print(f"Game completed in {moves_made} moves!")
```

---

### Exercise 3: Customize Welcome Messages

**Objective**: Personalize the game with custom messages and formatting

**What you'll learn**: String manipulation and user interface design

**Instructions**:
1. Change the welcome message to something more creative
2. Add your name as the game creator
3. Use ASCII art or special characters to make it look nice
4. Add a brief explanation of the rules

**Hints**:
- Look for the print statements at the beginning of the game
- You can use `*`, `=`, `-` characters to create borders
- Keep messages beginner-friendly

**Expected result**: A personalized, attractive welcome screen

**Solution**:
```python
print("🎮" * 20)
print("   SUPER TIC-TAC-TOE CHALLENGE")
print("   Created by: [Your Name]")
print("🎮" * 20)
print()
print("RULES:")
print("- Get 3 in a row to win (horizontal, vertical, or diagonal)")
print("- Enter numbers 1-9 to place your mark")
print("- Have fun and learn Python!")
print()
```

---

### Exercise 4: Add Color or Formatting

**Objective**: Make the game more visually appealing with simple formatting

**What you'll learn**: String formatting and terminal output

**Instructions**:
1. Make X and O appear differently (you can use brackets, stars, etc.)
2. Add spacing or borders to make the board clearer
3. Use UPPERCASE or lowercase for different effects

**Hints**:
- Instead of just 'X', you could use '[X]' or '*X*'
- You can add extra spaces around the board
- Be consistent with your formatting choices

**Expected result**: A more visually distinct game board

**Solution**:
```python
# When displaying the board, modify the output:
# Instead of just printing board[i][j], use:
if board[i][j] == 'X':
    print('[X]', end='')
elif board[i][j] == 'O':
    print('(O)', end='')
else:
    print(f' {board[i][j]} ', end='')
```

---

### Exercise 5: Add Input Hints

**Objective**: Help players by showing which positions are still available

**What you'll learn**: List/dictionary iteration and conditional logic

**Instructions**:
1. Before each turn, show which positions are still empty
2. Display them in a helpful format
3. Update the list as positions are taken

**Hints**:
- Loop through the board to find empty positions
- Empty positions still contain their number ('1', '2', etc.)
- Display them in a user-friendly way

**Expected result**:
```
Available positions: 1, 3, 4, 6, 7, 9
Player X, enter position (1-9):
```

**Solution for Lists Version**:
```python
# Before asking for input:
available = []
for i in range(3):
    for j in range(3):
        if board[i][j] not in ['X', 'O']:
            available.append(board[i][j])

print(f"Available positions: {', '.join(available)}")
```

**Solution for Dictionary Version**:
```python
# Before asking for input:
available = []
for position in range(1, 10):
    if board[position] not in ['X', 'O']:
        available.append(str(position))

print(f"Available positions: {', '.join(available)}")
```

---

### Exercise 6: Improve Error Messages

**Objective**: Make error messages more helpful and specific

**What you'll learn**: Error handling and user experience design

**Instructions**:
1. Give different messages for different types of errors
2. Provide specific guidance on how to fix each error
3. Make messages encouraging, not frustrating

**Current error types**:
- Invalid number format (letters/symbols)
- Number out of range (0, 10, etc.)
- Position already taken

**Hints**:
- Look at the try/except blocks and if statements
- Think about what would help you if you were learning
- Use positive language ("Please try..." instead of "Error!")

**Expected result**: More helpful, specific error messages

**Solution**:
```python
# Instead of generic messages, use specific ones:
except:
    print("Oops! That's not a number. Please enter a digit from 1 to 9.")
    print("For example: 5 (for the center position)")

# For out of range:
if position < 1:
    print(f"Position {position} is too low. The lowest position is 1 (top-left).")
elif position > 9:
    print(f"Position {position} is too high. The highest position is 9 (bottom-right).")

# For taken positions:
print(f"Position {position} already has {board[row][col]}. Try one of these instead:")
# Then show available positions
```

## Practice Challenges

### Challenge A: Play Multiple Games
Modify the code to automatically restart after each game without needing to run the program again.

### Challenge B: Keep Score
Track wins for each player across multiple games and display a scoreboard.

### Challenge C: Add Sound Effects
Use print statements to simulate sound effects (like "BEEP!" for invalid moves).

### Challenge D: Create a Tournament Mode
Allow players to enter their names and play a best-of-3 or best-of-5 series.

## Tips for Success

1. **Start Small**: Make one small change at a time and test it
2. **Read the Comments**: The existing code has extensive explanations
3. **Test Everything**: Try different inputs to make sure your changes work
4. **Don't Break the Original**: Keep a backup copy before making changes
5. **Ask Questions**: If you get stuck, review the documentation files

## Common Mistakes to Avoid

1. **Forgetting to Test**: Always run your code after making changes
2. **Changing Too Much**: Make one modification at a time
3. **Ignoring Error Messages**: Read them carefully - they tell you what's wrong
4. **Not Understanding the Original**: Make sure you understand how the code works before changing it

## Next Steps

Once you've completed these beginner exercises, you're ready for the intermediate and advanced challenges in the next section!

Remember: The goal is to learn and have fun. Don't worry if something doesn't work the first time - debugging is part of programming!
## 
Intermediate Exercises

These exercises require more complex logic and introduce new programming concepts while still avoiding functions and classes.

### Exercise 7: Smart Input Validation

**Objective**: Create more robust input handling that accepts different formats

**What you'll learn**: String processing, multiple validation methods, user experience

**Instructions**:
1. Accept both numbers and words (e.g., "center" for position 5)
2. Handle extra spaces and different cases
3. Allow "quit" or "exit" to end the game early

**Implementation Guide**:
```python
# Create a mapping for word inputs
position_words = {
    'center': 5, 'middle': 5,
    'top-left': 1, 'top-right': 3,
    'bottom-left': 7, 'bottom-right': 9,
    'top': 2, 'bottom': 8, 'left': 4, 'right': 6
}

# In your input processing:
player_input = input(f"Player {current_player}, enter position: ").strip().lower()

if player_input in ['quit', 'exit', 'q']:
    print("Thanks for playing!")
    game_over = True
    continue

# Check if it's a word first
if player_input in position_words:
    position = position_words[player_input]
else:
    # Try to convert to number
    try:
        position = int(player_input)
    except:
        print("Please enter a number (1-9) or a position word like 'center'")
        continue
```

**Learning objectives**: String manipulation, dictionaries for mapping, user-friendly interfaces

---

### Exercise 8: Game Statistics Tracking

**Objective**: Keep detailed statistics about the game session

**What you'll learn**: Data collection, calculations, formatted output

**Instructions**:
1. Track total games played, wins for each player, and ties
2. Calculate win percentages
3. Track average game length (number of moves)
4. Display statistics at the end of each game

**Implementation Guide**:
```python
# Add these variables at the start:
total_games = 0
x_wins = 0
o_wins = 0
ties = 0
total_moves = 0

# After each game:
total_games += 1
total_moves += moves_made

if winner == 'X':
    x_wins += 1
elif winner == 'O':
    o_wins += 1
else:
    ties += 1

# Display statistics:
print("\n" + "=" * 40)
print("SESSION STATISTICS")
print("=" * 40)
print(f"Games played: {total_games}")
print(f"X wins: {x_wins} ({x_wins/total_games*100:.1f}%)")
print(f"O wins: {o_wins} ({o_wins/total_games*100:.1f}%)")
print(f"Ties: {ties} ({ties/total_games*100:.1f}%)")
print(f"Average game length: {total_moves/total_games:.1f} moves")
```

**Learning objectives**: Mathematical calculations, percentage formatting, data analysis

---

### Exercise 9: Enhanced Board Display Options

**Objective**: Create multiple ways to display the game board

**What you'll learn**: Conditional formatting, user preferences, visual design

**Instructions**:
1. Add a setting to choose between different board styles
2. Create at least 3 different visual styles
3. Allow users to change the style during the game

**Implementation Guide**:
```python
# Add at game start:
print("Choose board style:")
print("1. Classic ( X | O | 3 )")
print("2. Fancy  [X] (O) [3]")
print("3. Minimal X O 3")

board_style = input("Enter style (1-3): ")

# Create display function for each style:
def display_classic():
    # Original format with | separators
    
def display_fancy():
    # Use brackets and parentheses
    
def display_minimal():
    # Just spaces between positions

# In your display code:
if board_style == '1':
    display_classic()
elif board_style == '2':
    display_fancy()
else:
    display_minimal()
```

**Learning objectives**: Code organization, user preferences, visual design principles

---

### Exercise 10: Undo Last Move

**Objective**: Allow players to undo their last move

**What you'll learn**: State management, data restoration, game flow control

**Instructions**:
1. Keep track of the last move made
2. Allow typing "undo" to reverse the last move
3. Handle edge cases (can't undo first move, can't undo twice in a row)

**Implementation Guide**:
```python
# Add tracking variables:
last_position = None
last_player = None
can_undo = False

# After making a move:
last_position = position  # or (row, col) for lists version
last_player = current_player
can_undo = True

# In input processing:
if player_input.lower() == 'undo':
    if can_undo and last_position is not None:
        # Restore the board
        board[last_position] = str(last_position)  # Dictionary version
        # or board[row][col] = str(last_position) for lists version
        
        # Switch back to previous player
        current_player = last_player
        moves_made -= 1
        can_undo = False
        print(f"Move undone! Back to Player {current_player}")
    else:
        print("Cannot undo right now")
    continue
```

**Learning objectives**: State management, conditional logic, user experience design

---

## Advanced Extensions

These exercises introduce more complex programming concepts and larger feature additions.

### Exercise 11: Simple Computer Player

**Objective**: Create a computer opponent with basic strategy

**What you'll learn**: AI logic, decision making, game strategy

**Instructions**:
1. Add an option to play against the computer
2. Implement basic strategy: win if possible, block opponent wins, otherwise random
3. Add difficulty levels (easy = random, medium = basic strategy)

**Implementation Guide**:
```python
# Add game mode selection:
game_mode = input("Play against (1) Human or (2) Computer? ")

# Computer move logic:
def computer_move():
    # Strategy 1: Win if possible
    for pos in range(1, 10):  # Dictionary version
        if board[pos] not in ['X', 'O']:
            board[pos] = 'O'  # Try the move
            if check_win_for_player('O'):
                return pos  # Winning move found
            board[pos] = str(pos)  # Undo test move
    
    # Strategy 2: Block opponent win
    for pos in range(1, 10):
        if board[pos] not in ['X', 'O']:
            board[pos] = 'X'  # Try opponent move
            if check_win_for_player('X'):
                board[pos] = 'O'  # Block it
                return pos
            board[pos] = str(pos)  # Undo test move
    
    # Strategy 3: Random available move
    available = [pos for pos in range(1, 10) if board[pos] not in ['X', 'O']]
    import random
    return random.choice(available)

# In game loop:
if current_player == 'O' and game_mode == '2':
    position = computer_move()
    print(f"Computer chooses position {position}")
else:
    # Human player input
```

**Learning objectives**: Basic AI concepts, game strategy, decision trees

---

### Exercise 12: Tournament Mode

**Objective**: Create a tournament system with multiple games and scoring

**What you'll learn**: Complex game flow, data structures, tournament logic

**Instructions**:
1. Allow players to enter their names
2. Play best-of-3, best-of-5, or best-of-7 series
3. Track series wins and display bracket-style results

**Implementation Guide**:
```python
# Tournament setup:
player1_name = input("Enter Player 1 name: ")
player2_name = input("Enter Player 2 name: ")
series_length = int(input("Best of how many games? (3, 5, or 7): "))

wins_needed = (series_length + 1) // 2
player1_wins = 0
player2_wins = 0
game_number = 1

# Tournament loop:
while player1_wins < wins_needed and player2_wins < wins_needed:
    print(f"\n{'='*50}")
    print(f"GAME {game_number} - {player1_name} vs {player2_name}")
    print(f"Series: {player1_name} {player1_wins} - {player2_wins} {player2_name}")
    print(f"{'='*50}")
    
    # Play one game (your existing game code here)
    
    # Update series score
    if winner == 'X':
        player1_wins += 1
    elif winner == 'O':
        player2_wins += 1
    
    game_number += 1

# Tournament results:
series_winner = player1_name if player1_wins > player2_wins else player2_name
print(f"\n🏆 TOURNAMENT CHAMPION: {series_winner}! 🏆")
```

**Learning objectives**: Complex program flow, user data management, competitive gaming concepts

---

### Exercise 13: Larger Board Sizes

**Objective**: Modify the game to work with 4x4 or 5x5 boards

**What you'll learn**: Scalable code design, dynamic data structures, algorithm adaptation

**Instructions**:
1. Ask user to choose board size (3x3, 4x4, or 5x5)
2. Adjust win conditions (4 in a row for 4x4, 5 in a row for 5x5)
3. Update display and input validation accordingly

**Implementation Guide**:
```python
# Board size selection:
board_size = int(input("Choose board size (3, 4, or 5): "))
win_length = board_size  # Need this many in a row to win

# Dynamic board creation (dictionary version):
board = {}
position = 1
for row in range(board_size):
    for col in range(board_size):
        board[position] = str(position)
        position += 1

# Dynamic display:
for row in range(board_size):
    for col in range(board_size):
        pos = row * board_size + col + 1
        print(f" {board[pos]} ", end="")
        if col < board_size - 1:
            print("|", end="")
    print()
    if row < board_size - 1:
        print("-" * (board_size * 4 - 1))

# Dynamic win checking:
# Check rows
for row in range(board_size):
    for start_col in range(board_size - win_length + 1):
        positions = [row * board_size + start_col + col + 1 for col in range(win_length)]
        if all(board[pos] == board[positions[0]] and board[pos] in ['X', 'O'] for pos in positions):
            # Win found!
```

**Learning objectives**: Dynamic programming, scalable algorithms, mathematical patterns

---

### Exercise 14: Save and Load Games

**Objective**: Allow players to save their game and continue later

**What you'll learn**: File operations, data serialization, program state management

**Instructions**:
1. Add option to save game state to a file
2. Add option to load a previously saved game
3. Handle file errors gracefully

**Implementation Guide**:
```python
# Save game function:
def save_game():
    filename = input("Enter filename to save: ") + ".txt"
    try:
        with open(filename, 'w') as file:
            # Save board state
            for pos in range(1, 10):
                file.write(f"{pos}:{board[pos]}\n")
            # Save game state
            file.write(f"current_player:{current_player}\n")
            file.write(f"moves_made:{moves_made}\n")
        print(f"Game saved as {filename}")
    except:
        print("Error saving game")

# Load game function:
def load_game():
    filename = input("Enter filename to load: ") + ".txt"
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                if key.isdigit():
                    board[int(key)] = value
                elif key == 'current_player':
                    current_player = value
                elif key == 'moves_made':
                    moves_made = int(value)
        print("Game loaded successfully!")
        return True
    except:
        print("Error loading game or file not found")
        return False

# In main menu:
choice = input("(N)ew game, (L)oad game, or (Q)uit? ").upper()
if choice == 'L':
    if not load_game():
        # Start new game if load failed
```

**Learning objectives**: File I/O operations, error handling, data persistence

---

### Exercise 15: Network Play (Advanced)

**Objective**: Allow two players to play over a network connection

**What you'll learn**: Network programming basics, client-server architecture

**Note**: This is quite advanced and may require additional Python libraries

**Instructions**:
1. Create a simple server that manages the game state
2. Create a client that connects to the server
3. Allow moves to be sent between players

**Implementation Concept**:
```python
# This is a conceptual example - actual implementation is complex
import socket

# Server side (simplified):
server = socket.socket()
server.bind(('localhost', 12345))
server.listen(2)

player1, addr1 = server.accept()
player2, addr2 = server.accept()

# Game loop with network communication
while not game_over:
    # Send board state to both players
    # Receive move from current player
    # Validate and apply move
    # Check for win
    # Switch players

# Client side (simplified):
client = socket.socket()
client.connect(('localhost', 12345))

# Receive board updates and send moves
```

**Learning objectives**: Network concepts, client-server programming, distributed systems

---

## Project Extensions

### Extension A: Create a GUI Version
Use a library like `tkinter` to create a graphical interface with clickable buttons.

### Extension B: Add Animations
Create simple text-based animations for moves, wins, and transitions.

### Extension C: Multiple Game Modes
Implement variations like "Reverse Tic-Tac-Toe" (try to lose) or "Quantum Tic-Tac-Toe" (positions can be in multiple states).

### Extension D: AI with Machine Learning
Implement a learning AI that gets better over time by analyzing past games.

## Tips for Advanced Exercises

1. **Plan Before Coding**: Write out your approach before starting
2. **Break Down Complex Problems**: Divide large features into smaller parts
3. **Test Incrementally**: Make sure each part works before adding the next
4. **Handle Edge Cases**: Think about what could go wrong and plan for it
5. **Keep It Educational**: Remember that the goal is learning, not just building features

## Debugging Advanced Features

1. **Use Print Statements**: Add temporary print statements to see what's happening
2. **Test with Simple Cases**: Start with the easiest scenario first
3. **Check Your Logic**: Walk through your code step by step
4. **Ask for Help**: Don't be afraid to seek assistance when stuck

## Conclusion

These exercises progress from simple modifications to complex features that could be found in professional games. Each one teaches important programming concepts while building on the foundation of the tic-tac-toe game.

Remember:
- Start with exercises that match your current skill level
- Don't try to do everything at once
- Focus on understanding, not just getting it to work
- Have fun and be creative with your implementations!

The most important thing is to keep learning and experimenting. Every programmer started with simple exercises like these, and each challenge you complete makes you a better developer.

Happy coding! 🚀