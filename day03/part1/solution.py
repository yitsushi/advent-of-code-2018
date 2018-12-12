#!/usr/bin/env python3

import advent_of_code as aoc
from typing import List


class Claim:
    id = 0
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, _id: int, x: int, y: int, _width: int, _height: int):
        self.id = _id
        self.x = x
        self.y = y
        self.width = _width
        self.height = _height


class Canvas:
    area: List[List[int]] = []
    width = 0
    height = 0

    def __init__(self, _width: int, _height: int):
        self.width = _width
        self.height = _height
        self.area = [[0 for _ in range(0, _width)] for _ in range(0, _height)]

    def cut(self, claim):
        for h in range(0, claim.height):
            self.area[claim.y + h][claim.x:claim.x+claim.width] = [
                x + 1 for x in self.area[claim.y + h][claim.x:claim.x + claim.width]]
        return claim

    def overlap(self):
        area_count = 0
        for row in self.area:
            area_count += len([x for x in row if x > 1])

        return area_count


(input_file, width, height) = aoc.parameters((str, int, int), ('Input File', 'Width', 'Height'), (None, 1000, 1000))

canvas = Canvas(width, height)

LINE_MATCH = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
claims = [canvas.cut(Claim(*aoc.parse(line, LINE_MATCH, (int, int, int, int, int))))
          for line in aoc.read_input(input_file)]

print(canvas.overlap())
