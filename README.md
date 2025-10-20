# Educational Tic-Tac-Toe Game

## Learning Objectives

This project is designed for **week 3 Python learners** who are just beginning to understand fundamental programming concepts. By working through this project, you will learn:

- **Variables and Data Types**: How to store and work with different types of information
- **Lists and Nested Lists**: How to organize data in collections and work with 2D structures
- **Dictionaries**: How to use key-value pairs to store and access data
- **Loops**: How to repeat code efficiently using for loops and while loops
- **Conditionals**: How to make decisions in your code using if/elif/else statements
- **Input Validation**: How to handle user input safely and provide helpful error messages
- **Problem Solving**: How to break down a complex problem into manageable steps

## What You'll Learn

### Python Concepts Covered
- **Basic Data Types**: strings, integers, booleans
- **Lists**: creating, accessing, and modifying list elements
- **Nested Lists**: working with lists inside lists (2D arrays)
- **Dictionaries**: creating and accessing key-value pairs
- **For Loops**: iterating through collections and using range()
- **While Loops**: repeating code until a condition changes
- **Conditionals**: making decisions with if/elif/else statements
- **Try/Except**: basic error handling for user input
- **String Formatting**: displaying information clearly to users

### Data Structures Demonstrated
This project shows you **two different ways** to solve the same problem:
1. **Nested Lists Approach**: Using lists inside lists to represent the game board
2. **Dictionary Approach**: Using numbered keys to represent board positions

Both implementations produce identical gameplay, allowing you to compare and understand different programming approaches.

### Problem-Solving Approaches Shown
- Breaking complex problems into smaller steps
- Input validation and error handling
- Game state management
- Win condition checking
- User interface design

## Prerequisites

Before starting this project, you should understand:
- How to create and run Python files
- Basic variable assignment (`x = 5`)
- Simple print statements (`print("Hello")`)
- Basic input collection (`input("Enter something: ")`)

## How to Run the Code

### Option 1: Run the Game Launcher (Recommended)
```bash
python main.py
```
This will show you a menu where you can choose between the two different implementations.

### Option 2: Run Individual Versions
```bash
# Run the nested lists version
python tictactoe_lists.py

# Run the dictionary version  
python tictactoe_dict.py
```

### What to Expect When Running
1. You'll see a welcome message explaining the game
2. The game board will display with numbers 1-9 showing available positions
3. Players take turns entering numbers to place their X or O
4. The game will check for wins or ties after each move
5. When the game ends, you can choose to play again

### How to Interact with the Program
- Enter numbers 1-9 to place your mark on the board
- Follow the on-screen prompts
- If you make a mistake, the game will explain what went wrong
- Press Ctrl+C to exit at any time

## Code Structure

### Main Files
- **`main.py`** - Game launcher with menu to choose between versions
- **`tictactoe_lists.py`** - Complete game using nested lists for the board
- **`tictactoe_dict.py`** - Complete game using a dictionary for the board

### Documentation Files
- **`docs/python-concepts.md`** - Detailed explanations of Python concepts used
- **`docs/data-structures-guide.md`** - Comparison of lists vs dictionaries
- **`docs/exercises.md`** - Practice exercises and extensions to try
- **`docs/common-errors.md`** - Common mistakes and how to fix them

### How the Files Work Together
1. **Start with `main.py`** - This gives you a menu to choose which version to play
2. **Try both versions** - Compare how lists and dictionaries work differently
3. **Read the documentation** - Learn about the concepts being demonstrated
4. **Try the exercises** - Practice modifying the code to reinforce learning

### Which File to Start With
**For Playing**: Start with `main.py` to see the menu and choose a version
**For Learning**: Read this README first, then look at `tictactoe_lists.py` to see the code with extensive comments

## Project Structure
```
tictactoe/
├── README.md                    # This file - start here!
├── main.py                      # Game launcher with menu
├── tictactoe_lists.py          # Nested lists implementation
├── tictactoe_dict.py           # Dictionary implementation
├── docs/                       # Educational documentation
│   ├── python-concepts.md      # Python concepts explained
│   ├── data-structures-guide.md # Lists vs dictionaries guide
│   ├── exercises.md            # Practice exercises
│   └── common-errors.md        # Debugging help
└── .kiro/                      # Project specifications
    ├── specs/                  # Design documents
    └── steering/               # Coding standards
```

## Exercises and Extensions

### Beginner Exercises
1. **Change the Starting Player**: Make 'O' go first instead of 'X'
2. **Add a Move Counter**: Keep track of how many moves have been made
3. **Customize Messages**: Change the welcome message and player prompts
4. **Add Color**: Use simple text formatting to make X and O different colors

### Intermediate Exercises
1. **Improve Error Messages**: Make error messages more specific and helpful
2. **Add Input Validation**: Handle more types of invalid input
3. **Create a Score System**: Keep track of wins across multiple games
4. **Add Game Statistics**: Show how many games were played, won, tied

### Advanced Extensions
1. **Add a Computer Player**: Make the computer play against the human
2. **Create Different Difficulty Levels**: Easy, medium, hard computer opponents
3. **Implement a Tournament Mode**: Best of 3, 5, or 7 games
4. **Add a Replay System**: Save and replay previous games

See `docs/exercises.md` for detailed instructions and hints for each exercise.

## Common Issues and Solutions

### "IndexError: list index out of range"
**Problem**: Trying to access a position that doesn't exist in the list
**Solution**: Remember that lists start counting at 0, not 1. Position 1 on the board is actually `board[0][0]`

### "TypeError: list indices must be integers, not str"
**Problem**: Trying to use a string as a list position
**Solution**: Convert user input to integer using `int(input())`

### "KeyError" (in dictionary version)
**Problem**: Trying to access a dictionary key that doesn't exist
**Solution**: Check that the key exists before accessing it

### Game doesn't end when someone wins
**Problem**: Win detection logic might have an error
**Solution**: Check that you're comparing the right positions and using the correct operators

See `docs/common-errors.md` for more detailed troubleshooting help.

## Educational Philosophy

This project follows these educational principles:

### Clarity Over Efficiency
The code prioritizes being easy to understand over being fast or clever. Every line is explained with comments.

### No Advanced Features
We only use basic Python concepts that week 3 students should know. No functions, classes, or advanced features that might confuse beginners.

### Extensive Documentation
Every variable, loop, and decision is explained in detail. Comments teach not just what the code does, but why it works that way.

### Comparative Learning
By showing two different approaches to the same problem, students can see that there are multiple ways to solve programming challenges.

### Progressive Complexity
The code starts simple and builds up complexity gradually, reinforcing concepts through repetition and practice.

## Getting Help

If you get stuck or have questions:

1. **Read the error message carefully** - Python error messages often tell you exactly what's wrong
2. **Check the comments** - The code has extensive comments explaining each step
3. **Look at the documentation** - The `docs/` folder has detailed explanations
4. **Try the exercises** - Start with simple modifications to build confidence
5. **Compare the two versions** - See how the same logic works with different data structures

Remember: making mistakes is part of learning! Don't be afraid to experiment and break things - that's how you learn what works and what doesn't.

## Next Steps

After completing this project, you'll be ready to:
- Work with more complex data structures
- Learn about functions and code organization
- Tackle larger programming projects
- Understand object-oriented programming concepts

Happy coding! 🎮