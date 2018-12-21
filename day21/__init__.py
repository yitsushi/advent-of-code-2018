
from advent_of_code import BaseSolution
from typing import List, Iterable
from collections import namedtuple


Instruction = namedtuple('Instruction', 'opcode a b c')


class Solution(BaseSolution):
    source: List[Instruction]

    def setup(self):
        (input_file, ) = self.parameters()
        lines = self.read_input(input_file)

        self.source = []
        for line in lines:
            if not line.startswith('#'):
                self.source.append(
                    Instruction(
                        *self.parse(line, r'(\w+) (\d+) (\d+) (\d+)', (str, int, int, int))))

    def part1(self):
        for value in self.execute_code(self.source[7].a):
            return value

    def part2(self):
        history: List[int] = []
        for value in self.execute_code(self.source[7].a):
            if value in history:
                # First non-repeat element (after this, it's an infinite loop with a given pattern)
                return history[-1]
            history.append(value)

    @staticmethod
    def execute_code(value) -> Iterable[int]:
        control_variable = 0
        while True:
            flow_it = control_variable | 0x10000
            control_variable = value
            while True:
                control_variable = (((control_variable + (flow_it & 0xff)) & 0xffffff) * 0x1016b) & 0xffffff
                flow_it //= 0x100

                if flow_it == 0:
                    yield control_variable
                    break
