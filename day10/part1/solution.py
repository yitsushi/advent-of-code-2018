#!/usr/bin/env python3

import re, math
from PIL import Image

class Point:
    STR_FORMAT = r'^position=< *([0-9-]+), *([0-9-]+)> velocity=< *([0-9-]+), *([0-9-]+)>$'
    x = 0
    y = 0
    velocity = (0, 0)

    def __init__(self, coordinates, velocity):
        (self.x, self.y) = coordinates
        self.velocity = velocity

    def step(self, count):
        self.x += self.velocity[0] * count
        self.y += self.velocity[1] * count

    def from_string(line):
        (x, y, vx, vy) = [int(v) for v in re.search(Point.STR_FORMAT, line).groups()]
        return Point((x, y), (vx, vy))



class Sky:
    points = None
    stepsMade = 0

    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def step(self, count=1):
        self.stepsMade += count
        [p.step(count) for p in self.points]

    def metrics(self):
        x_values = [p.x for p in self.points]
        y_values = [p.y for p in self.points]

        (min_x, max_x) = (min(x_values), max(x_values))
        (min_y, max_y) = (min(y_values), max(y_values))

        area = (max_x - min_x) * (max_y - min_y)

        return (min_x, max_x, min_y, max_y, area)

    def draw(self, filename):
        (min_x, max_x, min_y, max_y, area) = self.metrics()

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
            im.putpixel(xy=(p.x + norm_x, p.y + norm_y), value=(255, 0, 0))
        im.save(filename)


sky = Sky()
with open('../input') as f:
    [sky.add_point(Point.from_string(line)) for line in f.read().split("\n") if line != '']

last_area = sky.metrics()[4]
sky.step(1)
area = sky.metrics()[4]
diff = area - last_area
direction = int(diff / abs(diff))
speed = [pow(10, x) for x in range(int(math.log10(pow(last_area, 0.5))), -1, -1)] + [-1]
print(">>> Speed: {}".format(speed))
for s in speed:
    print(" >>> Current speed: {}".format(s))
    while diff / abs(diff) == direction:
        sky.step(s * direction * -1)
        area = sky.metrics()[4]
        diff = area - last_area
        last_area = area
        if diff == 0:
            continue
    sky.step(s * direction)
    area = sky.metrics()[4]
    diff = area - last_area
    last_area = area
    print(">>> Turn")

#sky.step(direction * -1)
print(">>> Steps: {}".format(sky.stepsMade))
data = sky.metrics()
print(">>> Size: {}x{}".format(data[1] - data[0], data[3] - data[2]))
print(">>> Area: {}".format(data[4]))
sky.draw('solution.png')
print(">>> PNG Saved...")
