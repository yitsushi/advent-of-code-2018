from advent_of_code import BaseSolution
from typing import List

class Solution(BaseSolution):
    material: str

    def setup(self):
        (input_file, ) = self.parameters()
        self.material = list(self.read_input(input_file))[0]

    def simulate(self, chain: str, to_remove: str = None) -> str:
        if to_remove is not None:
            chain = chain.replace(to_remove, '').replace(to_remove.upper(), '')

        i = 0
        while i < len(chain) - 1:
            if self.is_opposite_polarity(chain[i], chain[i+1]):
                chain = chain[:i] + chain[i+2:]
                i = max(i - 1, 0)
            else:
                i += 1

        return chain

    @staticmethod
    def is_opposite_polarity(a, b):
        return (a.upper() == b.upper()) and (a != b)

    def part1(self) -> int:
        return len(self.simulate(self.material))

    def part2(self) -> int:
        charset = set(list(self.material.lower()))
        shortest = min([len(self.simulate(self.material, ch)) for ch in charset])
        return shortest

