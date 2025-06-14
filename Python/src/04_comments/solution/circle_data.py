import math

class Circle:
    """Class to represent a circle and perform calculations."""
    
    def __init__(self, radius):
        """Initialize the radius of the circle."""
        self.radius = radius

    def calculate_circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius

    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def is_valid(self):
        """Check if the circle is valid (radius > 0)."""
        return self.radius > 0

# Example usage
if __name__ == "__main__":
    circle = Circle(5)

    print("Circumference:", circle.calculate_circumference())
    print("Area:", circle.calculate_area())
    print("Is Valid:", circle.is_valid())
