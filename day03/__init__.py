from advent_of_code import BaseSolution
from typing import List
from .claim import Claim
from .canvas import Canvas


class Solution(BaseSolution):
    canvas: Canvas
    claims: List[Claim]

    def setup(self):
        (input_file, width, height) = self.parameters(
            (str, int, int),
            ('Input File', 'Width', 'Height'),
            ('input', 1000, 1000))

        self.canvas = Canvas(width, height)
        line_match = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
        self.claims = [
            Claim(*self.parse(line, line_match, (int, int, int, int, int)))
            for line in self.read_input(input_file)]

        for c in self.claims:
            self.canvas.cut(c)

    def part1(self) -> int:
        return self.canvas.overlap()

    def part2(self) -> int:
        with_overlap = self.canvas.simplify()
        self.report_time('simplify')

        clear = [c for c in self.claims if c.id not in with_overlap]

        return clear[0].id
