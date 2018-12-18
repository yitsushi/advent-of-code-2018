from advent_of_code import BaseSolution, Map2D
from .world_map import WorldMap
from .tile import Tile


class Solution(BaseSolution):
    world_map: WorldMap

    def setup(self):
        (input_file, ) = self.parameters()
        lines = list(self.read_input(input_file))
        self.world_map = WorldMap(len(lines[0]), len(lines))

        for pos in self.world_map.iterate_through():
            self.world_map.set_value_at(pos, Tile.from_char(lines[pos.y][pos.x]))

    def part1(self):
        for i in range(0, 10):
            self.world_map.round()
        self.report_time('simulation')

        flat = self.world_map.flatten()
        return flat.count(Tile.TREES) * flat.count(Tile.LUMBERYARD)

    def part2(self):
        history = []

        i = 1
        while i <= 1_000_000_000:
            self.world_map.round()
            flat = self.world_map.flatten_snapshot(replace=Tile.render_map())
            if flat in history:
                print('Repeat found at: ', history.index(flat), len(history))
                history = history[history.index(flat):]
                remaining = (1_000_000_000 - i) % (len(history))
                flat = history[remaining]
                return flat.count(Tile.to_string(Tile.TREES)) * flat.count(Tile.to_string(Tile.LUMBERYARD))
            else:
                history.append(flat)
            i += 1
