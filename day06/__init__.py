from collections import Counter
from advent_of_code import BaseSolution, Vector2D
from .world_map import WorldMap


class Solution(BaseSolution):
    limit: int
    full_map: WorldMap

    def setup(self):
        (input_file, self.limit) = self.parameters(
            (str, int),
            ('Input file', 'Max Range'),
            ('input', 10_000))

        targets = [Vector2D(*[int(x) for x in line.split(', ')]) for line in self.read_input(input_file)]

        max_x = max([t.x for t in targets])
        max_y = max([t.y for t in targets])

        self.full_map = WorldMap(max_x + 1, max_y + 1)
        for t in targets:
            self.full_map.add_target(t)

    def part1(self) -> int:
        for location in self.full_map.fill():
            self.full_map.set_value_at(location, self.full_map.closest_target(location))

        (_, area) = Counter(self.full_map.flat_map_without_edges()).most_common(1)[0]

        return area

    def part2(self) -> int:
        for location in self.full_map.fill():
            self.full_map.set_value_at(location, sum(self.full_map.distance_from_targets(location)))

        filtered = [x for x in self.full_map.flatten() if x < self.limit]

        return len(filtered)
