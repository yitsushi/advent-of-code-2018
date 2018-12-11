#!/usr/bin/env python

import advent_of_code as aoc

serial_number = aoc.parameters(1, (int, ))

def level(x, y):
    rack_id = x + 10
    power_start = rack_id * y
    return (((power_start + serial_number) * rack_id) % 1000 // 100) - 5

def sum_area(x, y):
    a = sum_table[y][x-1] if x > 0 else 0
    b = sum_table[y-1][x] if y > 0 else 0
    c = sum_table[y-1][x-1] if y > 0 and x > 0 else 0
    return a + b - c + area[y][x]

area = []
sum_table = []

print('>>> Calculate Fields')
for y in range(1, 301):
    area.append([level(x, y) for x in range(1, 301)])

print('>>> Create SumTable')
for y in range(0, 300):
    sum_table.append([])
    for x in range(0, 300):
        sum_table[y].append(sum_area(x, y))

print('>>> Find')
get_value = lambda x,y: sum_table[y][x]


def calculate_value(x, y, s):
    a = get_value(x - 1, y - 1) if x > 0 and y > 0 else 0
    b = get_value(x+s, y-1) if y > 0 else 0
    c = get_value(x-1, y+s) if x > 0 else 0
    d = get_value(x+s, y+s)

    return d - b - c + a

max_value = (-10000, 0, 0, 0)
for y in range(0, 300):
    for x in range(0, 300):
        for s in range(1, 300-(max(x, y))):
            value = calculate_value(x, y, s)
            if value > max_value[0]:
                max_value = (value, x+1, y+1, s+1)

print('Maximum valie is {:d} at {:d},{:d},{:d}'.format(*max_value))
