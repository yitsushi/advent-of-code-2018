#!/usr/bin/env python3

import advent_of_code as aoc
from typing import Dict

(input_file, ) = aoc.parameters()

numbers = [int(line) for line in aoc.read_input(input_file)]

frequencies:Dict[int, bool] = {}
summary = 0
inProgress = True

while inProgress:
    for n in numbers:
        summary += n
        if summary in frequencies:
            inProgress = False
            break
        frequencies[summary] = True

print(summary)
