"""
Tic-Tac-Toe Game - Object-Oriented Programming Version

This file demonstrates how to create a tic-tac-toe game using Object-Oriented
Programming (OOP) principles. This version is designed for students who have
learned about functions and classes and are ready to see how OOP can organize
code more effectively.

Key OOP concepts demonstrated:
- Classes: Blueprints for creating objects that bundle data and behavior
- Objects: Instances of classes that have their own state
- Methods: Functions that belong to a class and operate on its data
- Instance Variables: Data that belongs to a specific object (using self)
- Encapsulation: Keeping related data and behavior together in a class
- Constructor (__init__): Special method that initializes new objects
- Private Methods: Methods prefixed with _ for internal use only
- Public Methods: Methods without _ prefix for external use

Comparison with procedural versions:
- Procedural (tictactoe_lists.py, tictactoe_dict.py):
  * Uses global variables to store game state
  * Functions operate on data passed as parameters
  * State is scattered across multiple variables
  * Good for learning basic programming concepts
  
- Object-Oriented (this file):
  * Uses instance variables to store game state
  * Methods operate on the object's own data (self)
  * State is encapsulated within the class
  * Better for larger programs and code organization
  * Easier to create multiple games or extend functionality

Why use OOP?
- Organization: Related data and behavior are grouped together
- Reusability: Can create multiple game instances easily
- Maintainability: Changes to game logic are localized to methods
- Extensibility: Easy to add new features (undo, save/load, AI player)
- Real-world modeling: Objects represent real-world entities naturally

This version uses nested lists to represent the board, making it easy to
work with rows and columns using 2D indexing.

Usage example:
    # Create a new game
    game = TicTacToeGame()
    
    # Play the game interactively
    game.play()
    
    # Or use individual methods for custom game flow
    game.display_board()
    game.make_move(5)  # X moves to center
    game.make_move(1)  # O moves to top-left
    if game.is_game_over():
        print(f"Winner: {game.winner}")

Author: Educational Python Project
Python Level: OOP Learners (Functions and Classes)
"""


# ============================================
# CLASS DEFINITION
# ============================================

class TicTacToeGame:
    """
    Represents a complete tic-tac-toe game with all game logic and state.
    
    This class encapsulates everything needed to play tic-tac-toe:
    - The game board (3x3 grid)
    - Which player's turn it is
    - Whether the game has ended
    - Who won (if anyone)
    - How many moves have been made
    
    By using a class, we keep all game-related data and behavior organized
    in one place. This makes the code easier to understand, test, and modify.
    
    Attributes:
        board (list): A 3x3 nested list representing the game board.
                     Each position starts with its number ('1'-'9') and
                     gets replaced with 'X' or 'O' when players move.
        board_size (int): The size of the board (3 for standard tic-tac-toe).
                         This makes it easier to extend to larger boards later.
        current_player (str): Either 'X' or 'O', indicating whose turn it is.
        game_over (bool): True if the game has ended, False if still playing.
        winner (str or None): 'X', 'O', 'Tie', or None if game is ongoing.
        moves_made (int): Counter tracking how many valid moves have been made.
    
    Example:
        >>> game = TicTacToeGame()
        >>> game.current_player
        'X'
        >>> game.game_over
        False
    """
    
    def __init__(self):
        """
        Initialize a new tic-tac-toe game.
        
        This is the constructor method (also called an initializer).
        It runs automatically when you create a new TicTacToeGame object.
        The __init__ method sets up the initial state of the game.
        
        The 'self' parameter is special in Python:
        - It refers to the specific object being created
        - It lets us attach data to this particular game instance
        - Every method in a class needs self as its first parameter
        
        Think of 'self' as "this specific game" - it's how we keep track
        of data that belongs to this particular game object.
        """
        
        # board: A nested list (list of lists) representing the 3x3 game grid
        # We initialize it with strings '1' through '9' to show position numbers
        # When players make moves, we'll replace these with 'X' or 'O'
        # 
        # The structure is:
        #   [['1', '2', '3'],   <- Row 0 (top row)
        #    ['4', '5', '6'],   <- Row 1 (middle row)
        #    ['7', '8', '9']]   <- Row 2 (bottom row)
        #
        # We access positions using board[row][column]
        # For example: board[0][0] is position '1', board[1][1] is position '5'
        self.board = [
            ['1', '2', '3'],  # Top row: positions 1, 2, 3
            ['4', '5', '6'],  # Middle row: positions 4, 5, 6
            ['7', '8', '9']   # Bottom row: positions 7, 8, 9
        ]
        
        # board_size: The dimension of our board (3 for a 3x3 grid)
        # We store this as an instance variable so we could potentially
        # extend the game to support different board sizes in the future
        # For now, it's always 3 for standard tic-tac-toe
        self.board_size = 3
        
        # current_player: A string that holds either 'X' or 'O'
        # This tracks whose turn it is to play
        # By convention, X always goes first in tic-tac-toe
        # This will switch between 'X' and 'O' after each valid move
        self.current_player = 'X'
        
        # game_over: A boolean (True/False) that tracks if the game has ended
        # We start with False because the game just began
        # This becomes True when someone wins or the board is full (tie)
        # We use this to control the main game loop
        self.game_over = False
        
        # winner: Stores who won the game
        # Starts as None because no one has won yet
        # Will be set to 'X' if X wins, 'O' if O wins, or 'Tie' for a tie
        # Remains None while the game is still in progress
        self.winner = None
        
        # moves_made: A counter that tracks how many valid moves have been made
        # Starts at 0 because no moves have been made yet
        # Increments by 1 each time a player successfully makes a move
        # Useful for detecting ties (if moves_made reaches 9 with no winner)
        self.moves_made = 0
    
    def display_board(self):
        """
        Display the current state of the game board.
        
        This method prints the board in a nice 3x3 grid format with:
        - Vertical bars (|) separating columns
        - Horizontal lines separating rows
        - Position numbers (1-9) for empty spaces
        - Player marks (X or O) for occupied spaces
        
        The board looks like this:
         1 | 2 | 3
        -----------
         4 | 5 | 6
        -----------
         7 | 8 | 9
        
        This is a method (a function that belongs to the class).
        Methods can access the object's data using 'self'.
        Here, we use self.board to access this game's board data.
        """
        
        # We use nested loops to go through each row and column
        # The outer loop handles rows (0, 1, 2)
        # The inner loop handles columns (0, 1, 2) within each row
        
        # Loop through each row in the board
        # range(self.board_size) gives us 0, 1, 2 for a 3x3 board
        # We use self.board_size instead of hardcoding 3 to make it flexible
        for row in range(self.board_size):
            
            # Loop through each column in the current row
            # This inner loop runs 3 times for each row
            for col in range(self.board_size):
                
                # self.board[row][col] accesses the value at this position
                # For example: self.board[0][1] is the top-middle position
                # We print it with a space before for nice formatting
                print(f" {self.board[row][col]} ", end='')
                
                # Add a vertical bar (|) between columns, but not after the last column
                # col < self.board_size - 1 means "not the last column"
                # For a 3x3 board: col < 2, so we add | after columns 0 and 1
                if col < self.board_size - 1:
                    print("|", end='')
            
            # After finishing all columns in a row, move to the next line
            print()  # This creates a line break
            
            # Add a horizontal line between rows, but not after the last row
            # row < self.board_size - 1 means "not the last row"
            # For a 3x3 board: row < 2, so we add lines after rows 0 and 1
            if row < self.board_size - 1:
                # Print a line of dashes to separate rows
                # We use 11 dashes to match the width of the board
                # (3 spaces for each cell + 2 bars = 11 characters)
                print("-----------")
    
    def _position_to_coords(self, position):
        """
        Convert a position number (1-9) to row and column coordinates.
        
        This is a private helper method (indicated by the underscore prefix).
        Private methods are meant to be used internally by the class, not by
        code outside the class. This helps with encapsulation - keeping
        implementation details hidden.
        
        Players think of the board as positions 1-9:
         1 | 2 | 3
        -----------
         4 | 5 | 6
        -----------
         7 | 8 | 9
        
        But our nested list uses row/column coordinates starting at 0:
         [0][0] | [0][1] | [0][2]
        ------------------------
         [1][0] | [1][1] | [1][2]
        ------------------------
         [2][0] | [2][1] | [2][2]
        
        This method converts between these two systems using math.
        
        Args:
            position (int): A position number from 1 to 9
            
        Returns:
            tuple: A tuple of (row, col) where both are 0-2
            
        Example:
            >>> game = TicTacToeGame()
            >>> game._position_to_coords(1)
            (0, 0)
            >>> game._position_to_coords(5)
            (1, 1)
            >>> game._position_to_coords(9)
            (2, 2)
        """
        
        # First, we need to convert from 1-9 to 0-8
        # We do this by subtracting 1 from the position
        # Position 1 becomes 0, position 5 becomes 4, position 9 becomes 8
        adjusted_position = position - 1
        
        # Now we calculate the row using integer division (//)
        # Integer division divides and rounds down to the nearest whole number
        # 
        # How it works:
        # - Positions 1-3 (adjusted: 0-2) → 0 // 3 = 0, 1 // 3 = 0, 2 // 3 = 0 → row 0
        # - Positions 4-6 (adjusted: 3-5) → 3 // 3 = 1, 4 // 3 = 1, 5 // 3 = 1 → row 1
        # - Positions 7-9 (adjusted: 6-8) → 6 // 3 = 2, 7 // 3 = 2, 8 // 3 = 2 → row 2
        #
        # This works because every 3 positions is a new row
        row = adjusted_position // self.board_size
        
        # Now we calculate the column using the modulo operator (%)
        # Modulo gives us the remainder after division
        # 
        # How it works:
        # - Positions 1, 4, 7 (adjusted: 0, 3, 6) → 0 % 3 = 0, 3 % 3 = 0, 6 % 3 = 0 → col 0
        # - Positions 2, 5, 8 (adjusted: 1, 4, 7) → 1 % 3 = 1, 4 % 3 = 1, 7 % 3 = 1 → col 1
        # - Positions 3, 6, 9 (adjusted: 2, 5, 8) → 2 % 3 = 2, 5 % 3 = 2, 8 % 3 = 2 → col 2
        #
        # This works because the remainder cycles through 0, 1, 2 for each row
        col = adjusted_position % self.board_size
        
        # Return both values as a tuple (a pair of values)
        # The calling code can unpack this like: row, col = self._position_to_coords(5)
        return (row, col)
    
    def _is_valid_move(self, position):
        """
        Check if a move to the specified position is valid.
        
        This is another private helper method that validates whether a player
        can make a move at a given position. A move is valid if:
        1. The position is in the valid range (1-9)
        2. The position is not already occupied by 'X' or 'O'
        
        This method demonstrates defensive programming - we check for errors
        before they happen, making our code more robust and user-friendly.
        
        Args:
            position (int): The position number (should be 1-9)
            
        Returns:
            bool: True if the move is valid, False otherwise
            
        Example:
            >>> game = TicTacToeGame()
            >>> game._is_valid_move(5)
            True
            >>> game.board[1][1] = 'X'  # Occupy position 5
            >>> game._is_valid_move(5)
            False
            >>> game._is_valid_move(10)
            False
        """
        
        # First validation: Check if position is in the valid range (1-9)
        # We use 'and' to check both conditions:
        # - position >= 1: position is not too small
        # - position <= 9: position is not too large
        # If either condition is False, the whole expression is False
        if position < 1 or position > 9:
            # Position is outside valid range, so the move is invalid
            return False
        
        # Second validation: Check if the position is already occupied
        # We need to convert the position to row/column coordinates first
        # We use our helper method _position_to_coords for this
        row, col = self._position_to_coords(position)
        
        # Now check what's at this position on the board
        # self.board[row][col] gives us the value at this position
        # It could be:
        # - A number string ('1' through '9') if empty
        # - 'X' if X has moved there
        # - 'O' if O has moved there
        cell_value = self.board[row][col]
        
        # A position is occupied if it contains 'X' or 'O'
        # We check if the cell value is one of these marks
        # If it is 'X' or 'O', the position is taken and the move is invalid
        if cell_value == 'X' or cell_value == 'O':
            # Position is already occupied, so the move is invalid
            return False
        
        # If we get here, both validations passed:
        # - Position is in range 1-9
        # - Position is not occupied
        # Therefore, the move is valid
        return True
    
    def make_move(self, position):
        """
        Attempt to make a move at the specified position.
        
        This is a public method (no underscore) that players use to make moves.
        It orchestrates the entire move process:
        1. Validates the move
        2. Updates the board if valid
        3. Increments the move counter
        4. Checks for a winner or tie
        5. Switches to the other player if game continues
        
        This method demonstrates how methods can call other methods to break
        down complex tasks into simpler steps.
        
        Args:
            position (int): The position number (1-9) where the player wants to move
            
        Returns:
            bool: True if the move was successful, False if invalid
            
        Example:
            >>> game = TicTacToeGame()
            >>> game.make_move(5)  # X moves to center
            True
            >>> game.current_player
            'O'
            >>> game.make_move(5)  # Try to move to occupied position
            False
            >>> game.current_player
            'O'
        """
        
        # Step 1: Validate the move using our helper method
        # This checks if the position is in range and not occupied
        # We call self._is_valid_move() to do this validation
        if not self._is_valid_move(position):
            # The move is invalid, so we return False
            # We don't change anything - the board stays the same
            # The current player stays the same (they need to try again)
            return False
        
        # If we get here, the move is valid, so we can proceed
        
        # Step 2: Convert the position to row/column coordinates
        # We need this to update the correct spot on the board
        row, col = self._position_to_coords(position)
        
        # Step 3: Update the board with the current player's mark
        # self.current_player is either 'X' or 'O'
        # We place this mark at the specified position
        self.board[row][col] = self.current_player
        
        # Step 4: Increment the move counter
        # We add 1 to track that another move has been made
        # This is useful for detecting ties (when moves_made reaches 9)
        self.moves_made += 1
        
        # Step 5: Check if this move resulted in a win or tie
        # We call check_winner() which will:
        # - Return 'X' or 'O' if someone won
        # - Return 'Tie' if the board is full with no winner
        # - Return None if the game should continue
        # Note: check_winner() will also set self.game_over and self.winner
        result = self.check_winner()
        
        # Step 6: Switch players if the game is not over
        # We only switch if the game is still ongoing
        # If someone won or there's a tie, we don't switch
        if not self.game_over:
            # Game continues, so switch to the other player
            # We call our helper method to do this
            self._switch_player()
        
        # Step 7: Return True to indicate the move was successful
        # The calling code can use this to know the move worked
        return True
    
    def _switch_player(self):
        """
        Switch to the other player.
        
        This private helper method changes the current player from X to O
        or from O to X. It's called after each successful move to alternate
        turns between the two players.
        
        This demonstrates a simple but important game mechanic - turn-taking.
        We use a conditional to check who the current player is and switch
        to the other one.
        
        The method modifies self.current_player directly, which is an example
        of how methods can change an object's state.
        
        Example:
            >>> game = TicTacToeGame()
            >>> game.current_player
            'X'
            >>> game._switch_player()
            >>> game.current_player
            'O'
            >>> game._switch_player()
            >>> game.current_player
            'X'
        """
        
        # Check who the current player is and switch to the other one
        # We use an if-else statement to handle both cases
        
        if self.current_player == 'X':
            # Current player is X, so switch to O
            self.current_player = 'O'
        else:
            # Current player is O, so switch to X
            # We use else instead of checking == 'O' because there are only two players
            # If it's not X, it must be O
            self.current_player = 'X'
    
    def check_winner(self):
        """
        Check if there's a winner or tie.
        
        This method systematically checks all possible winning conditions:
        - All 3 rows (horizontal wins)
        - All 3 columns (vertical wins)
        - Both diagonals (diagonal wins)
        - Full board with no winner (tie)
        
        When a winner is found, this method:
        1. Sets self.game_over to True
        2. Sets self.winner to the winning player
        3. Returns the winner
        
        This demonstrates systematic problem-solving - we check each possible
        win condition in an organized way using loops where possible.
        
        Returns:
            str or None: 'X' if X wins, 'O' if O wins, 'Tie' if board is full
                        with no winner, or None if game should continue
                        
        Example:
            >>> game = TicTacToeGame()
            >>> game.board[0] = ['X', 'X', 'X']  # X wins top row
            >>> game.check_winner()
            'X'
            >>> game.game_over
            True
        """
        
        # ============================================
        # CHECK ROWS (HORIZONTAL WINS)
        # ============================================
        # We check each of the 3 rows to see if all positions match
        # A row wins if all 3 positions have the same mark ('X' or 'O')
        
        # Loop through each row (0, 1, 2)
        for row in range(self.board_size):
            # Get the values in this row
            # board[row][0] is first column, [1] is second, [2] is third
            first = self.board[row][0]
            second = self.board[row][1]
            third = self.board[row][2]
            
            # Check if all three positions in this row are the same
            # AND make sure they're not empty (not a number string)
            # We need to check it's 'X' or 'O', not '1', '2', '3', etc.
            if first == second == third and (first == 'X' or first == 'O'):
                # We found a winner! All three in this row match
                self.game_over = True
                self.winner = first  # first contains the winning mark
                return first
        
        # ============================================
        # CHECK COLUMNS (VERTICAL WINS)
        # ============================================
        # We check each of the 3 columns to see if all positions match
        # A column wins if all 3 positions have the same mark ('X' or 'O')
        
        # Loop through each column (0, 1, 2)
        for col in range(self.board_size):
            # Get the values in this column
            # board[0][col] is first row, [1][col] is second, [2][col] is third
            first = self.board[0][col]
            second = self.board[1][col]
            third = self.board[2][col]
            
            # Check if all three positions in this column are the same
            # AND make sure they're not empty (not a number string)
            if first == second == third and (first == 'X' or first == 'O'):
                # We found a winner! All three in this column match
                self.game_over = True
                self.winner = first  # first contains the winning mark
                return first
        
        # ============================================
        # CHECK MAIN DIAGONAL (TOP-LEFT TO BOTTOM-RIGHT)
        # ============================================
        # The main diagonal goes from position 1 to position 9
        # That's board[0][0] → board[1][1] → board[2][2]
        
        # Get the three positions on the main diagonal
        first = self.board[0][0]   # Top-left (position 1)
        second = self.board[1][1]  # Center (position 5)
        third = self.board[2][2]   # Bottom-right (position 9)
        
        # Check if all three diagonal positions are the same
        # AND make sure they're not empty
        if first == second == third and (first == 'X' or first == 'O'):
            # We found a winner! All three on main diagonal match
            self.game_over = True
            self.winner = first
            return first
        
        # ============================================
        # CHECK ANTI-DIAGONAL (TOP-RIGHT TO BOTTOM-LEFT)
        # ============================================
        # The anti-diagonal goes from position 3 to position 7
        # That's board[0][2] → board[1][1] → board[2][0]
        
        # Get the three positions on the anti-diagonal
        first = self.board[0][2]   # Top-right (position 3)
        second = self.board[1][1]  # Center (position 5)
        third = self.board[2][0]   # Bottom-left (position 7)
        
        # Check if all three diagonal positions are the same
        # AND make sure they're not empty
        if first == second == third and (first == 'X' or first == 'O'):
            # We found a winner! All three on anti-diagonal match
            self.game_over = True
            self.winner = first
            return first
        
        # ============================================
        # CHECK FOR TIE (BOARD FULL, NO WINNER)
        # ============================================
        # If we get here, no one has won yet
        # Check if the board is full (all 9 moves made)
        # If it's full and no winner, it's a tie
        
        if self.moves_made >= 9:
            # Board is full (9 moves made) and no winner found
            # This is a tie game
            self.game_over = True
            self.winner = 'Tie'
            return 'Tie'
        
        # ============================================
        # GAME CONTINUES
        # ============================================
        # If we get here:
        # - No one has won yet
        # - The board is not full yet
        # - The game should continue
        return None
    
    def is_game_over(self):
        """
        Check if the game has ended.
        
        This is a simple getter method that returns the current value of
        the game_over attribute. It provides a clean way for external code
        to check if the game has finished without directly accessing the
        internal attribute.
        
        This demonstrates encapsulation - we provide a method to access
        internal state rather than requiring external code to know about
        our internal implementation details.
        
        The game is over when:
        - Someone has won (three in a row)
        - The board is full with no winner (tie)
        
        Returns:
            bool: True if the game has ended, False if still playing
            
        Example:
            >>> game = TicTacToeGame()
            >>> game.is_game_over()
            False
            >>> game.board[0] = ['X', 'X', 'X']
            >>> game.check_winner()
            'X'
            >>> game.is_game_over()
            True
        """
        
        # Simply return the value of the game_over attribute
        # This attribute is set to True by check_winner() when:
        # - A player wins (three in a row)
        # - The game ends in a tie (board full, no winner)
        return self.game_over
    
    def play(self):
        """
        Run the main game loop.
        
        This method orchestrates the entire game from start to finish.
        It's the main entry point for playing a complete game of tic-tac-toe.
        
        The game flow:
        1. Display welcome message
        2. Loop while game is not over:
           a. Display the current board
           b. Get input from current player
           c. Attempt to make the move
           d. If invalid, show error and continue loop
           e. If valid, move is made and players switch automatically
        3. Display final board
        4. Display game result (winner or tie)
        
        This demonstrates how a method can coordinate multiple other methods
        to create a complete, working application.
        
        Example:
            >>> game = TicTacToeGame()
            >>> game.play()
            # Game runs interactively until completion
        """
        
        # Display welcome message at the start of the game
        # We use a helper function to keep the code organized
        display_welcome_message()
        
        # ============================================
        # MAIN GAME LOOP
        # ============================================
        # This loop continues until the game is over
        # We use self.is_game_over() to check the game status
        
        while not self.is_game_over():
            
            # Step 1: Display the current board
            # This shows players the current state of the game
            self.display_board()
            print()  # Add a blank line for readability
            
            # Step 2: Get input from the current player
            # We use the helper function get_player_input()
            # It handles all input validation and returns a valid position
            position = get_player_input(self.current_player)
            
            # Step 3: Attempt to make the move
            # make_move() returns True if successful, False if invalid
            # A move can be invalid if the position is already occupied
            move_successful = self.make_move(position)
            
            # Step 4: Check if the move was successful
            if not move_successful:
                # The move was invalid (position already taken)
                # Display an error message and continue the loop
                # The player will get another chance to enter a valid move
                print(f"\nPosition {position} is already taken! Try again.\n")
                # Loop continues, asking for input again
            else:
                # The move was successful
                # make_move() has already:
                # - Updated the board
                # - Checked for winner
                # - Switched players (if game continues)
                # So we just continue to the next iteration
                pass
        
        # ============================================
        # GAME OVER - DISPLAY RESULTS
        # ============================================
        # If we get here, the game is over
        # Display the final board and announce the result
        
        # Display the final board state
        print("\nFinal board:")
        self.display_board()
        
        # Display the game over message with the result
        # We use a helper function to keep the code organized
        display_game_over_message(self.winner)


# ============================================
# HELPER FUNCTIONS
# ============================================
# These are standalone functions (not methods) that support the game
# but don't need to be part of the class


def display_welcome_message():
    """
    Display the game introduction and instructions.
    
    This function shows a welcome banner and explains what makes the
    OOP version special. It helps players understand they're playing
    an educational version that demonstrates object-oriented programming.
    
    This is a standalone function because it doesn't need access to any
    game state - it just displays static information.
    
    Example:
        >>> display_welcome_message()
        ==================================================
        Welcome to Tic-Tac-Toe - Object-Oriented Version!
        ==================================================
        ...
    """
    
    # Display a banner to make the welcome message stand out
    print("\n" + "=" * 50)
    print("Welcome to Tic-Tac-Toe - Object-Oriented Version!")
    print("=" * 50)
    
    # Explain what OOP concepts this version demonstrates
    # This helps students understand the educational value
    print("\nThis version demonstrates OOP concepts:")
    print("- Classes and objects")
    print("- Methods and instance variables")
    print("- Encapsulation of game logic")
    
    # Provide basic instructions for playing
    print("\nEnter a number (1-9) to place your mark.")
    print("=" * 50 + "\n")


def display_game_over_message(winner):
    """
    Display the game over message with the result.
    
    This function announces the end of the game and displays who won
    or if the game ended in a tie. It provides a nice conclusion to
    the game experience.
    
    Args:
        winner (str): Either 'X', 'O', or 'Tie'
        
    Example:
        >>> display_game_over_message('X')
        ==================================================
        GAME OVER!
        ==================================================
        Player X wins! Congratulations!
        
        >>> display_game_over_message('Tie')
        ==================================================
        GAME OVER!
        ==================================================
        It's a tie! The board is full with no winner.
    """
    
    # Display a banner to announce the game is over
    print("\n" + "=" * 50)
    print("GAME OVER!")
    print("=" * 50 + "\n")
    
    # Display the appropriate message based on the result
    # We check if it's a tie or if someone won
    if winner == 'Tie':
        # The game ended in a tie (board full, no winner)
        print("It's a tie! The board is full with no winner.")
    else:
        # Someone won the game (winner is 'X' or 'O')
        print(f"Player {winner} wins! Congratulations!")
    
    # Display a closing banner
    print("\n" + "=" * 50)
    print("Thanks for playing!")
    print("=" * 50 + "\n")


def get_player_input(current_player):
    """
    Get and validate input from the player.
    
    This is a standalone function (not a method of the class) that handles
    all user input and validation. It keeps asking for input until the
    player provides a valid number between 1 and 9.
    
    This function demonstrates:
    - Input validation with try-except
    - Loops that continue until valid input is received
    - Helpful error messages for different types of invalid input
    
    The function validates:
    1. Input is numeric (not letters or symbols)
    2. Input is in the valid range (1-9)
    
    Note: This function does NOT check if the position is occupied.
    That check happens in the make_move method.
    
    Args:
        current_player (str): Either 'X' or 'O', used in the prompt
        
    Returns:
        int: A valid position number from 1 to 9
        
    Example:
        >>> position = get_player_input('X')
        Player X, enter your move (1-9): 5
        >>> position
        5
    """
    
    # We use a while loop to keep asking until we get valid input
    # This loop will continue forever until we return a valid value
    while True:
        
        # Prompt the player for their move
        # We use an f-string to include the current player in the message
        player_input = input(f"Player {current_player}, enter your move (1-9): ")
        
        # ============================================
        # VALIDATION STEP 1: Check if input is numeric
        # ============================================
        # We use try-except to handle the case where input is not a number
        # If the player enters letters or symbols, int() will raise a ValueError
        
        try:
            # Try to convert the input string to an integer
            # If this works, we know the input is numeric
            position = int(player_input)
            
            # ============================================
            # VALIDATION STEP 2: Check if number is in range
            # ============================================
            # Now we know it's a number, but is it between 1 and 9?
            
            if position >= 1 and position <= 9:
                # Success! The input is a number between 1 and 9
                # Return it to the calling code
                return position
            else:
                # The number is outside the valid range
                # Display a helpful error message and loop again
                print("Invalid input! Please enter a number between 1 and 9.")
                # The loop continues, asking for input again
                
        except ValueError:
            # This runs if int() failed (input was not numeric)
            # ValueError is raised when you try to convert non-numeric text to int
            print("Invalid input! Please enter a number, not letters or symbols.")
            # The loop continues, asking for input again


# ============================================
# MAIN PROGRAM ENTRY POINT
# ============================================
# This section runs when the file is executed directly
# It's the starting point of the program

if __name__ == "__main__":
    """
    Main entry point for the tic-tac-toe game.
    
    This special block only runs when this file is executed directly
    (e.g., python tictactoe_oop.py), not when it's imported as a module.
    
    The pattern "if __name__ == '__main__':" is a Python convention that:
    - Allows the file to be both a runnable program and an importable module
    - Prevents code from running when the file is imported
    - Makes it clear where program execution begins
    
    This is good practice for organizing Python programs.
    """
    
    # Create a new instance of the TicTacToeGame class
    # This instantiates an object with all the game logic and state
    # The __init__ method runs automatically, setting up the board
    game = TicTacToeGame()
    
    # Call the play method to start the game
    # This runs the entire game from start to finish
    # The method handles all user interaction and game flow
    game.play()
