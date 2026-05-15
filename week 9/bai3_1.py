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

    def getColor(self):
        return self.__color

    def print(self):
        super().print()
        
        print(f": {self.__color}")

class ColorPointTest:
    def testCase(self):
        try:
            
            data1 = input().split()
            if not data1: return
            cp1 = ColorPoint(int(data1[0]), int(data1[1]), data1[2])

            
            data2 = input().split()
            if not data2: return
            dx, dy = map(int, data2)
            cp1.print()
            
            
            cp1.move(dx, dy)
            cp1.print()
            
        except (EOFError, ValueError, IndexError):
            pass