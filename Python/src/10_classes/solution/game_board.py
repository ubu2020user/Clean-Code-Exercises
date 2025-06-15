import os
import sys
import time

from position import Position

class GameBoard:
    """Represents the game board."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.SNAKE_CHAR = 'O'
        self.FOOD_CHAR = '*'
        self.EMPTY_CHAR = ' '
        
    def draw(self, snake, food, score):
        """Draws the current state of the game."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {score}")
        
        # Top border
        print('#' * (self.width + 2))
        
        for y in range(self.height):
            print('#', end='')  # Left border
            for x in range(self.width):
                current_pos = Position(x, y)
                
                # Check if position contains snake
                snake_segment = False
                for segment in snake.body:
                    if segment.x == x and segment.y == y:
                        print(self.SNAKE_CHAR, end='')
                        snake_segment = True
                        break
                        
                if not snake_segment:
                    if food.position.x == x and food.position.y == y:
                        print(self.FOOD_CHAR, end='')
                    else:
                        print(self.EMPTY_CHAR, end='')
                        
            print('#')  # Right border
        
        # Bottom border
        print('#' * (self.width + 2))