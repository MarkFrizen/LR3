from abc import ABC, abstractmethod
import math
class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    @abstractmethod
    def perimeter(self) -> float:
        pass
class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return math.pi * self.radius ** 2
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"Прямоугольник: Площадь = {rect.area()}, Периметр = {rect.perimeter()}")
    circle = Circle(4)
    print(f"Круг: Площадь = {circle.area():.2f}, Периметр = {circle.perimeter():.2f}")