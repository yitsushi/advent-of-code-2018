from math import sin, cos, pi


class Vector2D:
    x: int
    y: int

    def __init__(self, _x: int, _y: int):
        (self.x, self.y) = _x, _y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '{:d}x{:d}'.format(self.x, self.y)

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

    def rotate(self, degrees: float):
        degrees *= pi/180
        new_x = round(self.x * cos(degrees) - self.y * sin(degrees))
        new_y = round(self.x * sin(degrees) + self.y * cos(degrees))

        (self.x, self.y) = new_x, new_y
