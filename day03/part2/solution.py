#!/usr/bin/env python3

import re

LINE_MATCH = '^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'

class Claim():
    id = 0
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, s):
        groups = re.search(LINE_MATCH, s).groups()
        (self.id,
                self.x, self.y,
                self.width, self.height
        ) = [int(v) for v in groups]

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

print('[+] Prepare')
canvas = Canvas(1000, 1000)

with open('../input') as f:
    claims = [Claim(claim) for claim in f.read().split('\n') if claim != '']

print('[+] Cut')
for claim in claims:
    canvas.cut(claim)

print('[+] Cleanup')
withOverlap = canvas.simplify()

print('[+] Filter')
clear = [c for c in claims if c.id not in withOverlap]

print('[+] Result: {}'.format(clear[0].id))
