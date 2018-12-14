from advent_of_code import BaseSolution
from advent_of_code.data_structure import SumTable
from advent_of_code.data_structure import Vector2D
from typing import Tuple


class Solution(BaseSolution):
    SIZE = 300

    serial_number: int
    sum_table: SumTable

    def setup(self):
        (self.serial_number, ) = self.parameters((int, ), ('Serial Number', ), (6042, ))
        self.sum_table = SumTable(self.SIZE, self.SIZE)

        for y in range(1, self.SIZE+1):
            self.sum_table.set_row(y - 1, [self.energy_level(Vector2D(x, y)) for x in range(1, self.SIZE+1)])

        self.sum_table.calculate()

    def energy_level(self, location: Vector2D) -> int:
        rack_id = location.x + 10
        power_start = rack_id * location.y
        return (((power_start + self.serial_number) * rack_id) % 1000 // 100) - 5

    def part1(self) -> str:
        max_value: Tuple[int, int, int] = (-10000, 0, 0)

        for y in range(0, self.SIZE-2):
            for x in range(0, self.SIZE-2):
                value = self.sum_table.area(Vector2D(x, y), Vector2D(x+2, y+2))
                if value > max_value[0]:
                    max_value = (value, x+1, y+1)

        return '{:d},{:d}'.format(*max_value[1:])

    def part2(self) -> str:
        max_value: Tuple[int, int, int, int] = (-10000, 0, 0, 0)

        for y in range(0, self.SIZE):
            for x in range(0, self.SIZE):
                max_size = self.SIZE-(max(x, y))
                for s in range(1, max_size):
                    value = self.sum_table.area(Vector2D(x, y), Vector2D(x+s, y+s))
                    if value > max_value[0]:
                        max_value = (value, x+1, y+1, s+1)

        return '{:d},{:d},{:d}'.format(*max_value[1:])
