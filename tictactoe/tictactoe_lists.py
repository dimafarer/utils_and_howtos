"""
Tic-Tac-Toe Game - Nested Lists Version

This file demonstrates how to create a tic-tac-toe game using nested lists
to represent the game board. This version is designed for week 3 Python
learners who are just learning about lists, loops, and conditionals.

Key concepts demonstrated:
- Nested lists (lists inside lists)
- For loops with range()
- Nested for loops
- List indexing with [row][column]
- Input validation with try/except
- While loops for game control
- Converting position numbers to row/column coordinates

Educational Focus:
This code prioritizes clarity and learning over efficiency. Every line
is extensively commented to help beginners understand not just what the
code does, but why it works that way.

Author: Educational Tic-Tac-Toe Project
Date: 2024
Python Level: Beginner (Week 3)
Data Structure: Nested Lists
"""

# ============================================
# GAME SETUP AND INITIALIZATION
# ============================================
# This section sets up all the variables we need for the game
# We create the board and set the starting conditions

print("Welcome to Tic-Tac-Toe - Nested Lists Version!")
print("This version uses nested lists to store the game board.")
print("You'll see how we use [row][column] indexing to access positions.")
print()

# board: This is a list that contains 3 other lists (nested list)
# Each inner list represents one row of the tic-tac-toe board
# The values start as strings '1' through '9' to show position numbers
# When players make moves, we replace these with 'X' or 'O'
board = [
    ['1', '2', '3'],  # Row 0: positions 1, 2, 3 (top row)
    ['4', '5', '6'],  # Row 1: positions 4, 5, 6 (middle row)  
    ['7', '8', '9']   # Row 2: positions 7, 8, 9 (bottom row)
]

# current_player: A string that holds either 'X' or 'O'
# This tells us whose turn it is to play
# We start with 'X' because X always goes first in tic-tac-toe
current_player = 'X'

# game_over: A boolean (True or False) that tracks if the game has ended
# We start with False because the game just began
# This becomes True when someone wins or the board is full (tie)
game_over = False

# winner: A string that will hold 'X', 'O', or 'Tie' when the game ends
# We start with an empty string because no one has won yet
winner = ''

# moves_made: An integer that counts how many moves have been made
# We use this to detect tie games (when moves_made reaches 9)
moves_made = 0

print("Game setup complete! Here's how the nested list works:")
print("board[0] =", board[0], "← This is the top row")
print("board[1] =", board[1], "← This is the middle row") 
print("board[2] =", board[2], "← This is the bottom row")
print()
print("To access a specific position, we use board[row][column]:")
print("board[0][0] =", board[0][0], "← Top-left position")
print("board[1][1] =", board[1][1], "← Center position")
print("board[2][2] =", board[2][2], "← Bottom-right position")
print()
print("Let's start playing!")
print()

# ============================================
# BOARD DISPLAY SECTION
# ============================================
# This section contains code to show the current game board
# It formats the board nicely so players can see the game state

def display_board():
    """
    Note: We're not using functions in this educational version!
    This comment block shows what this section does, but the actual
    code is written inline below to keep it simple for beginners.
    
    This section displays the current game board in a nice format.
    It uses nested loops to go through each row and column.
    """
    pass  # This line does nothing - it's just a placeholder

# Display the current board using nested loops
# This is the heart of how we work with nested lists!

print("Current board:")
print()

# This outer loop goes through each row in our board
# range(3) gives us the numbers 0, 1, 2 (for our three rows)
# We use 'i' as our row number variable
for i in range(3):
    print(" ", end="")  # Print a space at the start of each row for formatting
    
    # This inner loop goes through each column in the current row
    # range(3) gives us the numbers 0, 1, 2 (for our three columns)
    # We use 'j' as our column number variable
    for j in range(3):
        # board[i][j] means: go to row i, then column j
        # For example: board[0][1] is row 0, column 1 (position 2)
        print(board[i][j], end="")
        
        # Add a vertical separator (|) between columns, but not after the last column
        if j < 2:  # j < 2 means "if this is not the last column"
            print(" | ", end="")
    
    # After printing all columns in this row, start a new line
    print()  # This creates a line break to move to the next row
    
    # Add a horizontal separator line between rows, but not after the last row
    if i < 2:  # i < 2 means "if this is not the last row"
        print("-----------")

print()  # Add an extra blank line after the board for better spacing

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
    # It checks if the input is valid and converts it to the right format
    
    # valid_move: A boolean that tracks whether the player's move is acceptable
    # We start with False and only set it to True if all checks pass
    valid_move = False
    
    # Keep asking for input until we get a valid move
    # This while loop will repeat until valid_move becomes True
    while not valid_move:
        
        # Get input from the current player
        # f-strings let us put variables directly into strings
        player_input = input(f"Player {current_player}, enter position (1-9): ")
        
        # INPUT VALIDATION STEP 1: Check if input can be converted to a number
        # We use try/except to catch errors if they enter letters or symbols
        try:
            # int() converts the string input to an integer (whole number)
            # If the player typed letters, this will cause an error
            position = int(player_input)
            
            # INPUT VALIDATION STEP 2: Check if the number is in valid range
            # Valid positions are 1, 2, 3, 4, 5, 6, 7, 8, 9
            if position >= 1 and position <= 9:
                
                # COORDINATE CONVERSION: Convert position number to row and column
                # This is the key math for working with nested lists!
                # Position numbers 1-9 need to become row/column coordinates 0-2
                
                # Calculate which row this position is in
                # We subtract 1 because positions start at 1 but rows start at 0
                # Then we divide by 3 and ignore the remainder (that's what // does)
                row = (position - 1) // 3
                
                # Calculate which column this position is in  
                # We use % (modulo) to get the remainder when dividing by 3
                col = (position - 1) % 3
                
                print(f"Position {position} converts to row {row}, column {col}")
                
                # INPUT VALIDATION STEP 3: Check if the position is empty
                # A position is empty if it still contains its original number
                # If it contains 'X' or 'O', then it's already taken
                if board[row][col] not in ['X', 'O']:
                    # Position is empty! We can make this move
                    valid_move = True
                    print(f"Valid move! Placing {current_player} at position {position}")
                else:
                    # Position is already taken
                    print(f"Position {position} is already taken by {board[row][col]}. Choose an empty position.")
                    
            else:
                # The number is outside our valid range (less than 1 or greater than 9)
                print("Please enter a number between 1 and 9")
                
        except:
            # This runs if int() failed because they entered non-numbers
            print("Please enter a number, not letters or symbols")
    
    # MAKE THE MOVE: Update the board with the player's choice
    # At this point we know the move is valid, so we can safely update the board
    board[row][col] = current_player
    moves_made = moves_made + 1  # Keep track of how many moves have been made
    
    print(f"Move made! {current_player} placed at row {row}, column {col}")
    print()
    
    # DISPLAY UPDATED BOARD: Show the board after the move
    print("Updated board:")
    print()
    
    # Display the board again using the same nested loop structure
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-----------")
    
    print()
    
    # ============================================
    # WIN DETECTION SECTION
    # ============================================
    # This section checks if someone has won the game
    # We need to check all possible winning combinations
    
    # CHECK FOR ROW WINS (horizontal lines)
    # We need to check if any row has three of the same symbol
    for i in range(3):  # Check each of the 3 rows
        # Check if all three positions in this row are the same
        # AND make sure they're not empty (not just numbers)
        if (board[i][0] == board[i][1] == board[i][2] and 
            board[i][0] in ['X', 'O']):
            winner = board[i][0]  # The winner is whoever has three in this row
            game_over = True
            print(f"Row {i} win! Player {winner} wins!")
            break  # Stop checking once we find a winner
    
    # CHECK FOR COLUMN WINS (vertical lines)
    # Only check if no one has won yet
    if not game_over:
        for j in range(3):  # Check each of the 3 columns
            # Check if all three positions in this column are the same
            # AND make sure they're not empty (not just numbers)
            if (board[0][j] == board[1][j] == board[2][j] and 
                board[0][j] in ['X', 'O']):
                winner = board[0][j]  # The winner is whoever has three in this column
                game_over = True
                print(f"Column {j} win! Player {winner} wins!")
                break  # Stop checking once we find a winner
    
    # CHECK FOR DIAGONAL WINS
    # Only check if no one has won yet
    if not game_over:
        # Check main diagonal (top-left to bottom-right)
        # Positions: board[0][0], board[1][1], board[2][2]
        if (board[0][0] == board[1][1] == board[2][2] and 
            board[0][0] in ['X', 'O']):
            winner = board[0][0]
            game_over = True
            print(f"Main diagonal win! Player {winner} wins!")
        
        # Check anti-diagonal (top-right to bottom-left)
        # Positions: board[0][2], board[1][1], board[2][0]
        elif (board[0][2] == board[1][1] == board[2][0] and 
              board[0][2] in ['X', 'O']):
            winner = board[0][2]
            game_over = True
            print(f"Anti-diagonal win! Player {winner} wins!")
    
    # CHECK FOR TIE GAME
    # If no one has won and all 9 positions are filled, it's a tie
    if not game_over and moves_made == 9:
        winner = 'Tie'
        game_over = True
        print("All positions filled - it's a tie game!")
    
    # SWITCH PLAYERS (only if game is not over)
    # After each move, we need to switch to the other player
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

# Display the final board one more time
for i in range(3):
    print(" ", end="")
    for j in range(3):
        print(board[i][j], end="")
        if j < 2:
            print(" | ", end="")
    print()
    if i < 2:
        print("-----------")

print()

# ============================================
# PLAY AGAIN FUNCTIONALITY
# ============================================
# Ask if the players want to play another game

play_again = input("Would you like to play again? (y/n): ").lower()

if play_again == 'y' or play_again == 'yes':
    print()
    print("Starting a new game...")
    print("To play again, run this program again!")
    print("In a more advanced version, we could restart the game automatically.")
else:
    print()
    print("Thanks for playing Tic-Tac-Toe!")
    print("This was the nested lists version - try the dictionary version next!")
    print("You learned about:")
    print("- Nested lists and [row][column] indexing")
    print("- Converting position numbers to coordinates")
    print("- Using loops for systematic checking")
    print("- Input validation and error handling")