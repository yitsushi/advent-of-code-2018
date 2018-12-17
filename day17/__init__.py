from advent_of_code import BaseSolution, Vector2D
from collections import namedtuple
from typing import List
from .tile import Tile
from .underground_world import UndergroundWorld


class Solution(BaseSolution):
    underground: UndergroundWorld

    def setup(self):
        (input_file, ) = self.parameters()
        ParsedInput = namedtuple('ParsedInput', 'axis1 value1 axis2 from_value to_value')
        parsed_lines = [ParsedInput(*self.parse(line, r'(\w)=(\d+), (\w)=(\d+)..(\d+)', (str, int, str, int, int)))
                        for line in self.read_input(input_file)]

        vector_array: List[Vector2D] = []
        for line in parsed_lines:
            if line.axis1 == 'x':
                for y in range(line.from_value, line.to_value+1):
                    vector_array.append(Vector2D(line.value1, y))
            elif line.axis1 == 'y':
                for x in range(line.from_value, line.to_value+1):
                    vector_array.append(Vector2D(x, line.value1))

        MinMax = namedtuple('MinMax', 'min max')
        x_values = [v.x for v in vector_array]
        min_max_x = MinMax(min(x_values) - 1, max(x_values) + 1)

        y_values = [v.y for v in vector_array]
        min_max_y = MinMax(min(y_values) - 1, max(y_values))

        self.underground = UndergroundWorld(min_max_x.max - min_max_x.min + 1, min_max_y.max - min_max_y.min + 1)
        self.underground.set_spring(Vector2D(500 - min_max_x.min, 0))
        for v in vector_array:
            self.underground.set_value_at(v - Vector2D(min_max_x.min, min_max_y.min), Tile.CLAY)

        self.underground.flow()

    def part1(self):
        # self.underground.draw(replace=Tile.render_map())
        all_values = [self.underground.value_at(p) for p in self.underground.iterate_through()]
        return len([v for v in all_values if v in [Tile.WATER_ROUTE, Tile.WATER]])

    def part2(self):
        all_values = [self.underground.value_at(p) for p in self.underground.iterate_through()]
        return len([v for v in all_values if v in [Tile.WATER]])
