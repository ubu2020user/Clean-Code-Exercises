import random

from position import Position

class Food:
    """Represents the food in the game."""
    def __init__(self, width, height):
        self.position = self.generate_position(width, height)
        
    def generate_position(self, width, height):
        """Generates a random position for the food."""
        return Position(random.randint(0, width - 1), random.randint(0, height - 1))
        
    def is_eaten(self, position):
        """Checks if the food has been eaten."""
        return self.position.x == position.x and self.position.y == position.y
        
    def reposition(self, width, height):
        """Moves the food to a new random position."""
        self.position = self.generate_position(width, height)
