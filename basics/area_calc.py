from math import pi, sqrt


class Shape:
    def __init__(self, _side1, _side2):
        self.side1 = _side1
        self.side2 = _side2

    def calc_area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f'The area of the shape: {self.__class__.__name__} is {self.calc_area()}'


class Rectangle(Shape):
    pass


class Square(Rectangle):
    def __init__(self, _side):
        super().__init__(_side, _side)


class Triangle(Rectangle):
    def __init__(self, _base, _height):
        super().__init__(_base, _height)

    def calc_area(self):
        return 0.5 * super().calc_area()


class circle(Shape):
    def __init__(self, _radius):
        self.radius = _radius

    def calc_area(self, radius):
        return pi * radius ** 2


class Hexagon(Square):
    def __init__(self, _side):
        self.side = _side

    def calc_area(self):
        return (3 * sqrt(3) * self.side ** 2) / 2


breakpoint()
