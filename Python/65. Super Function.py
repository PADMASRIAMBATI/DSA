# Super() = function used in a child class to call methods from a parent class (super class)
#           Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a cricle with an area of {3.14 * self.radius * self.radius}cm")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm")
        super().describe()

circle = Circle("Red", True, 5)
square = Square("Green", True, 30)
triangle = Triangle("Blue", False, 5, 10)

print("---------------------------------------")
print(f"{circle.color}, {circle.is_filled}, {circle.radius}cm")
circle.describe()

print("---------------------------------------")
print(f"{square.color}, {square.is_filled}, {square.width}cm")
square.describe()

print("---------------------------------------")
print(f"{triangle.color}, {triangle.is_filled}, {triangle.width}cm, {triangle.height}cm")
triangle.describe()