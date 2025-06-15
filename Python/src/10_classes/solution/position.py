class Position:
    """Represents a 2D position in the game."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False
        
    def __hash__(self):
        return hash((self.x, self.y))
