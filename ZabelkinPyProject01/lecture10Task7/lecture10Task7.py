import math

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round((math.pi * self.radius * self.radius), 2)


class Square(Shape):
    def __init__(self, length):
        self.length = length


circle = Circle(5)
print(circle.area())

square = Square(5)
print(square.area())