# Implementation Plan: Tic-Tac-Toe OOP Version

- [x] 1. Create the TicTacToeGame class with initialization
  - Create new file `tictactoe_oop.py` with proper file header and documentation
  - Define the `TicTacToeGame` class with comprehensive docstring
  - Implement `__init__` method to initialize board as 3x3 nested list
  - Initialize instance variables: current_player, game_over, winner, moves_made, board_size
  - Add educational comments explaining OOP concepts (self, instance variables, constructor)
  - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [ ]* 1.1 Write unit tests for initialization
  - Test board is created as 3x3 list with positions '1'-'9'
  - Test current_player starts as 'X'
  - Test game_over starts as False
  - Test winner starts as None
  - Test moves_made starts as 0
  - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [x] 2. Implement board display method
  - Create `display_board` method that prints the current board state
  - Use nested loops to iterate through rows and columns
  - Format output with vertical bars (|) between columns
  - Format output with horizontal lines between rows
  - Add comments explaining 2D list iteration
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

- [ ]* 2.1 Write property test for board display
  - **Property 1: Empty positions display their numbers**
  - **Validates: Requirements 2.4**
  - Generate random board states with empty positions
  - Verify empty positions show their numbers (1-9)

- [ ]* 2.2 Write property test for occupied position display
  - **Property 2: Occupied positions display player marks**
  - **Validates: Requirements 2.5**
  - Generate random board states with X and O marks
  - Verify occupied positions show correct marks

- [x] 3. Implement position conversion helper method
  - Create `_position_to_coords` private method
  - Convert position (1-9) to row and column coordinates
  - Use integer division (//) for row calculation
  - Use modulo (%) for column calculation
  - Add educational comments explaining the math
  - _Requirements: 3.1, 4.1_

- [ ]* 3.1 Write unit tests for position conversion
  - Test position 1 converts to (0, 0)
  - Test position 5 converts to (1, 1)
  - Test position 9 converts to (2, 2)
  - Test all positions 1-9 convert correctly
  - _Requirements: 3.1, 4.1_

- [x] 4. Implement move validation method
  - Create `_is_valid_move` private method
  - Check if position is in range 1-9
  - Convert position to coordinates
  - Check if board position is not occupied ('X' or 'O')
  - Return True for valid moves, False for invalid
  - Add educational comments about validation logic
  - _Requirements: 3.1, 3.2, 3.3, 3.4_

- [ ]* 4.1 Write property test for invalid position range
  - **Property 3: Invalid position range rejection**
  - **Validates: Requirements 3.1**
  - Generate random positions outside 1-9 range
  - Verify all are rejected as invalid

- [ ]* 4.2 Write property test for occupied position rejection
  - **Property 4: Occupied position rejection**
  - **Validates: Requirements 3.2**
  - Generate random board states with occupied positions
  - Verify moves to occupied positions are rejected

- [x] 5. Implement make_move method
  - Create `make_move` method that accepts a position parameter
  - Validate the move using `_is_valid_move`
  - If invalid, return False
  - If valid, convert position to coordinates
  - Update board with current player's mark
  - Increment moves_made counter
  - Check for winner using `check_winner` (to be implemented)
  - If game not over, switch players
  - Return True for successful move
  - Add comprehensive docstring and comments
  - _Requirements: 3.3, 3.4, 4.1, 4.2, 4.4, 4.5_

- [ ]* 5.1 Write property test for valid moves return True
  - **Property 6: Valid moves return True**
  - **Validates: Requirements 3.4**
  - Generate random valid moves on empty positions
  - Verify all return True

- [ ]* 5.2 Write property test for invalid moves return False
  - **Property 5: Invalid moves return False**
  - **Validates: Requirements 3.3**
  - Generate random invalid moves
  - Verify all return False

- [ ]* 5.3 Write property test for board updates
  - **Property 7: Valid moves update board**
  - **Validates: Requirements 4.1**
  - Generate random valid moves
  - Verify board is updated at correct position

- [ ]* 5.4 Write property test for correct mark placement
  - **Property 8: Moves place correct player mark**
  - **Validates: Requirements 4.2**
  - Generate random moves for both X and O
  - Verify correct mark is placed

- [ ]* 5.5 Write property test for player switching
  - **Property 9: Valid moves switch players**
  - **Validates: Requirements 4.4**
  - Generate random valid moves
  - Verify player switches from X to O or O to X

- [ ]* 5.6 Write property test for move counter
  - **Property 10: Moves increment counter**
  - **Validates: Requirements 4.5**
  - Generate random valid moves
  - Verify moves_made increments by 1

- [ ]* 5.7 Write property test for invalid move state preservation
  - **Property 16: Invalid moves preserve player turn**
  - **Validates: Requirements 8.3**
  - Generate random invalid moves
  - Verify current player remains unchanged

- [x] 6. Implement switch_player method
  - Create `_switch_player` private method
  - Change current_player from 'X' to 'O' or 'O' to 'X'
  - Add comment explaining player alternation
  - _Requirements: 4.4, 8.2_

- [ ]* 6.1 Write unit tests for player switching
  - Test switching from 'X' to 'O'
  - Test switching from 'O' to 'X'
  - _Requirements: 4.4, 8.2_

- [x] 7. Implement win detection method
  - Create `check_winner` method
  - Check all 3 rows for three matching marks using a loop
  - Check all 3 columns for three matching marks using a loop
  - Check main diagonal (positions [0][0], [1][1], [2][2])
  - Check anti-diagonal (positions [0][2], [1][1], [2][0])
  - Ensure marks are 'X' or 'O', not empty positions
  - Return winning player ('X' or 'O'), 'Tie' if board full, or None if game continues
  - Set game_over to True when winner found
  - Set winner attribute to the winning player
  - Add educational comments about systematic checking
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3_

- [ ]* 7.1 Write property test for horizontal wins
  - **Property 11: Horizontal wins detected**
  - **Validates: Requirements 5.1**
  - Generate random board states with horizontal wins
  - Verify winner is correctly identified

- [ ]* 7.2 Write property test for vertical wins
  - **Property 12: Vertical wins detected**
  - **Validates: Requirements 5.2**
  - Generate random board states with vertical wins
  - Verify winner is correctly identified

- [ ]* 7.3 Write property test for diagonal wins
  - **Property 13: Diagonal wins detected**
  - **Validates: Requirements 5.3**
  - Generate random board states with diagonal wins
  - Verify winner is correctly identified

- [ ]* 7.4 Write property test for game_over flag on win
  - **Property 14: Win sets game_over flag**
  - **Validates: Requirements 5.4**
  - Generate random winning board states
  - Verify game_over is set to True

- [ ]* 7.5 Write property test for winner attribute on win
  - **Property 15: Win sets winner attribute**
  - **Validates: Requirements 5.5**
  - Generate random winning board states
  - Verify winner attribute is set correctly

- [ ]* 7.6 Write unit tests for tie detection
  - Create a full board with no winner
  - Verify check_winner returns 'Tie'
  - Verify game_over is set to True
  - Verify winner is set to 'Tie'
  - _Requirements: 6.1, 6.2, 6.3_

- [x] 8. Implement is_game_over method
  - Create `is_game_over` method
  - Return the value of self.game_over
  - Add docstring explaining purpose
  - _Requirements: 5.4, 6.2_

- [x] 9. Create get_player_input helper function
  - Create standalone function (not a method) to get user input
  - Accept current_player as parameter
  - Prompt user for position (1-9)
  - Use try-except to handle non-numeric input
  - Validate input is in range 1-9
  - Display helpful error messages for invalid input
  - Loop until valid numeric input in range is received
  - Return the validated position as an integer
  - Add educational comments about input validation
  - _Requirements: 3.5, 9.1, 9.2, 9.4, 9.5_

- [ ]* 9.1 Write unit tests for input validation
  - Test handling of non-numeric input (mock input)
  - Test handling of out-of-range numbers
  - Test valid input returns correct value
  - _Requirements: 3.5, 9.1, 9.2_

- [x] 10. Implement play method (main game loop)
  - Create `play` method to run the complete game
  - Display welcome message explaining OOP version
  - Loop while game is not over
  - Display current board each turn
  - Get player input using helper function
  - Attempt to make move
  - If move invalid, display error and continue loop
  - If move valid, continue to next turn
  - After game ends, display final board
  - Display game result (winner or tie)
  - Add educational comments about game flow
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5_

- [ ]* 10.1 Write integration tests for complete game flow
  - Test a complete game from start to X winning
  - Test a complete game from start to O winning
  - Test a complete game ending in a tie
  - Test multiple invalid moves during a game
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5_

- [x] 11. Create helper functions for messages
  - Create `display_welcome_message` function
  - Display introduction to OOP version
  - Explain what OOP concepts are demonstrated
  - Create `display_game_over_message` function
  - Accept winner parameter
  - Display appropriate message for win or tie
  - Add educational comments about function organization
  - _Requirements: 7.1, 7.5_

- [x] 12. Add main program entry point
  - Add `if __name__ == "__main__":` block
  - Instantiate TicTacToeGame class
  - Call play method
  - Add comments explaining the entry point pattern
  - _Requirements: 7.1_

- [x] 13. Add comprehensive documentation
  - Add file-level docstring explaining OOP version
  - List key OOP concepts demonstrated
  - Add comparison notes with procedural versions
  - Include usage examples in docstrings
  - Add inline comments explaining OOP patterns
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 11.1, 11.2, 11.3, 11.4, 11.5_

- [x] 14. Update main.py launcher
  - Add option to run OOP version in the menu
  - Import and run tictactoe_oop when selected
  - Update menu display to show three options
  - _Requirements: 12.1_

- [x] 15. Update README.md
  - Add section about OOP version
  - Explain what OOP concepts are demonstrated
  - Add instructions for running OOP version
  - Include comparison table of all three versions
  - Add learning progression guide
  - _Requirements: 12.1, 12.2, 12.4_

- [x] 16. Create OOP concepts documentation
  - Create `docs/oop-concepts.md` file
  - Explain classes and objects
  - Explain methods and instance variables
  - Explain encapsulation with examples from the code
  - Explain the __init__ constructor
  - Explain self parameter
  - Include code examples from tictactoe_oop.py
  - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5_

- [ ] 17. Create comparison guide
  - Create `docs/procedural-vs-oop.md` file
  - Side-by-side comparison of procedural and OOP versions
  - Highlight key differences in code organization
  - Explain when to use each approach
  - Show how the same logic is implemented differently
  - Include visual diagrams if helpful
  - _Requirements: 12.1, 12.2_

- [x] 18. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.
