# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The area of the circle is {3.14 * self.radius ** 2}cm"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"The area of the square is {self.side ** 2}cm"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return f"The area of the triangle is {self.base * self.height / 2}cm"

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza(9,"pepperoni")]

for shape in shapes:
    print(shape.area())