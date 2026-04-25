import math


class Point :
    def __init__(self, x = 0, y = 1):
        self.__x = x
        self.__y = y

    def read (self,data):
        self.__x = int(data[0])
        self.__y = int(data[1])
    
    def print (self):
        print(f"({self.__x}, {self.__y}) ", end="")
    
    def move(self , dx , dy ):
        self.__x += dx
        self.__y += dy
    
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    
    def distance(self , P = None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)
class ColorPoint(Point):
    def __init__(self , *args):
        if len(args) == 0:
            super().__init__()
            self.__color = "blue"
        elif len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], str):
            super().__init__(args[0], args[1])
            self.__color = args[2]
        else:
            raise ValueError("Nhap 2 so nguyen (cach bang dau space ) va 1 chuoi")
    def copy(self, other):
        if isinstance(other, ColorPoint):
            self.__x = other.getX()
            self.__y = other.getY()
            self.__color = other.getColor()
        else:
            raise ValueError("Nhap mot ColorPoint khac de copy")
    
    def __init__(self , x = 0 , y = 1 , color = "blue"):
            super().__init__(x, y)
            self.__color = color
            
    def read(self):
        data = input().split()
        
        super().read(data)
        
        if len(data) > 2 :
            self.__color = data[2]
        
    def print(self):
        print(f"({self.getX()}, {self.getY()}) : {self.__color}")

    def setColor(self, color):
        self.__color = color
        
    def getColor(self):
        return self.__color
        
class ColorPointTest:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "white")
        A.print()
    @staticmethod
    def testCase2():
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()
    @staticmethod
    def testCase3():
        C = ColorPoint(6, 3, "black")
        D = ColorPoint()
        D.copy(C)
        D.print()
        D.setColor("yellow")
        D.print()
        C.print()
    @staticmethod
    def main():
        ColorPointTest.testCase1()
        ColorPointTest.testCase2()
        ColorPointTest.testCase3()
ColorPointTest.main()