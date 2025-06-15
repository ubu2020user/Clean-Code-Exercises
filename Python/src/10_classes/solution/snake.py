import keyboard

from position import Position

class Snake:
    """Represents the snake in the game."""
    def __init__(self, start_position):
        self.body = [start_position]
        self.direction = 'RIGHT'
    
    def move(self):
        """Moves the snake according to its current direction."""
        head = self.body[0]
        
        if self.direction == 'UP':
            new_head = Position(head.x, head.y - 1)
        elif self.direction == 'DOWN':
            new_head = Position(head.x, head.y + 1)
        elif self.direction == 'LEFT':
            new_head = Position(head.x - 1, head.y)
        elif self.direction == 'RIGHT':
            new_head = Position(head.x + 1, head.y)
            
        self.body.insert(0, new_head)
        return new_head
        
    def remove_tail(self):
        """Removes the last segment of the snake."""
        self.body.pop()
        
    def check_collision(self, width, height):
        """Checks if the snake has collided with itself or walls."""
        head = self.body[0]
        # Check wall collision
        if (head.x < 0 or head.x >= width or head.y < 0 or head.y >= height):
            return True
            
        # Check self collision (skip head)
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
                
        return False
    
    def update_direction(self):
        """Updates the snake's direction based on keyboard input."""
        if keyboard.is_pressed('w') and self.direction != 'DOWN':
            self.direction = 'UP'
        elif keyboard.is_pressed('s') and self.direction != 'UP':
            self.direction = 'DOWN'
        elif keyboard.is_pressed('a') and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif keyboard.is_pressed('d') and self.direction != 'LEFT':
            self.direction = 'RIGHT'