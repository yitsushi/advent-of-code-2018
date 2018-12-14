from advent_of_code import BaseSolution
from advent_of_code.data_structure import Vector2D
import math
from .point import Point
from .sky import Sky


class Solution(BaseSolution):
    sky: Sky

    def setup(self):
        self.sky = Sky()

        (input_file, ) = self.parameters()

        line_format = r'^position=< *([0-9-]+), *([0-9-]+)> velocity=< *([0-9-]+), *([0-9-]+)>$'
        for line in self.read_input(input_file):
            (x, y, vx, vy) = self.parse(line, line_format, (int, int, int, int))
            self.sky.add_point(Point(Vector2D(x, y), Vector2D(vx, vy)))

    def fast_forward(self):
        last_area = self.sky.metrics()[4]
        self.sky.step(1)
        area = self.sky.metrics()[4]
        diff = area - last_area
        direction = int(diff / abs(diff))

        speed = [pow(10, x) for x in range(int(math.log10(pow(last_area, 0.5))), -1, -1)] + [-1]

        for s in speed:
            while diff / abs(diff) == direction:
                self.sky.step(s * direction * -1)
                area = self.sky.metrics()[4]
                diff = area - last_area
                last_area = area
                if diff == 0:
                    continue
            self.sky.step(s * direction)
            area = self.sky.metrics()[4]
            diff = area - last_area
            last_area = area

    def part1(self) -> str:
        self.fast_forward()
        self.report_time('fast-forward')

        # self.sky.draw_png('day-10-part1-solution')
        # return "Open the 'day-10-part1-solution.png' file for your answer"

        self.sky.draw_ascii()
        return 'You can see your answer above.'

    def part2(self) -> int:
        self.fast_forward()
        self.report_time('fast-forward')

        return self.sky.elapsed_seconds()
