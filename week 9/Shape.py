    
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, r: int):
        self.r = r
    def area(self) -> float:
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
    def area(self) -> float:
        return self.w * self.h