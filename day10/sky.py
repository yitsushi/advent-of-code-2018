from advent_of_code import Vector2D
from PIL import Image
from typing import List
from .point import Point


class Sky:
    points: List[Point]

    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def step(self, count=1):
        [p.step(count) for p in self.points]

    def metrics(self):
        x_values = [p.location.x for p in self.points]
        y_values = [p.location.y for p in self.points]

        (min_x, max_x) = (min(x_values), max(x_values))
        (min_y, max_y) = (min(y_values), max(y_values))

        _area = (max_x - min_x) * (max_y - min_y)

        return min_x, max_x, min_y, max_y, _area

    def elapsed_seconds(self):
        return self.points[0].number_of_steps()

    def draw_ascii(self):
        (min_x, max_x, min_y, max_y, _) = self.metrics()

        norm_x = abs(min_x)
        norm_y = abs(min_y)

        if min_x > 0:
            norm_x *= -1
        if min_y > 0:
            norm_y *= -1

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        all_coordinates = [p.location for p in self.points]
        for y in range(0, height):
            line = ''
            for x in range(0, width):
                if Vector2D(x - norm_x, y - norm_y) in all_coordinates:
                    line += '#'
                else:
                    line += ' '
            print(line)

    def draw_png(self, filename):
        (min_x, max_x, min_y, max_y, _) = self.metrics()

        norm_x = abs(min_x)
        norm_y = abs(min_y)

        if min_x > 0:
            norm_x *= -1
        if min_y > 0:
            norm_y *= -1

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        im = Image.new('RGB', (width, height))
        for p in self.points:
            im.putpixel(xy=(p.location.x + norm_x, p.location.y + norm_y), value=(255, 0, 0))
        im.save('{:s}.png'.format(filename))
