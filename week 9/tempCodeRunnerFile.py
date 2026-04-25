from bai1_1 import Point
import math
import copy
class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 2)
        elif len(args) == 2 and all(isinstance(arg, Point) for arg in args):
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4 and all(isinstance(arg, (int, float)) for arg in args):
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.__d1 = copy.deepcopy(args[0].getD1())
            self.__d2 = copy.deepcopy(args[0].getD2())

    def read(self):
        x1 , y1 , x2 , y2 = map(int, input().split())
        self.__d1 = Point(x1, y1)
        self.__d2 = Point(x2, y2)
    def print(self):
        print(f"d1({self.__d1.getX()}, {self.__d1.getY()})")
        print(f"d2({self.__d2.getX()}, {self.__d2.getY()})")
    
    def move(self, dx, dy):
        self.__d1.move(int(dx), int(dy))
        self.__d2.move(int(dx), int(dy))
    def length(self):
        return self.__d1.distance(self.__d2)
    def int_angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        return math.atan2(dy, dx) * 180 / math.pi
    
    
class LineSegmentTest:
    @staticmethod
    def testCase1():
        A = Point(2,5)
        B = Point(20,35)
        AB = LineSegment(A, B)
        AB.move(35,51)
        AB.print()
    @staticmethod
    def testCase2():
        CD = LineSegment()
        CD.read()
        CD.length()
        print(f"Do dai CD: {CD.length():.2f}")
    @staticmethod
    def testCase3():
        print("nhập vào n đoạn thẳng: ")
        n = int(input())
        line_segments = []
        for _ in range(n):
            s = LineSegment()
            s.read(f"nhập đoạn thẳng {i+1}: ")
            line_segments.append(s)
        for i, s in enumerate(line_segments):
            print(f"Đoạn thẳng {i+1}:")
            s.print()
            print(f"Độ dài: {s.length():.2f}")
    @staticmethod
    def main():
        LineSegmentTest.testCase1()
        LineSegmentTest.testCase2()
        LineSegmentTest.testCase3()
LineSegmentTest.main()