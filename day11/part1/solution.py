#!/usr/bin/env python

import advent_of_code as aoc

serial_number = aoc.parameters(1, (int, ))

def level(x, y):
    rack_id = x + 10
    power_start = rack_id * y
    return (((power_start + serial_number) * rack_id) % 1000 // 100) - 5

def neighbors(x, y):
    valid = lambda n: n >=0 and n < 300
    window = [0, 1, 2]
    return [((x+i, y+j)) for i in window for j in window if valid(x+i) and valid(y+j) ]

area = []
for y in range(1, 301):
    area.append([level(x, y) for x in range(1, 301)])

windows = []
for y in range(0, 300):
    for x in range(0, 300):
        windows.append(sum([area[_y][_x] for _x, _y in neighbors(x, y)]))

max_value = max(windows)
index = windows.index(max_value)

print(max_value)
print(index % 300 + 1, index // 300 + 1)
