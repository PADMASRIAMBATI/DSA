# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width     # here width & height variables are private variables
        self._height = height   # by specifying underscore '_' before variable name is called private variable which can access in particular class only

    # getter methods to read
    @property
    def width(self):
        return f"{self._width}cm"

    @property
    def height(self):
        return f"{self._height}cm"

    # setter methods to write
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # delete methods to delete
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)

print("---------- setter ----------")
rectangle.width = 0

print("--------- variable ---------")
print(rectangle.width)
print(rectangle.height)

print("----- private variable -----")
print(rectangle._width)
print(rectangle._height)

print("--------- deleter ----------")
del rectangle.width
del rectangle.height


