"""
Tic-Tac-Toe Game - Dictionary Version

This file demonstrates how to create a tic-tac-toe game using a dictionary
to represent the game board. This version is designed for week 3 Python
learners who are just learning about dictionaries and key-value pairs.

Key concepts demonstrated:
- Dictionaries with numeric keys
- Dictionary key access with [key]
- Direct position mapping (no coordinate conversion needed)
- Dictionary iteration and checking
- Key-value pair relationships
- Comparing dictionary approach vs nested lists approach

Educational Focus:
This code shows how the same problem can be solved using a different
data structure. By comparing this with the nested lists version, students
can see the advantages and trade-offs of each approach.

Author: Educational Tic-Tac-Toe Project
Date: 2024
Python Level: Beginner (Week 3)
Data Structure: Dictionary
"""

# ============================================
# GAME SETUP AND INITIALIZATION
# ============================================
# This section sets up all the variables we need for the game
# We create the board and set the starting conditions

print("Welcome to Tic-Tac-Toe - Dictionary Version!")
print("This version uses a dictionary to store the game board.")
print("You'll see how we use keys (1-9) to directly access positions.")
print()

# board: This is a dictionary with number keys (1-9) and string values
# Keys represent board positions, values are either numbers or X/O
# This is different from the nested lists version - no row/column math needed!
board = {
    1: '1', 2: '2', 3: '3',  # Top row: positions 1, 2, 3
    4: '4', 5: '5', 6: '6',  # Middle row: positions 4, 5, 6
    7: '7', 8: '8', 9: '9'   # Bottom row: positions 7, 8, 9
}

# current_player: A string that holds either 'X' or 'O'
# This tells us whose turn it is to play
# We start with 'X' because X always goes first in tic-tac-toe
# (This is identical to the nested lists version)
current_player = 'X'

# game_over: A boolean (True or False) that tracks if the game has ended
# We start with False because the game just began
# This becomes True when someone wins or the board is full (tie)
# (This is identical to the nested lists version)
game_over = False

# winner: A string that will hold 'X', 'O', or 'Tie' when the game ends
# We start with an empty string because no one has won yet
# (This is identical to the nested lists version)
winner = ''

# moves_made: An integer that counts how many moves have been made
# We use this to detect tie games (when moves_made reaches 9)
# (This is identical to the nested lists version)
moves_made = 0

print("Game setup complete! Here's how the dictionary works:")
print("board =", board)
print()
print("To access a specific position, we use board[key]:")
print("board[1] =", board[1], "← Position 1 (top-left)")
print("board[5] =", board[5], "← Position 5 (center)")
print("board[9] =", board[9], "← Position 9 (bottom-right)")
print()
print("Notice: No row/column conversion needed! Position number IS the key!")
print()
print("Let's start playing!")
print()

# ============================================
# BOARD DISPLAY SECTION
# ============================================
# This section contains code to show the current game board
# It formats the board nicely so players can see the game state
# COMPARISON: Notice how different this is from the nested lists version!

# Display the current board using direct dictionary access
# This is much simpler than nested loops - we just access each position directly!

print("Current board:")
print()

# DICTIONARY APPROACH: Access positions directly by their keys
# Compare this to the nested lists version that needed loops and [row][col] indexing

# Top row: positions 1, 2, 3
print(" " + board[1] + " | " + board[2] + " | " + board[3])
print("-----------")

# Middle row: positions 4, 5, 6  
print(" " + board[4] + " | " + board[5] + " | " + board[6])
print("-----------")

# Bottom row: positions 7, 8, 9
print(" " + board[7] + " | " + board[8] + " | " + board[9])

print()

# EDUCATIONAL NOTE: Compare this approach with nested lists
print("Dictionary vs Nested Lists comparison:")
print("- Dictionary: board[1], board[2], board[3] (direct access)")
print("- Nested Lists: board[0][0], board[0][1], board[0][2] (row/column)")
print("- Dictionary: No loops needed for display")
print("- Nested Lists: Needed nested for loops")
print("- Dictionary: Position number IS the key")
print("- Nested Lists: Need math to convert position to row/column")
print()

# ============================================
# MAIN GAME LOOP - Keep playing until game ends
# ============================================
# This section contains the main game logic that repeats until someone wins

# Start the main game loop - this will keep running until game_over becomes True
while not game_over:
    
    # ============================================
    # INPUT VALIDATION AND PROCESSING SECTION
    # ============================================
    # This section handles getting input from players
    # COMPARISON: Much simpler than nested lists - no coordinate conversion!
    
    # valid_move: A boolean that tracks whether the player's move is acceptable
    # We start with False and only set it to True if all checks pass
    # (This is identical to the nested lists version)
    valid_move = False
    
    # Keep asking for input until we get a valid move
    # This while loop will repeat until valid_move becomes True
    while not valid_move:
        
        # Get input from the current player
        # f-strings let us put variables directly into strings
        # (This is identical to the nested lists version)
        player_input = input(f"Player {current_player}, enter position (1-9): ")
        
        # INPUT VALIDATION STEP 1: Check if input can be converted to a number
        # We use try/except to catch errors if they enter letters or symbols
        # (This is identical to the nested lists version)
        try:
            # int() converts the string input to an integer (whole number)
            # If the player typed letters, this will cause an error
            position = int(player_input)
            
            # INPUT VALIDATION STEP 2: Check if the number is in valid range
            # Valid positions are 1, 2, 3, 4, 5, 6, 7, 8, 9
            # (This is identical to the nested lists version)
            if position >= 1 and position <= 9:
                
                # DICTIONARY ADVANTAGE: No coordinate conversion needed!
                # Compare this to nested lists version that needed:
                # row = (position - 1) // 3
                # col = (position - 1) % 3
                
                print(f"Position {position} - checking dictionary key {position}")
                
                # INPUT VALIDATION STEP 3: Check if the position is empty
                # DICTIONARY APPROACH: Direct key access - much simpler!
                # A position is empty if it still contains its original number
                # If it contains 'X' or 'O', then it's already taken
                if board[position] not in ['X', 'O']:
                    # Position is empty! We can make this move
                    valid_move = True
                    print(f"Valid move! Placing {current_player} at position {position}")
                else:
                    # Position is already taken
                    print(f"Position {position} is already taken by {board[position]}. Choose an empty position.")
                    
            else:
                # The number is outside our valid range (less than 1 or greater than 9)
                print("Please enter a number between 1 and 9")
                
        except:
            # This runs if int() failed because they entered non-numbers
            print("Please enter a number, not letters or symbols")
    
    # MAKE THE MOVE: Update the board with the player's choice
    # DICTIONARY ADVANTAGE: Direct assignment - no row/column needed!
    # Compare to nested lists: board[row][col] = current_player
    board[position] = current_player
    moves_made = moves_made + 1  # Keep track of how many moves have been made
    
    print(f"Move made! {current_player} placed at position {position}")
    print()
    
    # DISPLAY UPDATED BOARD: Show the board after the move
    print("Updated board:")
    print()
    
    # Display the board again using direct dictionary access
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    
    print()
    
    # ============================================
    # WIN DETECTION SECTION
    # ============================================
    # This section checks if someone has won the game
    # COMPARISON: Different approach than nested lists - we specify exact positions
    
    # CHECK FOR ROW WINS (horizontal lines)
    # DICTIONARY APPROACH: We explicitly check each winning combination
    # Compare to nested lists that used loops - this is more explicit but longer
    
    # Top row: positions 1, 2, 3
    if (board[1] == board[2] == board[3] and 
        board[1] in ['X', 'O']):
        winner = board[1]
        game_over = True
        print(f"Top row win! Player {winner} wins!")
    
    # Middle row: positions 4, 5, 6
    elif (board[4] == board[5] == board[6] and 
          board[4] in ['X', 'O']):
        winner = board[4]
        game_over = True
        print(f"Middle row win! Player {winner} wins!")
    
    # Bottom row: positions 7, 8, 9
    elif (board[7] == board[8] == board[9] and 
          board[7] in ['X', 'O']):
        winner = board[7]
        game_over = True
        print(f"Bottom row win! Player {winner} wins!")
    
    # CHECK FOR COLUMN WINS (vertical lines)
    # Left column: positions 1, 4, 7
    elif (board[1] == board[4] == board[7] and 
          board[1] in ['X', 'O']):
        winner = board[1]
        game_over = True
        print(f"Left column win! Player {winner} wins!")
    
    # Middle column: positions 2, 5, 8
    elif (board[2] == board[5] == board[8] and 
          board[2] in ['X', 'O']):
        winner = board[2]
        game_over = True
        print(f"Middle column win! Player {winner} wins!")
    
    # Right column: positions 3, 6, 9
    elif (board[3] == board[6] == board[9] and 
          board[3] in ['X', 'O']):
        winner = board[3]
        game_over = True
        print(f"Right column win! Player {winner} wins!")
    
    # CHECK FOR DIAGONAL WINS
    # Main diagonal: positions 1, 5, 9 (top-left to bottom-right)
    elif (board[1] == board[5] == board[9] and 
          board[1] in ['X', 'O']):
        winner = board[1]
        game_over = True
        print(f"Main diagonal win! Player {winner} wins!")
    
    # Anti-diagonal: positions 3, 5, 7 (top-right to bottom-left)
    elif (board[3] == board[5] == board[7] and 
          board[3] in ['X', 'O']):
        winner = board[3]
        game_over = True
        print(f"Anti-diagonal win! Player {winner} wins!")
    
    # CHECK FOR TIE GAME
    # If no one has won and all 9 positions are filled, it's a tie
    elif moves_made == 9:
        winner = 'Tie'
        game_over = True
        print("All positions filled - it's a tie game!")
    
    # SWITCH PLAYERS (only if game is not over)
    # After each move, we need to switch to the other player
    # (This is identical to the nested lists version)
    if not game_over:
        if current_player == 'X':
            current_player = 'O'  # Switch from X to O
        else:
            current_player = 'X'  # Switch from O to X
        
        print(f"Next turn: Player {current_player}")
        print()

# ============================================
# GAME END SECTION
# ============================================
# This section runs after the game loop ends
# It displays the final results
# (This is identical to the nested lists version)

print()
print("=" * 30)
print("GAME OVER!")
print("=" * 30)

if winner == 'Tie':
    print("The game ended in a tie!")
    print("Both players played well!")
else:
    print(f"Congratulations! Player {winner} wins!")
    print(f"Player {winner} got three in a row!")

print()
print("Final board:")
print()

# Display the final board one more time using dictionary access
print(" " + board[1] + " | " + board[2] + " | " + board[3])
print("-----------")
print(" " + board[4] + " | " + board[5] + " | " + board[6])
print("-----------")
print(" " + board[7] + " | " + board[8] + " | " + board[9])

print()
print("Thanks for playing Tic-Tac-Toe!")
print("This was the dictionary version - compare it with the nested lists version!")
print()
print("DICTIONARY vs NESTED LISTS SUMMARY:")
print("Dictionary advantages:")
print("- Direct position access (no math needed)")
print("- Simple move processing")
print("- Intuitive key-value mapping")
print()
print("Nested Lists advantages:")
print("- Systematic win checking with loops")
print("- Natural 2D representation")
print("- Easier to scale to larger boards")
print()
print("Both approaches solve the same problem - choose what makes sense for your situation!")