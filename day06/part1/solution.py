#!/usr/bin/env python3

from collections import Counter
import advent_of_code as aoc
from typing import List, Any


class Point:
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        (self.x, self.y) = (x, y)


class Target(Point):
    pass


class Map:
    width = 0
    height = 0
    area: List[List[Any]] = []
    targets: List[Target] = []

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.area = [['.' for _ in range(0, self.width+1)] for _ in range(0, self.height+1)]

    def is_on_grid(self, x: int, y: int):
        return 0 <= x <= self.width and 0 <= y <= self.height

    def add_target(self, target: Target):
        self.targets.append(target)

    @staticmethod
    def distance(p1: Point, p2: Point):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def closest_target(self, x: int, y: int):
        distances = sorted([(self.distance(self.targets[i], Point(x, y)), i) for i in range(0, len(self.targets))])

        if distances[0][0] == distances[1][0]:
            return '.'

        return distances[0][1]

    def fill(self):
        for y in range(0, self.height + 1):
            if int(y/self.height*100) % 2 == 0:
                print(f'{int(y/self.height * 100)}%', end='\r')
            for x in range(0, self.width + 1):
                self.area[y][x] = self.closest_target(x, y)

        print()

    def flat_map_without_edges(self) -> List[Target]:
        ids = set(self.area[0] + self.area[self.height] +
                  [l[0] for l in self.area] +
                  [l[self.width] for l in self.area])
        return [x for line in self.area for x in line if x not in ids]


(input_file, ) = aoc.parameters()
targets = [Target(*[int(x) for x in line.split(', ')]) for line in aoc.read_input(input_file)]

max_x = max([t.x for t in targets])
max_y = max([t.y for t in targets])

full_map = Map(max_x, max_y)
for t in targets:
    full_map.add_target(t)

full_map.fill()

(number, area) = Counter(full_map.flat_map_without_edges()).most_common(1)[0]

print(f"The largest one is '{number}' with area of '{area}' units")
