from typing import List, Generator
from advent_of_code import Vector2D, Map2D


class WorldMap(Map2D):
    defaultValue = '.'
    targets: List[Vector2D] = []

    def __init__(self, _width: int, _height: int):
        super().__init__(_width, _height)

    def add_target(self, target: Vector2D):
        self.targets.append(target)

    def closest_target(self, location: Vector2D):
        distances = sorted(
            [((self.targets[i] - location).manhattan(), i)
             for i in range(0, len(self.targets))])

        if distances[0][0] == distances[1][0]:
            return '.'

        return distances[0][1]

    def distance_from_targets(self, location) -> List[int]:
        return [(target - location).manhattan() for target in self.targets]

    def fill(self) -> Generator:
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                yield Vector2D(x, y)

    def flat_map_without_edges(self) -> List[int]:
        ids = set(self.edge_values())
        return [x for x in self.flatten() if x not in ids]
