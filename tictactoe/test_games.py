"""
Educational Tic-Tac-Toe Testing Suite

This file demonstrates how to systematically test the tic-tac-toe games.
It serves both as documentation of our testing process and as a practical
example of how to write test code for beginners.

Educational Focus:
- Shows how to simulate game inputs programmatically
- Demonstrates systematic testing approaches
- Provides examples of test case documentation
- Teaches validation and verification concepts

Author: Educational Tic-Tac-Toe Project
Date: 2024
Python Level: Beginner (Week 3) - Testing Concepts
Purpose: Automated Testing Documentation
"""

import subprocess
import sys
import os
from io import StringIO
import contextlib

# ============================================
# TESTING UTILITIES SECTION
# ============================================
# These functions help us run tests and capture results

def simulate_game_input(moves_list):
    """
    Convert a list of moves into a string that simulates user input.
    
    Args:
        moves_list: List of moves like [5, 1, 3, 7, 9]
    
    Returns:
        String with newlines that simulates typing each move
    """
    return '\n'.join(str(move) for move in moves_list) + '\n'

def run_game_with_input(game_file, input_string):
    """
    Run a game file with simulated input and capture the output.
    
    Args:
        game_file: Name of the Python file to run
        input_string: Simulated user input
    
    Returns:
        Tuple of (stdout, stderr, return_code)
    """
    try:
        result = subprocess.run(
            [sys.executable, game_file],
            input=input_string,
            capture_output=True,
            text=True,
            timeout=30  # Prevent hanging
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Test timed out", -1
    except Exception as e:
        return "", f"Error running test: {e}", -1

def check_win_in_output(output, expected_winner):
    """
    Check if the game output contains the expected winner announcement.
    
    Args:
        output: Game output string
        expected_winner: 'X', 'O', or 'Tie'
    
    Returns:
        Boolean indicating if the expected winner was found
    """
    output_lower = output.lower()
    
    if expected_winner == 'X':
        return 'player x wins' in output_lower or 'x wins' in output_lower
    elif expected_winner == 'O':
        return 'player o wins' in output_lower or 'o wins' in output_lower
    elif expected_winner == 'Tie':
        return 'tie' in output_lower or 'draw' in output_lower
    
    return False

def print_test_header(test_name):
    """Print a formatted test header."""
    print("\n" + "=" * 60)
    print(f"TEST: {test_name}")
    print("=" * 60)

def print_test_result(passed, details=""):
    """Print formatted test results."""
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"Result: {status}")
    if details:
        print(f"Details: {details}")
    print("-" * 60)

# ============================================
# TEST CASE DEFINITIONS
# ============================================
# Each test case documents a specific scenario we want to verify

class TestCase:
    """
    A test case represents one specific scenario to test.
    This helps us organize and document our testing approach.
    """
    
    def __init__(self, name, moves, expected_winner, description):
        self.name = name
        self.moves = moves
        self.expected_winner = expected_winner
        self.description = description
    
    def __str__(self):
        return f"{self.name}: {self.description}"

# Define our test cases based on the testing guide
TEST_CASES = [
    TestCase(
        name="Basic Diagonal Win",
        moves=[5, 1, 3, 7, 9],  # X: 5,3,9 (diagonal), O: 1,7
        expected_winner='X',
        description="X wins with main diagonal (positions 1,5,9)"
    ),
    
    TestCase(
        name="Top Row Win",
        moves=[1, 4, 2, 5, 3],  # X: 1,2,3 (top row), O: 4,5
        expected_winner='X',
        description="X wins with top row (positions 1,2,3)"
    ),
    
    TestCase(
        name="Middle Row Win",
        moves=[4, 1, 5, 2, 6],  # X: 4,5,6 (middle row), O: 1,2
        expected_winner='X',
        description="X wins with middle row (positions 4,5,6)"
    ),
    
    TestCase(
        name="Bottom Row Win",
        moves=[7, 1, 8, 2, 9],  # X: 7,8,9 (bottom row), O: 1,2
        expected_winner='X',
        description="X wins with bottom row (positions 7,8,9)"
    ),
    
    TestCase(
        name="Left Column Win",
        moves=[1, 2, 4, 3, 7],  # X: 1,4,7 (left column), O: 2,3
        expected_winner='X',
        description="X wins with left column (positions 1,4,7)"
    ),
    
    TestCase(
        name="Middle Column Win",
        moves=[2, 1, 5, 3, 8],  # X: 2,5,8 (middle column), O: 1,3
        expected_winner='X',
        description="X wins with middle column (positions 2,5,8)"
    ),
    
    TestCase(
        name="Right Column Win",
        moves=[3, 1, 6, 2, 9],  # X: 3,6,9 (right column), O: 1,2
        expected_winner='X',
        description="X wins with right column (positions 3,6,9)"
    ),
    
    TestCase(
        name="Anti-Diagonal Win",
        moves=[3, 1, 5, 2, 7],  # X: 3,5,7 (anti-diagonal), O: 1,2
        expected_winner='X',
        description="X wins with anti-diagonal (positions 3,5,7)"
    ),
    
    TestCase(
        name="O Wins Test",
        moves=[1, 5, 2, 4, 8, 6],  # O: 5,4,6 (middle row), X: 1,2,8
        expected_winner='O',
        description="O wins with middle row (positions 4,5,6)"
    ),
    
    TestCase(
        name="Tie Game",
        moves=[1, 2, 3, 4, 5, 6, 8, 7, 9],  # Fill board without winner
        expected_winner='Tie',
        description="Game ends in a tie with full board"
    ),
    
    TestCase(
        name="Minimum Moves Win",
        moves=[1, 4, 2, 5, 3],  # X wins in 5 moves (fastest possible)
        expected_winner='X',
        description="Fastest possible win - X wins in 5 moves"
    )
]

# ============================================
# INPUT VALIDATION TEST CASES
# ============================================
# These test cases check error handling with invalid inputs

INVALID_INPUT_TESTS = [
    {
        'name': 'Letters Instead of Numbers',
        'inputs': ['abc', '5'],  # Try invalid input, then valid
        'should_contain': ['number', 'not letters'],
        'description': 'Test rejection of alphabetic input'
    },
    {
        'name': 'Out of Range Numbers',
        'inputs': ['0', '10', '5'],  # Try invalid ranges, then valid
        'should_contain': ['between 1 and 9'],
        'description': 'Test rejection of numbers outside 1-9 range'
    },
    {
        'name': 'Position Already Taken',
        'inputs': ['5', '5', '1'],  # Try same position twice, then valid
        'should_contain': ['already taken', 'taken by'],
        'description': 'Test rejection of moves to occupied positions'
    }
]

# ============================================
# MAIN TESTING FUNCTIONS
# ============================================

def test_single_game(game_file, test_case):
    """
    Run a single test case against a game file.
    
    Args:
        game_file: Path to the game file (tictactoe_lists.py or tictactoe_dict.py)
        test_case: TestCase object with moves and expected result
    
    Returns:
        Boolean indicating if the test passed
    """
    print(f"\nTesting: {test_case}")
    print(f"Moves: {test_case.moves}")
    print(f"Expected winner: {test_case.expected_winner}")
    
    # Create input string from moves
    input_string = simulate_game_input(test_case.moves)
    
    # Run the game
    stdout, stderr, return_code = run_game_with_input(game_file, input_string)
    
    # Check if there were any errors
    if return_code != 0:
        print(f"❌ Game crashed with return code {return_code}")
        if stderr:
            print(f"Error output: {stderr}")
        return False
    
    # Check if the expected winner was announced
    win_detected = check_win_in_output(stdout, test_case.expected_winner)
    
    if win_detected:
        print(f"✅ Correct winner detected: {test_case.expected_winner}")
        return True
    else:
        print(f"❌ Expected winner {test_case.expected_winner} not found in output")
        print("Game output (last 500 chars):")
        print(stdout[-500:] if len(stdout) > 500 else stdout)
        return False

def test_input_validation(game_file, test_data):
    """
    Test input validation by trying invalid inputs.
    
    Args:
        game_file: Path to the game file
        test_data: Dictionary with test information
    
    Returns:
        Boolean indicating if validation worked correctly
    """
    print(f"\nTesting Input Validation: {test_data['name']}")
    print(f"Description: {test_data['description']}")
    print(f"Test inputs: {test_data['inputs']}")
    
    # Create input string
    input_string = '\n'.join(test_data['inputs']) + '\n'
    
    # Run the game
    stdout, stderr, return_code = run_game_with_input(game_file, input_string)
    
    # Check if expected error messages appear
    output_lower = stdout.lower()
    found_messages = []
    
    for expected_msg in test_data['should_contain']:
        if expected_msg.lower() in output_lower:
            found_messages.append(expected_msg)
    
    if found_messages:
        print(f"✅ Found expected error messages: {found_messages}")
        return True
    else:
        print(f"❌ Expected error messages not found: {test_data['should_contain']}")
        print("Game output (last 300 chars):")
        print(stdout[-300:] if len(stdout) > 300 else stdout)
        return False

def test_game_comparison():
    """
    Test that both game versions produce identical results for the same inputs.
    This is a key requirement - both versions should behave identically.
    """
    print_test_header("GAME COMPARISON TEST")
    print("Testing that both versions produce identical results...")
    
    comparison_test = TestCase(
        name="Comparison Test",
        moves=[5, 1, 3, 7, 9],  # Simple diagonal win
        expected_winner='X',
        description="Both versions should detect same winner"
    )
    
    # Test both versions with the same input
    input_string = simulate_game_input(comparison_test.moves)
    
    lists_stdout, lists_stderr, lists_code = run_game_with_input('tictactoe_lists.py', input_string)
    dict_stdout, dict_stderr, dict_code = run_game_with_input('tictactoe_dict.py', input_string)
    
    # Both should run successfully
    if lists_code != 0 or dict_code != 0:
        print("❌ One or both games crashed")
        return False
    
    # Both should detect the same winner
    lists_win = check_win_in_output(lists_stdout, 'X')
    dict_win = check_win_in_output(dict_stdout, 'X')
    
    if lists_win and dict_win:
        print("✅ Both versions correctly detected X as winner")
        return True
    else:
        print(f"❌ Win detection mismatch - Lists: {lists_win}, Dict: {dict_win}")
        return False

def run_all_tests():
    """
    Run the complete test suite for both game versions.
    This is the main testing function that coordinates all tests.
    """
    print("🎮 EDUCATIONAL TIC-TAC-TOE TESTING SUITE")
    print("=" * 60)
    print("This test suite validates both game implementations")
    print("and demonstrates systematic testing practices.")
    print()
    
    # Check that game files exist
    if not os.path.exists('tictactoe_lists.py'):
        print("❌ tictactoe_lists.py not found!")
        return
    
    if not os.path.exists('tictactoe_dict.py'):
        print("❌ tictactoe_dict.py not found!")
        return
    
    # Track test results
    total_tests = 0
    passed_tests = 0
    
    # Test both game versions with all test cases
    for game_file in ['tictactoe_lists.py', 'tictactoe_dict.py']:
        game_name = "Nested Lists" if "lists" in game_file else "Dictionary"
        
        print_test_header(f"{game_name.upper()} VERSION TESTS")
        
        # Run win condition tests
        print(f"\n🎯 Testing Win Conditions for {game_name} Version")
        for test_case in TEST_CASES:
            total_tests += 1
            if test_single_game(game_file, test_case):
                passed_tests += 1
        
        # Run input validation tests
        print(f"\n🛡️ Testing Input Validation for {game_name} Version")
        for test_data in INVALID_INPUT_TESTS:
            total_tests += 1
            if test_input_validation(game_file, test_data):
                passed_tests += 1
    
    # Run comparison test
    print(f"\n🔄 Testing Version Comparison")
    total_tests += 1
    if test_game_comparison():
        passed_tests += 1
    
    # Print final results
    print_test_header("FINAL TEST RESULTS")
    print(f"Total Tests Run: {total_tests}")
    print(f"Tests Passed: {passed_tests}")
    print(f"Tests Failed: {total_tests - passed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! Both games are working correctly.")
    else:
        print(f"\n⚠️ {total_tests - passed_tests} tests failed. Check the output above for details.")
    
    print("\n📚 Educational Notes:")
    print("- This test suite demonstrates systematic testing practices")
    print("- Each test case documents a specific scenario")
    print("- Input validation tests ensure robust error handling")
    print("- Comparison tests verify both versions behave identically")
    print("- Test results help identify and fix bugs")

# ============================================
# INDIVIDUAL TEST FUNCTIONS
# ============================================
# These functions allow testing specific scenarios

def test_specific_win_condition(condition_name):
    """
    Test a specific win condition by name.
    Useful for debugging specific scenarios.
    """
    test_case = None
    for tc in TEST_CASES:
        if condition_name.lower() in tc.name.lower():
            test_case = tc
            break
    
    if not test_case:
        print(f"❌ Test case '{condition_name}' not found")
        return
    
    print_test_header(f"SPECIFIC TEST: {test_case.name}")
    
    for game_file in ['tictactoe_lists.py', 'tictactoe_dict.py']:
        game_name = "Lists" if "lists" in game_file else "Dictionary"
        print(f"\n🎯 Testing {game_name} Version:")
        test_single_game(game_file, test_case)

def test_error_handling_only():
    """
    Run only the input validation tests.
    Useful for testing error handling specifically.
    """
    print_test_header("INPUT VALIDATION TESTS ONLY")
    
    for game_file in ['tictactoe_lists.py', 'tictactoe_dict.py']:
        game_name = "Lists" if "lists" in game_file else "Dictionary"
        print(f"\n🛡️ Testing {game_name} Version Input Validation:")
        
        for test_data in INVALID_INPUT_TESTS:
            test_input_validation(game_file, test_data)

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    """
    Main execution block - runs when this file is executed directly.
    This demonstrates how to organize test execution.
    """
    
    print(__doc__)  # Print the module docstring
    
    # Check command line arguments for specific test types
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "win":
            # Test only win conditions
            print("Running win condition tests only...")
            for test_case in TEST_CASES:
                test_specific_win_condition(test_case.name)
        
        elif command == "validation":
            # Test only input validation
            test_error_handling_only()
        
        elif command == "comparison":
            # Test only version comparison
            test_game_comparison()
        
        elif command.startswith("specific:"):
            # Test a specific condition
            condition = command.split(":", 1)[1]
            test_specific_win_condition(condition)
        
        else:
            print(f"Unknown command: {command}")
            print("Available commands:")
            print("  python test_games.py win         - Test win conditions only")
            print("  python test_games.py validation  - Test input validation only")
            print("  python test_games.py comparison  - Test version comparison only")
            print("  python test_games.py specific:diagonal - Test specific condition")
            print("  python test_games.py             - Run all tests")
    
    else:
        # Run the complete test suite
        run_all_tests()
    
    print("\n📖 Learning Objectives Achieved:")
    print("- Systematic testing approach demonstrated")
    print("- Test case documentation and organization")
    print("- Automated validation of game functionality")
    print("- Error handling verification")
    print("- Comparison testing between implementations")
    print("\nThis testing file serves as both validation and educational example!")