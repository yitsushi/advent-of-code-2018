#!/usr/bin/env python3

import advent_of_code as aoc

class Claim():
    id = 0
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, id:int, x:int, y:int, width:int, height:int):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Canvas():
    sarea = []
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = [[0 for _ in range(0, width)] for _ in range(0, height)]

    def cut(self, claim):
        for h in range(0, claim.height):
            self.area[claim.y + h][claim.x:claim.x+claim.width] = [x + 1 for x in self.area[claim.y + h][claim.x:claim.x+claim.width]]

    def overlap(self):
        area_count = 0
        for row in self.area:
            area_count += len([x for x in row if x > 1])

        return area_count

input_file, width, height = aoc.parameters(3, (str, int, int), (None, 1000, 1000))

canvas = Canvas(width, height)

LINE_MATCH = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
p = lambda line: Claim(*aoc.parse(line, LINE_MATCH, (int, int, int, int, int)))
claims = [canvas.cut(p(line)) for line in aoc.read_input(input_file)]

print(canvas.overlap())
