
from advent_of_code import BaseSolution
from typing import List
from .instruction import Instruction
from .sample import Sample
from .device import Device
from .opcode_map import OpcodeMap


class Solution(BaseSolution):
    samples: List[Sample]
    instructions: List[Instruction]

    def setup(self):
        (input_file, ) = self.parameters()
        lines: List[str] = list(self.read_input(input_file))

        self.samples = []
        self.instructions = []

        while len(lines) > 0:
            section = lines.pop(0)
            if section.startswith('Before'):
                before_parts = section.split(': ')[1][1:-1].split(', ')
                before = Device([int(x) for x in before_parts])
                ins = Instruction(*[int(x) for x in lines.pop(0).split(' ')])
                after_parts = lines.pop(0).split(':  ')[1][1:-1].split(', ')
                after = Device([int(x) for x in after_parts])
                self.samples.append(Sample(before, after, ins))
                continue

            ins = Instruction(*[int(x) for x in section.split(' ')])
            self.instructions.append(ins)

    def part1(self):
        samples_with_more_than_two_matches: List[Sample] = []
        for s in self.samples:
            if s.test() > 2:
                samples_with_more_than_two_matches.append(s)
        return len(samples_with_more_than_two_matches)

    def part2(self):
        for s in self.samples:
            s.train()

        final_device = Device()
        for ins in self.instructions:
            OpcodeMap.execute(final_device, ins)
            
        return final_device.registers[0]
