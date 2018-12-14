from advent_of_code import BaseSolution
from typing import List, Dict


class Solution(BaseSolution):
    numbers: List[int]

    def setup(self):
        (input_file, ) = self.parameters()

        self.numbers = [int(line) for line in self.read_input(input_file)]

    def part1(self) -> int:
        return sum(self.numbers)

    def part2(self) -> int:
        frequencies: Dict[int, bool] = {}
        summary = 0
        in_progress = True

        while in_progress:
            for n in self.numbers:
                summary += n
                if summary in frequencies:
                    in_progress = False
                    break
                frequencies[summary] = True

        return summary
