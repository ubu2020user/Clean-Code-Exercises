import sys
import time

from position import Position
from game_board import GameBoard
from snake import Snake
from food import Food

class Game:
    """Main game class that coordinates game logic."""
    def __init__(self):
        self.WIDTH = 20
        self.HEIGHT = 10
        self.score = 0
        self.game_board = GameBoard(self.WIDTH, self.HEIGHT)
        
        # Create snake at the center of the board
        start_pos = Position(self.WIDTH // 2, self.HEIGHT // 2)
        self.snake = Snake(start_pos)
        
        # Create food at a random position
        self.food = Food(self.WIDTH, self.HEIGHT)
        
    def update(self):
        """Updates the game state for one frame."""
        self.snake.update_direction()
        new_head = self.snake.move()
        
        # Check collision
        if self.snake.check_collision(self.WIDTH, self.HEIGHT):
            print("Game Over!")
            sys.exit()
            
        # Check if food is eaten
        if self.food.is_eaten(new_head):
            self.score += 1
            self.food.reposition(self.WIDTH, self.HEIGHT)
        else:
            self.snake.remove_tail()
    
    def run(self):
        """Runs the main game loop."""
        while True:
            self.game_board.draw(self.snake, self.food, self.score)
            self.update()
            time.sleep(0.2)