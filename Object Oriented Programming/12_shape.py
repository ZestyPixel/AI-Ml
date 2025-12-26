from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def area(self, radius):
        print(3.14* radius* radius)

class Rectangle(Shape):
    def area(self, length, breadth):
        print(length* breadth)

class Triangle(Shape):
    def area(self, base, height):
        print(0.5* base* height)

c = Circle()
r = Rectangle()
t = Triangle()

c.area(10)
r.area(10, 10)
t.area(10, 10)