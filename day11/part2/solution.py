#!/usr/bin/env python

import advent_of_code as aoc

SIZE = 300


def level(_x: int, _y: int):
    rack_id = _x + 10
    power_start = rack_id * _y
    return (((power_start + serial_number) * rack_id) % 1000 // 100) - 5


(serial_number, ) = aoc.parameters((int, ), ('Serial Number', ))
sum_table = aoc.data_structure.SumTable(SIZE, SIZE)

print('>>> Populate')
for y in range(1, SIZE+1):
    sum_table.set_row(y - 1, [level(x, y) for x in range(1, SIZE+1)])

print('>>> Calculate SumTable')
sum_table.calculate()


print('>>> Find')
max_value = (-10000, 0, 0, 0)

for y in range(0, SIZE):
    for x in range(0, SIZE):
        max_size = SIZE-(max(x, y))
        for s in range(1, max_size):
            value = sum_table.area((x, y), (x+s, y+s))
            if value > max_value[0]:
                max_value = (value, x+1, y+1, s+1)

print('Maximum value is {:d} at {:d},{:d},{:d}'.format(*max_value))
