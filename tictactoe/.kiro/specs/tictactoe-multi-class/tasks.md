# Implementation Plan: Tic-Tac-Toe Multi-Class Version

- [x] 1. Set up project structure and configuration
  - Create new file `tictactoe_multiclass.py` with file header
  - Add BOARD_SIZE configuration constant at the top
  - Add comprehensive docstring explaining multi-class design
  - Include section headers for each class
  - _Requirements: 1.1, 10.1_

- [x] 2. Implement Player class
  - Define Player class with comprehensive docstring
  - Implement `__init__` method with mark and optional name
  - Implement `get_mark()` method
  - Implement `get_name()` method
  - Implement `__str__()` method for string representation
  - Add educational comments explaining data classes
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5_

- [x] 3. Implement Board class initialization
  - Define Board class with comprehensive docstring
  - Implement `__init__` method accepting size parameter
  - Initialize grid dynamically based on size
  - Populate grid with coordinate strings (e.g., "00", "11", "22")
  - Add educational comments explaining dynamic initialization
  - _Requirements: 1.2, 1.3, 2.1, 3.1_

- [x] 4. Implement Board display method
  - Create `display()` method
  - Use nested loops to iterate through grid
  - Format output with proper spacing and separators
  - Ensure formatting works for any board size
  - Add educational comments explaining dynamic display
  - _Requirements: 2.2, 2.3, 2.4, 2.5, 8.1, 8.2, 8.3, 8.4, 8.5_

- [x] 5. Implement Board coordinate parsing
  - Create `_parse_coordinate()` private method
  - Validate coordinate format (two digits)
  - Parse row and column from coordinate string
  - Validate range based on board size
  - Return tuple (row, col) or None if invalid
  - Add educational comments explaining validation
  - _Requirements: 2.4, 6.1, 6.2_

- [x] 6. Implement Board move validation
  - Create `is_valid_move()` method
  - Use `_parse_coordinate()` to validate format and range
  - Check if cell is already occupied
  - Return True for valid moves, False otherwise
  - Add educational comments explaining validation layers
  - _Requirements: 3.3, 6.2, 6.3_

- [x] 7. Implement Board mark placement
  - Create `place_mark()` method
  - Accept coordinate and mark parameters
  - Parse coordinate and validate
  - Update grid at specified position
  - Return True if successful
  - Add educational comments explaining grid manipulation
  - _Requirements: 3.4_

- [x] 8. Implement Board helper method for fullness check
  - Create `is_full()` method
  - Check if all cells contain marks (not coordinates)
  - Return True if board is full
  - Add educational comments
  - _Requirements: 7.4_

- [x] 9. Implement Board row win detection
  - Create `_check_rows()` private method
  - Loop through all rows dynamically
  - Check if all cells in a row match
  - Skip rows with empty cells (coordinates)
  - Return winning mark or None
  - Add educational comments explaining dynamic checking
  - _Requirements: 7.1_

- [x] 10. Implement Board column win detection
  - Create `_check_columns()` private method
  - Loop through all columns dynamically
  - Check if all cells in a column match
  - Skip columns with empty cells
  - Return winning mark or None
  - Add educational comments
  - _Requirements: 7.2_

- [x] 11. Implement Board diagonal win detection
  - Create `_check_diagonals()` private method
  - Check main diagonal (top-left to bottom-right)
  - Check anti-diagonal (top-right to bottom-left)
  - Both checks must work for any board size
  - Return winning mark or None
  - Add educational comments explaining diagonal logic
  - _Requirements: 7.3_

- [x] 12. Implement Board check_winner method
  - Create `check_winner()` method
  - Call `_check_rows()`, `_check_columns()`, `_check_diagonals()`
  - If winner found, return the mark
  - If board is full with no winner, return 'Tie'
  - Otherwise return None
  - Add educational comments explaining win detection coordination
  - _Requirements: 3.5, 7.4_

- [x] 13. Implement Game class initialization
  - Define Game class with comprehensive docstring
  - Implement `__init__` method accepting board_size parameter
  - Create Board instance with specified size
  - Create two Player instances (X and O)
  - Initialize current_player to player_x
  - Initialize game_over to False
  - Initialize winner to None
  - Add educational comments explaining composition
  - _Requirements: 5.1, 5.2, 9.1_

- [x] 14. Implement Game player switching
  - Create `switch_player()` method
  - Toggle between player_x and player_o
  - Update current_player
  - Add educational comments
  - _Requirements: 5.3_

- [x] 15. Implement Game input handling
  - Create `get_player_input()` method
  - Prompt current player for coordinate
  - Use try-except for non-numeric input
  - Validate format (two digits)
  - Loop until valid format received
  - Return validated coordinate string
  - Add educational comments explaining input validation
  - _Requirements: 6.1, 6.2, 6.4, 6.5_

- [x] 16. Implement Game welcome message
  - Create `display_welcome()` method
  - Display banner and introduction
  - Explain multi-class design
  - Show coordinate system explanation
  - Display board size information
  - Add educational comments
  - _Requirements: 10.2, 10.3_

- [x] 17. Implement Game result display
  - Create `display_result()` method
  - Display final board state
  - Announce winner or tie
  - Thank player for playing
  - Add educational comments
  - _Requirements: 12.2, 12.3_

- [x] 18. Implement Game main loop
  - Create `play()` method
  - Call `display_welcome()`
  - Loop while game not over
  - Display board using `self.board.display()`
  - Get player input using `get_player_input()`
  - Validate move using `self.board.is_valid_move()`
  - Place mark using `self.board.place_mark()`
  - Check winner using `self.board.check_winner()`
  - Switch players if game continues
  - Call `display_result()` when game ends
  - Add educational comments explaining class coordination
  - _Requirements: 5.3, 5.4, 5.5, 9.2, 9.3, 9.4, 9.5_

- [x] 19. Add main program entry point
  - Add `if __name__ == "__main__":` block
  - Create Game instance with BOARD_SIZE
  - Call play() method
  - Add educational comments explaining entry point
  - _Requirements: 12.1_

- [x] 20. Add comprehensive documentation
  - Ensure all classes have detailed docstrings
  - Ensure all methods have detailed docstrings
  - Add comments explaining class interactions
  - Add comments explaining composition pattern
  - Add comments explaining separation of concerns
  - Include examples in docstrings
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5_

- [x] 21. Test with different board sizes
  - Test with 3x3 board (default)
  - Test with 4x4 board
  - Test with 5x5 board
  - Verify win detection works for all sizes
  - Verify display formatting works for all sizes
  - Verify coordinate validation works for all sizes
  - _Requirements: 1.1, 1.2, 1.4, 1.5, 11.1_

- [x] 22. Update main.py launcher
  - Add option 4 for multi-class version
  - Update menu to show four game versions
  - Add launch code for tictactoe_multiclass.py
  - Update choice validation to accept 1-6
  - Shift "View Documentation" and "Exit" options
  - _Requirements: 12.1_

- [x] 23. Update README.md
  - Add section about multi-class version
  - Explain advanced OOP concepts demonstrated
  - Add to comparison table
  - Update learning progression guide
  - Add instructions for changing board size
  - _Requirements: 12.4_

- [x] 24. Create multi-class design documentation
  - Create `docs/multi-class-design.md` file
  - Explain separation of concerns
  - Explain composition pattern
  - Show class interaction diagrams
  - Compare single-class vs multi-class design
  - Include code examples from tictactoe_multiclass.py
  - _Requirements: 10.4, 10.5_

- [x] 25. Final checkpoint - Test complete game
  - Play complete game with 3x3 board
  - Test all win conditions (rows, columns, diagonals)
  - Test tie condition
  - Test error handling
  - Change BOARD_SIZE to 4 and test again
  - Ensure all tests pass, ask the user if questions arise
