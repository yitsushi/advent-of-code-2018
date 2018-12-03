#!/usr/bin/env python3

import re
#import Image
from PIL import Image

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

with open('../input') as f:
    claims = [Claim(claim) for claim in f.read().split('\n') if claim != '']

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

    def draw(self):
        im = Image.new('RGB', (self.width, self.height))
        for y in range(0, self.height):
            for x in range(0, self.width):
                extract = min((self.area[y][x] * 30), 255)
                value = (255, 255 - extract, 255 - extract)
                im.putpixel(xy=(x, y), value=value)

        return im

    def overlap(self):
        area_count = 0
        for row in self.area:
            area_count += len([x for x in row if x > 1])

        return area_count

canvas = Canvas(1000, 1000)

for claim in claims:
    canvas.cut(claim)

print(canvas.overlap())

image = canvas.draw()
image.save('test.png')

