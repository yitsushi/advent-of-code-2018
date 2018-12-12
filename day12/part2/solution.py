#!/usr/bin/env python3

import advent_of_code as aoc
from typing import Dict


class Cave:
    pots = None
    patterns = None
    zero_pot_index = None

    def __init__(self):
        self.patterns: Dict[str, str] = {}
        self.zero_pot_index = 0

    def set_state(self, state: str):
        self.zero_pot_index = 5
        self.pots = "....." + state + "....."

    def add_pattern(self, pattern: str):
        source, _, result = pattern.split(' ')
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

input_file, generations = aoc.parameters(
        (str, int),
        ('Input File', 'Generations'),
        (None, 50_000_000_000))
for line in aoc.read_input(input_file):
    if "initial state:" in line:
        cave.set_state(line.split(' ')[-1])
    else:
        cave.add_pattern(line)

last_value = sum(cave.pots_with_plant())
diff_history = []
for gen in range(0, generations):
    cave.next()
    current_value = sum(cave.pots_with_plant())
    diff = current_value - last_value
    last_value = current_value

    diff_history.append(diff)
    if len(diff_history) > 10:
        if len(set(diff_history[-10:])) == 1:
            print((generations-gen-1) * diff + current_value)
            break
