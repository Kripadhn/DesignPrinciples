class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class CirclePerimeter:
    def __init__(self, circle):
        self.circle = circle

    def perimeter(self):
        return 2 * 3.14 * self.circle.radius

