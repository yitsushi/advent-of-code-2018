#!/usr/bin/env python

import advent_of_code as aoc

SIZE = 300

def level(x, y):
    rack_id = x + 10
    power_start = rack_id * y
    return (((power_start + serial_number) * rack_id) % 1000 // 100) - 5

serial_number = aoc.parameters((int, ), ('Serial Number', ))
sum_table = aoc.data_structure.SumTable(SIZE, SIZE)

print('>>> Populate')
for y in range(1, SIZE+1):
    sum_table.set_row(y - 1, [level(x, y) for x in range(1, SIZE+1)])

print('>>> Calculate SumTable')
sum_table.calculate()


print('>>> Find')
max_value = (-10000, 0, 0)

for y in range(0, SIZE-2):
    for x in range(0, SIZE-2):
        value = sum_table.area((x, y), (x+2, y+2))
        if value > max_value[0]:
            max_value = (value, x+1, y+1)

print('Maximum value is {:d} at {:d},{:d}'.format(*max_value))
