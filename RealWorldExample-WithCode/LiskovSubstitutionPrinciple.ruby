Liskov Substitution Principle (LSP) - Subtypes should be substitutable for their base types.
Example: A class that implements a rectangle, and a class that implements a square as a special type of rectangle.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
