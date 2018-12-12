#!/usr/bin/env python3

import advent_of_code as aoc

input_file = aoc.parameters()
idList = aoc.read_input(input_file)

has_two = 0
has_three = 0

for _id in idList:
    h = {}
    for c in set(_id):
        h[c] = _id.count(c)

    has_two += int(2 in set(h.values()))
    has_three += int(3 in set(h.values()))

print(has_two * has_three)
