#!/bin/bash

# Educational Tic-Tac-Toe Testing Script
# This script runs manual tests for both game versions

echo "🎮 Educational Tic-Tac-Toe Testing Script"
echo "=========================================="
echo ""

# Check if game files exist
if [ ! -f "tictactoe_lists.py" ]; then
    echo "❌ Error: tictactoe_lists.py not found!"
    exit 1
fi

if [ ! -f "tictactoe_dict.py" ]; then
    echo "❌ Error: tictactoe_dict.py not found!"
    exit 1
fi

echo "✅ Both game files found"
echo ""

# Function to test basic syntax
test_syntax() {
    echo "🔍 Testing Python syntax..."
    
    echo -n "  Lists version syntax: "
    if python3 -m py_compile tictactoe_lists.py 2>/dev/null; then
        echo "✅ OK"
    else
        echo "❌ SYNTAX ERROR"
        python3 -m py_compile tictactoe_lists.py
        return 1
    fi
    
    echo -n "  Dictionary version syntax: "
    if python3 -m py_compile tictactoe_dict.py 2>/dev/null; then
        echo "✅ OK"
    else
        echo "❌ SYNTAX ERROR"
        python3 -m py_compile tictactoe_dict.py
        return 1
    fi
    
    echo -n "  Main launcher syntax: "
    if python3 -m py_compile main.py 2>/dev/null; then
        echo "✅ OK"
    else
        echo "❌ SYNTAX ERROR"
        python3 -m py_compile main.py
        return 1
    fi
    
    return 0
}

# Function to test basic startup
test_startup() {
    echo ""
    echo "🚀 Testing game startup (first 10 lines of output)..."
    
    echo ""
    echo "📋 Lists version startup:"
    echo "------------------------"
    timeout 5s python3 tictactoe_lists.py < /dev/null 2>&1 | head -10
    
    echo ""
    echo "📋 Dictionary version startup:"
    echo "-----------------------------"
    timeout 5s python3 tictactoe_dict.py < /dev/null 2>&1 | head -10
    
    echo ""
    echo "📋 Main launcher startup:"
    echo "------------------------"
    timeout 5s python3 main.py < /dev/null 2>&1 | head -10
}

# Function to run interactive test
run_interactive_test() {
    local game_file=$1
    local game_name=$2
    
    echo ""
    echo "🎯 Interactive Test: $game_name"
    echo "================================"
    echo "This will run the $game_name version interactively."
    echo "Try these moves for a quick test: 5, 1, 3, 7, 9 (X should win diagonally)"
    echo ""
    echo "Press Enter to start, or Ctrl+C to skip..."
    read -r
    
    python3 "$game_file"
}

# Function to test with predefined input
test_with_input() {
    local game_file=$1
    local game_name=$2
    
    echo ""
    echo "🤖 Automated Test: $game_name"
    echo "============================="
    echo "Testing with moves: 5, 1, 3, 7, 9 (should result in X winning diagonally)"
    
    # Create input sequence
    echo -e "5\n1\n3\n7\n9\nn" | timeout 10s python3 "$game_file" 2>&1 | tail -20
}

# Main menu function
show_menu() {
    echo ""
    echo "🔧 Test Options:"
    echo "==============="
    echo "1. Syntax check only"
    echo "2. Startup test only" 
    echo "3. Automated test with predefined moves"
    echo "4. Interactive test - Lists version"
    echo "5. Interactive test - Dictionary version"
    echo "6. Interactive test - Main launcher"
    echo "7. Run all automated tests"
    echo "8. Exit"
    echo ""
    echo -n "Choose an option (1-8): "
}

# Main execution
main() {
    while true; do
        show_menu
        read -r choice
        
        case $choice in
            1)
                test_syntax
                ;;
            2)
                test_startup
                ;;
            3)
                echo ""
                echo "🤖 Running automated tests..."
                test_with_input "tictactoe_lists.py" "Lists Version"
                test_with_input "tictactoe_dict.py" "Dictionary Version"
                ;;
            4)
                run_interactive_test "tictactoe_lists.py" "Lists Version"
                ;;
            5)
                run_interactive_test "tictactoe_dict.py" "Dictionary Version"
                ;;
            6)
                run_interactive_test "main.py" "Main Launcher"
                ;;
            7)
                echo ""
                echo "🔄 Running all automated tests..."
                test_syntax
                if [ $? -eq 0 ]; then
                    test_startup
                    test_with_input "tictactoe_lists.py" "Lists Version"
                    test_with_input "tictactoe_dict.py" "Dictionary Version"
                    echo ""
                    echo "✅ All automated tests completed!"
                    echo "💡 For thorough testing, also run the interactive tests (options 4-6)"
                else
                    echo "❌ Syntax errors found. Fix these before running other tests."
                fi
                ;;
            8)
                echo ""
                echo "👋 Testing complete! Thanks for using the testing script."
                echo ""
                echo "📚 Educational Notes:"
                echo "- Syntax checking ensures code can be parsed"
                echo "- Startup testing verifies basic initialization"
                echo "- Automated testing checks game logic with known inputs"
                echo "- Interactive testing allows full manual verification"
                echo ""
                echo "🎯 Next Steps:"
                echo "- If tests pass, the games are ready for educational use"
                echo "- If tests fail, check the error messages for debugging clues"
                echo "- Use the documentation in docs/ for troubleshooting help"
                exit 0
                ;;
            *)
                echo "❌ Invalid option. Please choose 1-8."
                ;;
        esac
        
        echo ""
        echo "Press Enter to continue..."
        read -r
    done
}

# Run the main function
main