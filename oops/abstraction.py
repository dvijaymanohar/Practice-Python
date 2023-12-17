

class Shape:
    # @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side


circle = Circle(5)
square = Square(15)

print("Area of circle: " + str(circle.get_area()))
print("Area of square: " + str(square.get_area()))
