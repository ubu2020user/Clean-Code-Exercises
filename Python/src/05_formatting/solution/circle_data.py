import math


class CircleData:
    def __init__(self, _Rad):
        self._Rad = _Rad

    def calcCircumfrnc(self):
        return 2 * math.pi * self._Rad

    def calcAr(self):
        return (math.pi * (self._Rad)) * self._Rad

    def checkValid(self):
        return self._Rad > 0


if __name__ == "__main__":
    circ = CircleData(5)
    print("Calc (Circumference):", circ.calcCircumfrnc())
    print("Calc (Area):", circ.calcAr())
    print("Check (Valid):", circ.checkValid())
