class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def calculate_area(shape):
    return shape.area()

rect = Rectangle(10, 5)
print(calculate_area(rect)) # 50

sq = Square(10)
print(calculate_area(sq)) # 100
