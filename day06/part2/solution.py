#!/usr/bin/env python3

from collections import Counter
import advent_of_code as aoc

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Target(Point):
    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

class Map:
    width = 0
    height = 0
    area = None
    targets = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.area = [['.' for _ in range(0, self.width+1)] for _ in range(0, self.height+1)]

    def is_on_grid(self, x, y):
        return (x >= 0 and x <= self.width and y >= 0 and y <= self.height)

    def add_target(self, target):
        self.targets.append(target)

    def distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def distance_sum(self, x, y):
        return sum([self.distance(self.targets[i], Point(x, y)) for i in range(0, len(self.targets))])

    def fill(self):
        i = 0
        for y in range(0, self.height + 1):
            if int(y/self.height*100) % 2 == 0:
                print(f'{int(y/self.height * 100)}%', end='\r')
            for x in range(0, self.width + 1):
                self.area[y][x] = self.distance_sum(x, y)

        print()

    def flat(self):
        return [x for line in self.area for x in line]

input_file, limit = aoc.parameters(2, (str, int), (None, 10_000))
targets = [Target(*[int(x) for x in line.split(', ')]) for line in aoc.read_input(input_file)]

max_x = max([t.x for t in targets])
max_y = max([t.y for t in targets])

full_map = Map(max_x, max_y)
for t in targets:
    full_map.add_target(t)

full_map.fill()

filtered = [x for x in full_map.flat() if x < limit]

print(len(filtered))
