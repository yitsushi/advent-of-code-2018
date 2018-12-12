#!/usr/bin/env python3

import advent_of_code as aoc

input_file, generations = aoc.parameters(2, (str, int), (None, 20))

class Cave:
    pots = None
    patterns = None
    zero_pot_index = None

    def __init__(self):
        self.patterns = {}
        self.zero_pot_index = 0

    def set_state(self, state):
        self.zero_pot_index = 5
        self.pots = "....." + state + "....."

    def add_pattern(self, pattern):
        source, _, result = pattern.split(' ')
        #final = source[:2] + result + source[-2:]
        self.patterns[source] = result

    def next(self):
        add_to = 5-self.pots[0:5].count('.')
        self.zero_pot_index += add_to
        self.pots = (add_to * '.') + self.pots
        self.pots += (5-self.pots[-5:].count('.')) * '.'

        new_pots = '..'

        for n in range(2, len(self.pots)-2):
            new_pots += self.patterns.get(self.pots[n-2:n+3], '.')

        self.pots = new_pots + '..'

    def number_of_plants(self):
        return self.pots.count('#')

    def pots_with_plant(self):
        return [(i - self.zero_pot_index) for i in range(0, len(self.pots)) if self.pots[i] == '#']

cave = Cave()

for line in aoc.read_input(input_file):
    if "initial state:" in line:
        cave.set_state(line.split(' ')[-1])
    else:
        cave.add_pattern(line)

for gen in range(0, generations):
    cave.next()

print(sum(cave.pots_with_plant()))
