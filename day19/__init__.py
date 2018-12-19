from advent_of_code import BaseSolution
from typing import List
from .device import Device
from .instruction import Instruction


class Solution(BaseSolution):
    device: Device

    def setup(self):
        (input_file, ) = self.parameters()
        lines = self.read_input(input_file)

        source: List[Instruction] = []
        ip_index = 0
        for line in lines:
            if line.startswith('#'):
                ip_index = int(line.split(' ')[-1])
            else:
                source.append(
                    Instruction(
                        *self.parse(line, r'(\w+) (\d+) (\d+) (\d+)', (str, int, int, int))))

        self.device = Device()
        self.device.load_program(source, ip_index)

    def part1(self):
        """
        # I leave it here, how I did the first part originally ;)
        self.device.run()
        return self.device.registers()[0]
        """

        return self.after_part2_reverse_engineering()

    def part2(self):
        # With the original solution for part one, part two run for like 5ish minutes
        # and I decided to skip that and just try to understand what it does.
        # Reverse Engineering forever!

        # It's tricky, code does not depiction the method how I ended up with this.
        # However, it's not that hard, just analyzed what the code does and simplified it

        # Pre-initialized values before the jump into the main (long) loop
        value = 836
        value += 22 * self.device.get_source_line(21).b + self.device.get_source_line(23).b
        value += 10550400

        # There are more instructions in there, but as I understood, they have no effect on teh results.
        # If not, that's your problem. Do not just copy that, but start thinking and extend it.
        # Now, it worked with two input files, so I assume it's a generalized one.
        return sum([d + value // d for d in range(1, int(value ** .5) + 1) if value % d == 0])

    def after_part2_reverse_engineering(self):
        value = 836
        value += 22 * self.device.get_source_line(21).b + self.device.get_source_line(23).b

        return sum([d + value // d for d in range(1, int(value ** .5) + 1) if value % d == 0])
