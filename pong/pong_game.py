"""
Simple Pong Game - Object-Oriented Programming Demo
This game demonstrates key OOP concepts for first-time programmers:
- Encapsulation: Each class manages its own data and behavior
- Composition: Game contains other objects (Ball, Paddle, Bricks)
- Single Responsibility: Each class has one clear purpose
"""

from graphics import *
import time
import random

class Ball:
    """
    Represents the bouncing ball in the game.
    Encapsulates: position, speed, direction, and bouncing behavior
    """
    def __init__(self, x, y, radius, win):
        # Private attributes (encapsulation)
        self._x = x
        self._y = y
        self._radius = radius
        self._dx = random.choice([-3, 3])  # Horizontal speed
        self._dy = 3  # Vertical speed (downward)
        self._win = win
        
        # Create the visual representation
        self._circle = Circle(Point(x, y), radius)
        self._circle.setFill("white")
        self._circle.draw(win)
    
    def move(self):
        """Move the ball by its current speed"""
        self._x += self._dx
        self._y += self._dy
        self._circle.move(self._dx, self._dy)
    
    def bounce_horizontal(self):
        """Reverse horizontal direction (hit left/right wall or paddle)"""
        self._dx = -self._dx
    
    def bounce_vertical(self):
        """Reverse vertical direction (hit top wall or brick)"""
        self._dy = -self._dy
    
    def check_wall_collision(self, width, height):
        """Check if ball hits walls and bounce if needed"""
        # Left wall
        if self._x - self._radius <= 0:
            self._x = self._radius
            self.bounce_horizontal()
        
        # Right wall
        if self._x + self._radius >= width:
            self._x = width - self._radius
            self.bounce_horizontal()
        
        # Top wall
        if self._y - self._radius <= 0:
            self._y = self._radius
            self.bounce_vertical()
    
    def is_below_screen(self, height):
        """Check if ball fell below the screen (game over)"""
        return self._y > height
    
    def get_position(self):
        """Return ball's current position (getter method)"""
        return self._x, self._y
    
    def get_radius(self):
        """Return ball's radius"""
        return self._radius

class Paddle:
    """
    Represents the player's paddle.
    Encapsulates: position, size, and movement behavior
    """
    def __init__(self, x, y, width, height, win):
        # Private attributes
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._win = win
        self._speed = 15  # How fast paddle moves
        
        # Create visual representation
        self._rect = Rectangle(
            Point(x - width//2, y - height//2),
            Point(x + width//2, y + height//2)
        )
        self._rect.setFill("blue")
        self._rect.draw(win)
    
    def move_left(self):
        """Move paddle left (but not off screen)"""
        if self._x - self._width//2 > self._speed:
            self._x -= self._speed
            self._rect.move(-self._speed, 0)
    
    def move_right(self, screen_width):
        """Move paddle right (but not off screen)"""
        if self._x + self._width//2 < screen_width - self._speed:
            self._x += self._speed
            self._rect.move(self._speed, 0)
    
    def check_ball_collision(self, ball):
        """Check if ball hits this paddle"""
        ball_x, ball_y = ball.get_position()
        ball_radius = ball.get_radius()
        
        # Check if ball is at paddle height and within paddle width
        if (ball_y + ball_radius >= self._y - self._height//2 and
            ball_y - ball_radius <= self._y + self._height//2 and
            ball_x >= self._x - self._width//2 and
            ball_x <= self._x + self._width//2):
            return True
        return False

class Brick:
    """
    Represents a single brick that can be destroyed.
    Encapsulates: position, size, visibility, and destruction behavior
    """
    def __init__(self, x, y, width, height, color, win):
        # Private attributes
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._destroyed = False  # Track if brick is destroyed
        self._win = win
        
        # Create visual representation
        self._rect = Rectangle(
            Point(x, y),
            Point(x + width, y + height)
        )
        self._rect.setFill(color)
        self._rect.setOutline("black")
        self._rect.draw(win)
    
    def check_ball_collision(self, ball):
        """Check if ball hits this brick"""
        if self._destroyed:
            return False
        
        ball_x, ball_y = ball.get_position()
        ball_radius = ball.get_radius()
        
        # Check if ball overlaps with brick
        if (ball_x + ball_radius >= self._x and
            ball_x - ball_radius <= self._x + self._width and
            ball_y + ball_radius >= self._y and
            ball_y - ball_radius <= self._y + self._height):
            return True
        return False
    
    def destroy(self):
        """Remove this brick from the game"""
        if not self._destroyed:
            self._destroyed = True
            self._rect.undraw()
    
    def is_destroyed(self):
        """Check if this brick has been destroyed"""
        return self._destroyed

class BrickGrid:
    """
    Manages a collection of bricks.
    Demonstrates composition: BrickGrid HAS-A list of Brick objects
    """
    def __init__(self, rows, cols, brick_width, brick_height, start_x, start_y, win):
        # Private attributes
        self._bricks = []  # List to store all brick objects
        self._win = win
        
        # Create grid of bricks
        colors = ["red", "orange", "yellow", "green", "blue"]
        for row in range(rows):
            brick_row = []
            for col in range(cols):
                x = start_x + col * brick_width
                y = start_y + row * brick_height
                color = colors[row % len(colors)]  # Cycle through colors
                
                brick = Brick(x, y, brick_width, brick_height, color, win)
                brick_row.append(brick)
            
            self._bricks.append(brick_row)
        """_summary_
        """    
    def check_ball_collision(self, ball):
        """Check if ball hits any brick and destroy it"""
        for row in self._bricks:
            for brick in row:
                if brick.check_ball_collision(ball):
                    brick.destroy()
                    return True  # Ball hit a brick
        return False
    
    def all_destroyed(self):
        """Check if all bricks have been destroyed (win condition)"""
        for row in self._bricks:
            for brick in row:
                if not brick.is_destroyed():
                    return False
        return True

class Game:
    """
    Main game class that coordinates all other objects.
    Demonstrates composition: Game HAS-A Ball, Paddle, and BrickGrid
    """
    def __init__(self):
        # Game settings
        self._width = 800
        self._height = 600
        self._win = GraphWin("Pong Game - Use Arrow Keys", self._width, self._height)
        self._win.setBackground("black")
        
        # Create game objects (composition)
        self._ball = Ball(400, 300, 10, self._win)
        self._paddle = Paddle(400, 550, 100, 20, self._win)
        self._brick_grid = BrickGrid(5, 10, 80, 30, 0, 50, self._win)
        
        # Game state
        self._running = True
        self._game_over = False
        self._score = 0
        
        # Create score display
        self._score_text = Text(Point(100, 20), f"Score: {self._score}")
        self._score_text.setTextColor("white")
        self._score_text.draw(self._win)
        
        # Instructions
        instructions = Text(Point(400, 20), "Use LEFT and RIGHT arrow keys to move paddle. Press 'R' to restart")
        instructions.setTextColor("white")
        instructions.draw(self._win)
    
    def handle_input(self):
        """Check for keyboard input and move paddle"""
        key = self._win.checkKey()
        if key == "Left":
            self._paddle.move_left()
        elif key == "Right":
            self._paddle.move_right(self._width)
        elif key == "r":
            self.restart_game()
        elif key == "q":
            self._running = False
    
    def update_game(self):
        """Update all game objects"""
        # Move the ball
        self._ball.move()
        
        # Check wall collisions
        self._ball.check_wall_collision(self._width, self._height)
        
        # Check paddle collision
        if self._paddle.check_ball_collision(self._ball):
            self._ball.bounce_vertical()
        
        # Check brick collisions
        if self._brick_grid.check_ball_collision(self._ball):
            self._ball.bounce_vertical()
            self._score += 10
            self._score_text.setText(f"Score: {self._score}")
        
        # Check if ball fell below screen (game over)
        if self._ball.is_below_screen(self._height):
            self._game_over = True
            self.show_game_over("Game Over! Ball fell below paddle.")
        
        # Check if all bricks destroyed (win)
        if self._brick_grid.all_destroyed():
            self._game_over = True
            self.show_game_over("You Win! All bricks destroyed!")
    
    def restart_game(self):
        """Reset the game to initial state"""
        # Clear the window
        for item in self._win.items[:]:
            item.undraw()
        
        # Reset game objects
        self._ball = Ball(400, 300, 10, self._win)
        self._paddle = Paddle(400, 550, 100, 20, self._win)
        self._brick_grid = BrickGrid(5, 10, 80, 30, 0, 50, self._win)
        
        # Reset game state
        self._running = True
        self._game_over = False
        self._score = 0
        
        # Recreate UI elements
        self._score_text = Text(Point(100, 20), f"Score: {self._score}")
        self._score_text.setTextColor("white")
        self._score_text.draw(self._win)
        
        instructions = Text(Point(400, 20), "Use LEFT and RIGHT arrow keys to move paddle. Press 'R' to restart")
        instructions.setTextColor("white")
        instructions.draw(self._win)
    
    def show_game_over(self, message):
        """Display game over message"""
        game_over = Text(Point(400, 300), message)
        game_over.setTextColor("white")
        game_over.setSize(20)
        game_over.draw(self._win)
        
        restart_msg = Text(Point(400, 330), "Press 'R' to restart, 'Q' to quit, or click to close")
        restart_msg.setTextColor("white")
        restart_msg.draw(self._win)
    
    def run(self):
        """Main game loop"""
        while self._running:
            self.handle_input()
            if not self._game_over:
                self.update_game()
            time.sleep(0.02)  # Control game speed
        
        # Wait for final input before closing
        try:
            self._win.getMouse()
        except:
            pass
        self._win.close()

def main():
    """Create and run the game"""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
    
    

 