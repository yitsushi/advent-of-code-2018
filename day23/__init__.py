from advent_of_code import BaseSolution
from typing import List
import z3
from .bot import Bot


class Solution(BaseSolution):
    bots: List[Bot]

    def setup(self):
        (input_file, ) = self.parameters()
        self.bots = []
        for line in self.read_input(input_file):
            x, y, z, r = self.parse(line, 'pos=<([0-9-]+),([0-9-]+),([0-9-]+)>, r=([0-9]+)', (int, int, int, int))
            v = Bot(x, y, z)
            v.set_range(r)
            self.bots.append(v)

    def part1(self):
        nanobot = sorted(self.bots)[-1]

        return sum(1 for b in self.bots if (nanobot - b).manhattan() <= nanobot.range())

    def part2(self):
        def z3abs(v):
            return z3.If(v >= 0, v, -v)

        def z3manhattan(x1, y1, z1, x2, y2, z2):
            return z3abs(x1 - x2) + z3abs(y1 - y2) + z3abs(z1 - z2)

        optimizer = z3.Optimize()
        x, y, z = z3.Int('x'), z3.Int('y'), z3.Int('z')
        distance = z3.Int('distance')
        simplified_bot_list = []

        for i, b in enumerate(self.bots):
            z3bot = z3.Int("bot{:04d}".format(i))
            bxyz = (b.x, b.y, b.z)
            brange = b.range()
            works = z3.If(z3manhattan(x, y, z, *bxyz) <= brange, 1, 0)
            optimizer.add(z3bot == works)
            simplified_bot_list.append(z3bot)
            i += 1

        optimizer.add(distance == z3manhattan(x, y, z, 0, 0, 0))
        self.report_time('z3:prepare')

        optimizer.maximize(z3.Sum(simplified_bot_list))
        self.report_time('z3:maximize')
        optimizer.minimize(distance)
        self.report_time('z3:minimize')
        optimizer.check()
        self.report_time('z3:check')

        model = optimizer.model()
        minimal = model.eval(distance)

        return minimal
