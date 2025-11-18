"""
Tic-Tac-Toe Game - Multi-Class Object-Oriented Version

This file demonstrates advanced object-oriented programming through a multi-class
design. Unlike the single-class OOP version, this implementation separates concerns
into multiple cooperating classes, each with a single, well-defined responsibility.

Key Advanced OOP Concepts Demonstrated:
- Multi-Class Design: Breaking a problem into multiple classes
- Separation of Concerns: Each class has one clear responsibility
- Composition: Objects contain and coordinate other objects (HAS-A relationships)
- Delegation: Objects delegate work to other objects
- Encapsulation: Internal details are hidden behind public interfaces
- Scalability: Code adapts to different board sizes without modification
- Extensibility: Easy to add new features by extending classes

Architecture Overview:
    Game (Orchestrator)
    ├── Board (Grid Manager)
    └── Player (Data Holder) x2

Class Responsibilities:
- Board: Manages the game grid, validates moves, detects wins
- Player: Represents a player with their mark and optional name
- Game: Coordinates gameplay, manages turns, handles user interaction

Key Design Differences from Single-Class Version:
1. Separation: Logic is distributed across specialized classes
2. Composition: Game contains Board and Player objects
3. Scalability: Board size is configurable via a single constant
4. Coordinates: Uses row-column coordinates (e.g., "00", "11", "22")
5. Flexibility: Easy to extend with new features or game variations

Configurable Board Size:
Change BOARD_SIZE below to play with different board dimensions.
All game logic automatically adapts to the specified size.

Author: Educational Python Project
Python Level: Advanced OOP Learners
"""

# ============================================
# CONFIGURATION
# ============================================

# Board size configuration - change this value to modify the game board size
# Default: 3 for standard 3x3 tic-tac-toe
# Try: 4 for 4x4, 5 for 5x5, or any positive integer
BOARD_SIZE = 5


# ============================================
# PLAYER CLASS
# ============================================

class Player:
    """
    Represents a player in the tic-tac-toe game.
    
    This class demonstrates:
    - Simple data classes in OOP
    - Encapsulation of player-specific information
    - Modeling real-world entities as objects
    - Getter methods for accessing data
    
    The Player class is intentionally simple - it just holds data about
    a player. This shows that not all classes need complex logic; some
    classes exist primarily to organize and encapsulate data.
    
    In a multi-class design, this separation allows the Game class to
    work with Player objects without knowing the internal details of
    how player data is stored.
    
    Attributes:
        mark (str): The player's mark ('X' or 'O')
        name (str): Optional player name (defaults to mark if not provided)
    
    Example:
        >>> player = Player('X', 'Alice')
        >>> player.get_mark()
        'X'
        >>> player.get_name()
        'Alice'
        >>> str(player)
        'Alice'
    """
    
    def __init__(self, mark, name=None):
        """
        Initialize a player with a mark and optional name.
        
        This constructor demonstrates:
        - Required parameters (mark)
        - Optional parameters with defaults (name=None)
        - Instance variable initialization
        
        Args:
            mark (str): The player's mark ('X' or 'O')
            name (str): Optional player name. If not provided, uses mark as name.
        
        Example:
            >>> player1 = Player('X')  # Name defaults to 'X'
            >>> player2 = Player('O', 'Bob')  # Name is 'Bob'
        """
        # Store the player's mark (X or O)
        # This is the symbol that will appear on the board
        self.mark = mark
        
        # Store the player's name
        # If no name provided, use the mark as the name
        # This allows for both named and unnamed players
        self.name = name if name is not None else mark
    
    def get_mark(self):
        """
        Get the player's mark.
        
        This is a getter method - it provides controlled access to
        the player's mark. Using a method instead of direct access
        demonstrates encapsulation.
        
        Returns:
            str: The player's mark ('X' or 'O')
        
        Example:
            >>> player = Player('X')
            >>> player.get_mark()
            'X'
        """
        return self.mark
    
    def get_name(self):
        """
        Get the player's name.
        
        Returns the player's name, or their mark if no name was set.
        This method demonstrates how objects can provide convenient
        access to their data.
        
        Returns:
            str: The player's name or mark
        
        Example:
            >>> player = Player('X', 'Alice')
            >>> player.get_name()
            'Alice'
        """
        return self.name
    
    def __str__(self):
        """
        String representation of the player.
        
        This special method (also called a "dunder" method for double
        underscore) defines how the player appears when converted to
        a string. This is called automatically by print() and str().
        
        Returns:
            str: The player's name
        
        Example:
            >>> player = Player('X', 'Alice')
            >>> print(player)
            Alice
            >>> str(player)
            'Alice'
        """
        return self.name


# ============================================
# BOARD CLASS
# ============================================

class Board:
    """
    Manages the tic-tac-toe game board.
    
    This class demonstrates:
    - Encapsulation: Grid is private, accessed through methods
    - Single Responsibility: Only handles board operations
    - Scalability: Works with any board size
    - Dynamic initialization: Grid size determined at runtime
    
    The Board class is responsible for everything related to the game grid:
    - Storing the current state
    - Displaying the board
    - Validating moves
    - Placing marks
    - Detecting wins and ties
    
    The Board doesn't know about Players or Game rules - it just manages
    the grid. This separation allows the Board to be reused in different
    contexts or extended with new features without affecting other classes.
    
    Attributes:
        size (int): The dimension of the square board (e.g., 3 for 3x3)
        grid (list): 2D nested list storing the board state
    
    Example:
        >>> board = Board(3)
        >>> board.display()
         00 | 01 | 02
        ---------------
         10 | 11 | 12
        ---------------
         20 | 21 | 22
    """
    
    def __init__(self, size=3):
        """
        Initialize the board with the specified size.
        
        This constructor demonstrates:
        - Dynamic data structure creation
        - Nested loops for 2D initialization
        - Default parameter values
        - Coordinate-based cell labeling
        
        The board is initialized with each cell containing its coordinate
        as a two-digit string (e.g., "00", "11", "22"). This makes it easy
        for players to see available positions and understand the coordinate
        system.
        
        Args:
            size (int): The dimension of the square board (default 3)
        
        Example:
            >>> board = Board(3)  # Creates 3x3 board
            >>> board = Board(4)  # Creates 4x4 board
        """
        # Store the board size
        # This is used throughout the class to make all operations dynamic
        self.size = size
        
        # Initialize an empty list to hold the grid
        # We'll build this as a 2D nested list (list of lists)
        self.grid = []
        
        # Create the grid dynamically based on the size
        # Outer loop: create each row
        for row in range(self.size):
            # Create an empty list for this row
            row_list = []
            
            # Inner loop: create each cell in this row
            for col in range(self.size):
                # Create a coordinate string for this cell
                # Format: "row col" as two digits (e.g., "00", "11", "22")
                # This coordinate will be displayed until a player marks this cell
                coordinate = f"{row}{col}"
                row_list.append(coordinate)
            
            # Add this completed row to the grid
            self.grid.append(row_list)
        
        # At this point, self.grid looks like:
        # [['00', '01', '02'],
        #  ['10', '11', '12'],
        #  ['20', '21', '22']]
        # (for a 3x3 board)
    
    def display(self):
        """
        Display the current board state.
        
        Shows the board with proper formatting including:
        - Coordinates for empty cells
        - Player marks (X or O) for occupied cells
        - Vertical separators between columns
        - Horizontal separators between rows
        
        The display adapts automatically to any board size.
        Padding ensures alignment regardless of cell content length.
        """
        for row in range(self.size):
            # Display each cell in the row
            for col in range(self.size):
                cell = self.grid[row][col]
                # Pad to ensure consistent width (2 characters)
                # Coordinates are already 2 chars ("00"), marks need padding
                cell_display = cell.ljust(2)  # Left-justify and pad to 2 chars
                # Add spacing for alignment
                print(f" {cell_display} ", end='')
                # Add vertical separator between columns (but not after last column)
                if col < self.size - 1:
                    print("|", end='')
            print()  # New line after each row
            
            # Add horizontal separator between rows (but not after last row)
            if row < self.size - 1:
                # Each cell is " XX " (4 chars), separator is "|" (1 char)
                # Total: (4 * size) + (size - 1) for separators
                separator = "-" * (4 * self.size + (self.size - 1))
                print(separator)
    
    def _parse_coordinate(self, coordinate):
        """Parse and validate a coordinate string."""
        if len(coordinate) != 2 or not coordinate.isdigit():
            return None
        row, col = int(coordinate[0]), int(coordinate[1])
        if row >= self.size or col >= self.size:
            return None
        return (row, col)
    
    def is_valid_move(self, coordinate):
        """Check if a move is valid."""
        parsed = self._parse_coordinate(coordinate)
        if parsed is None:
            return False
        row, col = parsed
        # Cell is valid if it still contains a coordinate (not a mark)
        return len(self.grid[row][col]) == 2
    
    def place_mark(self, coordinate, mark):
        """Place a mark at the specified coordinate."""
        parsed = self._parse_coordinate(coordinate)
        if parsed is None:
            return False
        row, col = parsed
        self.grid[row][col] = mark
        return True
    
    def is_full(self):
        """Check if board is full."""
        for row in range(self.size):
            for col in range(self.size):
                if len(self.grid[row][col]) == 2:  # Still a coordinate
                    return False
        return True
    
    def _check_rows(self):
        """Check all rows for a win."""
        for row in range(self.size):
            first = self.grid[row][0]
            if len(first) == 2:  # Coordinate, not mark
                continue
            if all(self.grid[row][col] == first for col in range(self.size)):
                return first
        return None
    
    def _check_columns(self):
        """Check all columns for a win."""
        for col in range(self.size):
            first = self.grid[0][col]
            if len(first) == 2:
                continue
            if all(self.grid[row][col] == first for row in range(self.size)):
                return first
        return None
    
    def _check_diagonals(self):
        """Check both diagonals for a win."""
        # Main diagonal
        first = self.grid[0][0]
        if len(first) == 1:
            if all(self.grid[i][i] == first for i in range(self.size)):
                return first
        # Anti-diagonal
        first = self.grid[0][self.size - 1]
        if len(first) == 1:
            if all(self.grid[i][self.size - 1 - i] == first for i in range(self.size)):
                return first
        return None
    
    def check_winner(self):
        """Check for a winner or tie."""
        winner = self._check_rows()
        if winner:
            return winner
        winner = self._check_columns()
        if winner:
            return winner
        winner = self._check_diagonals()
        if winner:
            return winner
        if self.is_full():
            return 'Tie'
        return None


# ============================================
# GAME CLASS
# ============================================

class Game:
    """Orchestrates the tic-tac-toe game."""
    
    def __init__(self, board_size=3):
        """Initialize game with board and players."""
        self.board = Board(board_size)
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.current_player = self.player_x
        self.game_over = False
        self.winner = None
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = self.player_o if self.current_player == self.player_x else self.player_x
    
    def get_player_input(self):
        """Get and validate coordinate input."""
        while True:
            try:
                coord = input(f"Player {self.current_player}, enter coordinate (e.g., '11'): ")
                if len(coord) == 2 and coord.isdigit():
                    return coord
                print("Invalid format! Enter two digits (e.g., '00', '11', '22')")
            except:
                print("Invalid input! Enter two digits.")
    
    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "=" * 60)
        print("Tic-Tac-Toe - Multi-Class OOP Version")
        print("=" * 60)
        print(f"\nBoard Size: {self.board.size}x{self.board.size}")
        print("Enter coordinates as two digits (row, column)")
        print("Example: '00' for top-left, '11' for center, '22' for bottom-right")
        print("=" * 60 + "\n")
    
    def display_result(self):
        """Display game result."""
        print("\n" + "=" * 60)
        print("GAME OVER!")
        print("=" * 60)
        print("\nFinal board:")
        self.board.display()
        if self.winner == 'Tie':
            print("\nIt's a tie!")
        else:
            print(f"\nPlayer {self.winner} wins!")
        print("\n" + "=" * 60 + "\n")
    
    def play(self):
        """Run the main game loop."""
        self.display_welcome()
        
        while not self.game_over:
            self.board.display()
            print()
            
            coord = self.get_player_input()
            
            if not self.board.is_valid_move(coord):
                print(f"Invalid move! Cell {coord} is occupied or invalid.\n")
                continue
            
            self.board.place_mark(coord, self.current_player.get_mark())
            
            result = self.board.check_winner()
            if result:
                self.game_over = True
                self.winner = result
            else:
                self.switch_player()
        
        self.display_result()


# ============================================
# MAIN PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    """
    Main entry point for the multi-class tic-tac-toe game.
    
    Creates a Game instance with the configured board size and starts play.
    """
    game = Game(BOARD_SIZE)
    game.play()
