# OOP Python Games - Installation Instructions

This project contains Python games demonstrating Object-Oriented Programming concepts using the graphics.py library. This is for Ubuntu24.

## Prerequisites

### 1. Install System Dependencies

First, install the required system packages (tkinter is needed for graphics.py):

```bash
sudo apt update && sudo apt install -y python3-tk python3-venv
```

### 2. Set Up Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd pong
python3 -m venv venv
```

### 3. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 4. Install Python Dependencies

```bash
pip install graphics.py
```

## Running the Game

Game (Full OOP Example)
```bash
python pong_game.py
```

## Game Controls

### Pong Game:
- **Left/Right Arrow Keys**: Move paddle
- **R**: Restart game
- **Q**: Quit game

