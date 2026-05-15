import math

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def getX(self): return self._x
    def getY(self): return self._y
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
    def print(self):
        print(f"({self._x}, {self._y})", end="")

class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="white"):
        super().__init__(x, y)
        self.__color = color
    def getColor(self): return self.__color
    def setColor(self, color): self.__color = color
    def copy(self, other):
        self._x = other.getX()
        self._y = other.getY()
        self.__color = other.getColor()
    def read(self):
        try:
            line = input().split()
            if len(line) >= 3:
                self._x = int(line[0])
                self._y = int(line[1])
                self.__color = line[2]
        except EOFError:
            pass
    def print(self):
        super().print()
        print(f": {self.__color}")


class ColorPointTest:
    def testCase(self):
        try:
            
            p1 = ColorPoint(0, 1, "xanh")
            p1.print()
            
            
            p2 = ColorPoint()
            p2.read()
            p2.print()
            
            
            p3 = ColorPoint(p2.getX(), p2.getY(), p2.getColor())
            p3.move(5, 5)
            p3.print()
            
            
            p2.print()
            
        except (EOFError, ValueError, IndexError):
            pass