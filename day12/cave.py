from typing import Dict


class Cave:
    pots: str
    patterns: Dict[str, str]
    zero_pot_index: int

    def __init__(self):
        self.pots = '.'
        self.patterns = {}
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

    def pots_with_plant(self):
        return [(i - self.zero_pot_index) for i in range(0, len(self.pots)) if self.pots[i] == '#']
