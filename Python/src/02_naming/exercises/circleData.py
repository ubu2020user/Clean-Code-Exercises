import math

class CircleData:
    # Initialize the radius of the circle
    def __init__(self, _Rad):
        self._Rad = _Rad

    # Calculate the circumference of the circle
    def calcCircumfrnc(self):
        return 2 * math.pi * self._Rad

    # Calculate the area of the circle
    def calcAr(self):
        return math.pi * self._Rad * self._Rad

    # Check if the circle is valid
    def checkValid(self):
        return self._Rad > 0

# Example usage
if __name__ == "__main__":
    circ = CircleData(5)

    print("Calc (Circumference):", circ.calcCircumfrnc())
    print("Calc (Area):", circ.calcAr())
    print("Check (Valid):", circ.checkValid())
