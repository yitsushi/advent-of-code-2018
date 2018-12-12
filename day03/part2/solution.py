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
    area: List[List[List[int]]] = []
    width = 0
    height = 0

    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
        self.area = [[[] for _ in range(0, _width)] for _ in range(0, _height)]

    def cut(self, claim):
        for h in range(0, claim.height):
            self.area[claim.y + h][claim.x:claim.x + claim.width] = [
                x + [claim.id] for x in self.area[claim.y + h][claim.x:claim.x + claim.width]]

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

                if all([_id in already_removed for _id in ids]):
                    continue

                to_remove = [c for c in claims if c.id in ids]
                for claim in to_remove:
                    claims.remove(claim)

                already_removed += ids

        print()


input_file, width, height = aoc.parameters((str, int, int), ('Input File', 'Width', 'Height'), (None, 1000, 1000))

print('[+] Prepare')
canvas = Canvas(width, height)

LINE_MATCH = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
claims = [Claim(*aoc.parse(line, LINE_MATCH, (int, int, int, int, int)))
          for line in aoc.read_input(input_file)]

[canvas.cut(c) for c in claims]

print('[+] Cleanup')
withOverlap = canvas.simplify()

print('[+] Filter')
clear = [c for c in claims if c.id not in withOverlap]

print('[+] Result: {}'.format(clear[0].id))
