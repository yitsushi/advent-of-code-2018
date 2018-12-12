#!/usr/bin/env python3

import advent_of_code as aoc

input_file = aoc.parameters()

numbers = [int(line) for line in aoc.read_input(input_file)]

frequencies = {}
summary = 0
inProgress = True

while inProgress:
    for n in numbers:
        summary += n
        if str(summary) in frequencies:
            inProgress = False
            break
        frequencies[str(summary)] = True

print(summary)
