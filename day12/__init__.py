from advent_of_code import BaseSolution
from .cave import Cave


class Solution(BaseSolution):
    cave: Cave

    def setup(self):
        self.cave = Cave()

        (input_file, ) = self.parameters()

        for line in self.read_input(input_file):
            if "initial state:" in line:
                self.cave.set_state(line.split(' ')[-1])
            else:
                self.cave.add_pattern(line)

    def part1(self) -> int:
        generations = 20
        for gen in range(0, generations):
            self.cave.next()

        return sum(self.cave.pots_with_plant())

    def part2(self) -> int:
        generations = 50_000_000_000
        last_value = sum(self.cave.pots_with_plant())
        diff_history = []
        for gen in range(0, generations):
            self.cave.next()
            current_value = sum(self.cave.pots_with_plant())
            diff = current_value - last_value
            last_value = current_value

            diff_history.append(diff)
            if len(diff_history) > 10:
                if len(set(diff_history[-10:])) == 1:
                    return (generations-gen-1) * diff + current_value
