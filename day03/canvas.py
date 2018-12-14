from typing import List, Set
from .claim import Claim


class Canvas:
    # TODO: use Map2D
    area: List[List[List[int]]] = []
    width = 0
    height = 0

    def __init__(self, _width: int, _height: int):
        self.width = _width
        self.height = _height
        self.area = [[[] for _ in range(0, _width)] for _ in range(0, _height)]

    def cut(self, claim: Claim):
        for h in range(0, claim.height):
            self.area[claim.y + h][claim.x:claim.x + claim.width] = [
                x + [claim.id] for x in self.area[claim.y + h][claim.x:claim.x + claim.width]]

    def simplify(self) -> Set[int]:
        items = [item for sublist in self.area for item in sublist if len(item) > 1]
        items = [item for sublist in items for item in sublist]
        return set(items)

    def overlap(self) -> int:
        area_count = 0
        for row in self.area:
            area_count += len([x for x in row if len(x) > 1])

        return area_count
