#!/usr/bin/env python3
"""
Simple Educational Tic-Tac-Toe Tests

This script performs basic validation tests that can run in any environment.
It focuses on syntax checking, import testing, and basic code validation.

Educational Focus:
- Demonstrates basic testing concepts
- Shows how to validate code without full execution
- Provides examples of systematic checking
"""

import ast
import sys
import os

def test_syntax(filename):
    """Test if a Python file has valid syntax."""
    print(f"🔍 Testing syntax: {filename}")
    
    if not os.path.exists(filename):
        print(f"  ❌ File not found: {filename}")
        return False
    
    try:
        with open(filename, 'r') as file:
            source = file.read()
        
        # Try to parse the AST (Abstract Syntax Tree)
        ast.parse(source)
        print(f"  ✅ Syntax OK")
        return True
        
    except SyntaxError as e:
        print(f"  ❌ Syntax Error: {e}")
        print(f"     Line {e.lineno}: {e.text}")
        return False
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

def test_imports(filename):
    """Test if a Python file can be imported without errors."""
    print(f"📦 Testing imports: {filename}")
    
    if not os.path.exists(filename):
        print(f"  ❌ File not found: {filename}")
        return False
    
    try:
        # Try to compile the file
        with open(filename, 'r') as file:
            source = file.read()
        
        compile(source, filename, 'exec')
        print(f"  ✅ Compilation OK")
        return True
        
    except Exception as e:
        print(f"  ❌ Compilation Error: {e}")
        return False

def analyze_code_structure(filename):
    """Analyze the structure of the code for educational purposes."""
    print(f"🔬 Analyzing structure: {filename}")
    
    if not os.path.exists(filename):
        print(f"  ❌ File not found: {filename}")
        return False
    
    try:
        with open(filename, 'r') as file:
            source = file.read()
        
        tree = ast.parse(source)
        
        # Count different types of nodes
        variables = 0
        loops = 0
        conditionals = 0
        functions = 0
        classes = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                variables += 1
            elif isinstance(node, (ast.For, ast.While)):
                loops += 1
            elif isinstance(node, ast.If):
                conditionals += 1
            elif isinstance(node, ast.FunctionDef):
                functions += 1
            elif isinstance(node, ast.ClassDef):
                classes += 1
        
        print(f"  📊 Code Analysis:")
        print(f"     Variables: {variables}")
        print(f"     Loops: {loops}")
        print(f"     Conditionals: {conditionals}")
        print(f"     Functions: {functions}")
        print(f"     Classes: {classes}")
        
        # Check educational requirements
        if functions == 0 and classes == 0:
            print(f"  ✅ Educational requirement met: No functions or classes")
        else:
            print(f"  ⚠️  Contains functions/classes (may be too advanced for beginners)")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Analysis Error: {e}")
        return False

def check_educational_comments(filename):
    """Check if the file has adequate educational comments."""
    print(f"📝 Checking comments: {filename}")
    
    if not os.path.exists(filename):
        print(f"  ❌ File not found: {filename}")
        return False
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        total_lines = len(lines)
        comment_lines = 0
        code_lines = 0
        
        for line in lines:
            stripped = line.strip()
            if not stripped:  # Empty line
                continue
            elif stripped.startswith('#'):  # Comment line
                comment_lines += 1
            elif '"""' in stripped or "'''" in stripped:  # Docstring
                comment_lines += 1
            else:  # Code line
                code_lines += 1
        
        if code_lines > 0:
            comment_ratio = comment_lines / code_lines
            print(f"  📊 Comment Analysis:")
            print(f"     Total lines: {total_lines}")
            print(f"     Code lines: {code_lines}")
            print(f"     Comment lines: {comment_lines}")
            print(f"     Comment ratio: {comment_ratio:.2f}")
            
            if comment_ratio >= 0.5:
                print(f"  ✅ Good educational commenting (ratio >= 0.5)")
                return True
            else:
                print(f"  ⚠️  Could use more comments for educational purposes")
                return False
        else:
            print(f"  ⚠️  No code lines found")
            return False
        
    except Exception as e:
        print(f"  ❌ Comment analysis error: {e}")
        return False

def test_file_completeness():
    """Check that all required files exist."""
    print(f"📁 Checking file completeness...")
    
    required_files = [
        'README.md',
        'main.py',
        'tictactoe_lists.py',
        'tictactoe_dict.py',
        'docs/python-concepts.md',
        'docs/data-structures-guide.md',
        'docs/exercises.md',
        'docs/common-errors.md',
        'docs/testing-guide.md'
    ]
    
    missing_files = []
    present_files = []
    
    for filename in required_files:
        if os.path.exists(filename):
            present_files.append(filename)
            print(f"  ✅ {filename}")
        else:
            missing_files.append(filename)
            print(f"  ❌ {filename}")
    
    print(f"\n  📊 Summary:")
    print(f"     Present: {len(present_files)}/{len(required_files)}")
    print(f"     Missing: {len(missing_files)}")
    
    if missing_files:
        print(f"  ⚠️  Missing files: {missing_files}")
        return False
    else:
        print(f"  ✅ All required files present")
        return True

def run_all_tests():
    """Run all available tests."""
    print("🎮 Educational Tic-Tac-Toe Simple Tests")
    print("=" * 50)
    print()
    
    # Track results
    tests_run = 0
    tests_passed = 0
    
    # Test file completeness
    tests_run += 1
    if test_file_completeness():
        tests_passed += 1
    print()
    
    # Test Python files
    python_files = ['main.py', 'tictactoe_lists.py', 'tictactoe_dict.py']
    
    for filename in python_files:
        if os.path.exists(filename):
            print(f"🐍 Testing Python file: {filename}")
            print("-" * 40)
            
            # Syntax test
            tests_run += 1
            if test_syntax(filename):
                tests_passed += 1
            
            # Import test
            tests_run += 1
            if test_imports(filename):
                tests_passed += 1
            
            # Structure analysis
            tests_run += 1
            if analyze_code_structure(filename):
                tests_passed += 1
            
            # Comment analysis
            tests_run += 1
            if check_educational_comments(filename):
                tests_passed += 1
            
            print()
    
    # Final results
    print("=" * 50)
    print("🏁 FINAL RESULTS")
    print("=" * 50)
    print(f"Tests run: {tests_run}")
    print(f"Tests passed: {tests_passed}")
    print(f"Tests failed: {tests_run - tests_passed}")
    print(f"Success rate: {(tests_passed/tests_run)*100:.1f}%")
    
    if tests_passed == tests_run:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Code structure looks good for educational use")
    else:
        print(f"\n⚠️ {tests_run - tests_passed} tests had issues")
        print("💡 Check the details above for improvement suggestions")
    
    print("\n📚 What these tests check:")
    print("- File completeness: All required files present")
    print("- Syntax validation: Code can be parsed by Python")
    print("- Import testing: Code can be compiled without errors")
    print("- Structure analysis: Code complexity appropriate for beginners")
    print("- Comment analysis: Adequate educational commenting")
    
    print("\n🎯 What these tests DON'T check:")
    print("- Game logic correctness (requires interactive testing)")
    print("- Win condition detection (requires game execution)")
    print("- Input validation behavior (requires user input simulation)")
    print("- User experience quality (requires manual testing)")
    
    print("\n💡 For complete testing:")
    print("- Use ./run_tests.sh for interactive testing")
    print("- Manually play both games to verify functionality")
    print("- Try invalid inputs to test error handling")
    print("- Compare both versions to ensure identical behavior")

if __name__ == "__main__":
    run_all_tests()