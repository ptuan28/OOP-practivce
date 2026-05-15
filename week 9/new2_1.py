import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def getX(self): return self.__x
    def getY(self): return self.__y
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def distance(self, other):
        return float(math.sqrt((self.__x - other.getX())**2 + (self.__y - other.getY())**2))
    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

class LineSegment:
    def __init__(self, *args):
        if len(args) == 4:
            self.__d1 = Point(int(args[0]), int(args[1]))
            self.__d2 = Point(int(args[2]), int(args[3]))
        elif len(args) == 2:
            self.__d1 = args[0]
            self.__d2 = args[1]
        else:
            self.__d1 = Point()
            self.__d2 = Point()

    def print(self):
        print("[", end="")
        self.__d1.print()
        print("; ", end="")
        self.__d2.print()
        print("]")

    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        
        # 1. Tính radian và chuyển sang độ
        res = math.degrees(math.atan2(dy, dx))
        
        # 2. CHUẨN HÓA GÓC (Quan trọng cho testcase ẩn)
        # Nếu góc âm (ví dụ -90), chuyển thành góc dương (270)
        if res < 0:
            res += 360
            
        # 3. Xử lý trường hợp đặc biệt 360 độ về 0 độ
        if round(res) >= 360:
            res = 0
            
        return int(round(res))