#!/usr/bin/env python3

import advent_of_code as aoc
import regex, sys

(input_file, ) = aoc.parameters()
idList = [l for l in aoc.read_input(input_file)]

has_two = 0
has_three = 0

for index in range(0, len(idList)):
    current = idList[index]
    for id in idList[index+1:]:
        result = regex.search(r'(%s){e<2}' % (id), current)
        if result is not None:
            i = result.fuzzy_changes[0][0]
            print(current[:i] + current[i+1:])
            sys.exit(0)

