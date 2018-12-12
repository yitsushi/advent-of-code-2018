#!/usr/bin/env python3

import advent_of_code as aoc

(input_file, ) = aoc.parameters()

print(sum([int(line) for line in aoc.read_input(input_file)]))
