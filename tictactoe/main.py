"""
Tic-Tac-Toe Game Launcher - Educational Menu System

This file provides a menu system that allows students to choose between
two different implementations of tic-tac-toe: one using nested lists
and one using dictionaries. This demonstrates how the same problem
can be solved using different data structures.

Educational Focus:
This launcher helps students understand the learning objectives of each
version and encourages them to try both approaches for comparison.

Author: Educational Tic-Tac-Toe Project
Date: 2024
Python Level: Beginner (Week 3)
Purpose: Game Selection and Educational Guidance
"""

import subprocess
import sys

# ============================================
# WELCOME AND INTRODUCTION SECTION
# ============================================

print("=" * 60)
print("    EDUCATIONAL TIC-TAC-TOE GAME LAUNCHER")
print("=" * 60)
print()
print("Welcome to the Educational Tic-Tac-Toe Project!")
print()
print("This project demonstrates two different ways to solve the same problem")
print("using different Python data structures. Both games work identically,")
print("but they organize and access data in different ways.")
print()
print("Learning Objectives:")
print("- Understand nested lists vs dictionaries")
print("- See how data structure choice affects code complexity")
print("- Compare different approaches to the same problem")
print("- Practice fundamental Python concepts")
print()

# ============================================
# MAIN MENU LOOP
# ============================================

# keep_running: Boolean to control the main menu loop
# We'll keep showing the menu until the user chooses to exit
keep_running = True

while keep_running:
    
    print("-" * 60)
    print("CHOOSE YOUR LEARNING ADVENTURE:")
    print("-" * 60)
    print()
    print("1. Nested Lists Version")
    print("   → Learn about: 2D arrays, [row][column] indexing, nested loops")
    print("   → Best for: Understanding systematic data organization")
    print("   → File: tictactoe_lists.py")
    print()
    print("2. Dictionary Version") 
    print("   → Learn about: Key-value pairs, direct access, hash tables")
    print("   → Best for: Understanding flexible data mapping")
    print("   → File: tictactoe_dict.py")
    print()
    print("3. View Documentation")
    print("   → Read about Python concepts and data structure comparisons")
    print("   → Includes exercises and troubleshooting guides")
    print()
    print("4. Exit")
    print("   → Quit the launcher")
    print()
    
    # Get user choice with input validation
    choice = input("Enter your choice (1-4): ").strip()
    print()
    
    # ============================================
    # CHOICE PROCESSING SECTION
    # ============================================
    
    if choice == '1':
        print("Starting Nested Lists Version...")
        print("=" * 40)
        print("WHAT YOU'LL LEARN:")
        print("- How nested lists work (lists inside lists)")
        print("- Converting position numbers to [row][column] coordinates")
        print("- Using nested loops to check win conditions")
        print("- Systematic approach to 2D data structures")
        print("=" * 40)
        print()
        
        try:
            # Run the nested lists version
            subprocess.run([sys.executable, 'tictactoe_lists.py'], check=True)
        except subprocess.CalledProcessError:
            print("Error: Could not run tictactoe_lists.py")
            print("Make sure the file exists in the current directory.")
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
        
        print()
        print("Game completed! You experienced the nested lists approach.")
        print()
        
    elif choice == '2':
        print("Starting Dictionary Version...")
        print("=" * 40)
        print("WHAT YOU'LL LEARN:")
        print("- How dictionaries store key-value pairs")
        print("- Direct position access without coordinate conversion")
        print("- Explicit win condition checking")
        print("- Flexible approach to data mapping")
        print("=" * 40)
        print()
        
        try:
            # Run the dictionary version
            subprocess.run([sys.executable, 'tictactoe_dict.py'], check=True)
        except subprocess.CalledProcessError:
            print("Error: Could not run tictactoe_dict.py")
            print("Make sure the file exists in the current directory.")
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
        
        print()
        print("Game completed! You experienced the dictionary approach.")
        print()
        
    elif choice == '3':
        print("EDUCATIONAL DOCUMENTATION:")
        print("=" * 40)
        print()
        print("Available documentation files:")
        print("- README.md - Project overview and getting started guide")
        print("- docs/python-concepts.md - Detailed Python concept explanations")
        print("- docs/data-structures-guide.md - Lists vs dictionaries comparison")
        print()
        print("To read these files:")
        print("- Open them in a text editor")
        print("- Or use: cat filename.md (on Mac/Linux)")
        print("- Or use: type filename.md (on Windows)")
        print()
        print("Recommended reading order:")
        print("1. README.md (start here)")
        print("2. docs/python-concepts.md (understand the concepts)")
        print("3. docs/data-structures-guide.md (compare approaches)")
        print("4. Try both game versions")
        print()
        
    elif choice == '4':
        print("Thank you for exploring the Educational Tic-Tac-Toe Project!")
        print()
        print("WHAT YOU'VE LEARNED:")
        print("- Two different approaches to the same problem")
        print("- How data structure choice affects code design")
        print("- Fundamental Python concepts in action")
        print()
        print("NEXT STEPS:")
        print("- Try modifying the code to add new features")
        print("- Experiment with the exercises in the documentation")
        print("- Apply these concepts to your own projects")
        print()
        print("Happy coding! 🎮")
        keep_running = False
        
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        print()

print()
print("Launcher closed.")