#!/bin/bash

# Educational Chatbot Setup Script
# This script sets up the Python environment for the educational chatbot

echo "Setting up Educational Chatbot environment..."

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "Setup complete!"
echo ""
echo "To run the chatbot:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the chatbot: python chatbot.py"
echo ""
echo "Make sure you have AWS credentials configured for Bedrock access."