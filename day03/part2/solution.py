#!/usr/bin/env python3

import re
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
        self.area = [[[] for _ in range(0, width)] for _ in range(0, height)]

    def cut(self, claim):
        for h in range(0, claim.height):
            self.area[claim.y + h][claim.x:claim.x+claim.width] = [x + [claim.id] for x in self.area[claim.y + h][claim.x:claim.x+claim.width]]

    def simplify(self):
        items = [item for sublist in self.area for item in sublist if len(item) > 1]
        items = [item for sublist in items for item in sublist]
        return set(items)

    def overlap(self):
        already_removed = []
        i = 0
        for row in self.area:
            i += 1
            percentage = int(i / self.height * 100)
            if percentage % 5 == 0:
                print("{:3d}%".format(percentage), end='\r')
            for ids in row:
                if len(ids) < 2:
                    continue

                if all([id in already_removed for id in ids]):
                    continue

                toRemove = [c for c in claims if c.id in ids]
                for claim in toRemove:
                    claims.remove(claim)

                already_removed += ids

        print()

input_file, width, height = aoc.parameters(3, (str, int, int), (None, 1000, 1000))

print('[+] Prepare')
canvas = Canvas(width, height)

LINE_MATCH = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
p = lambda line: Claim(*aoc.parse(line, LINE_MATCH, (int, int, int, int, int)))
claims = [p(line) for line in aoc.read_input(input_file)]

[canvas.cut(c) for c in claims]

print('[+] Cleanup')
withOverlap = canvas.simplify()

print('[+] Filter')
clear = [c for c in claims if c.id not in withOverlap]

print('[+] Result: {}'.format(clear[0].id))
