import math
from py_compile import main
class Point:
    def __init__(self, x = 0, y = 1):
        self.__x = x
        self.__y = y

    def read (self, x, y):
        self.__x = int(input(x))
        self.__y = int(input(y))
    
    def print (self):
        print(f"({self.__x}, {self.__y})")
    
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
class PointTest :
    def main(self):
        p1 = Point(3,4)
        
        p1.print()
        
    #tạo điểm p2
        p2 = Point()
        p2.read('nhap x : ', 'nhap y : ')
        p2.print()
        
        
    #tạo điểm p3 đối xứng p2 qua gốc tọa độ
        
        p3 = Point(-p2.getX(), -p2.getY())
        p3.print()
        
        print("Khoang cach tu p2 den goc toa do: ", p2.distance())
        print("Khoang cach tu p1 den p2: ", p1.distance(p2))
        

if __name__ == "__main__":
    test = PointTest()
    test.main()
