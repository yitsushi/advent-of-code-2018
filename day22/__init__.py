
from advent_of_code import BaseSolution, Map2D, Vector2D
import networkx as nx
from .cell import Cell


class Solution(BaseSolution):
    depth: int
    target: Vector2D
    mouth: Vector2D
    cave: Map2D

    def setup(self):
        (self.depth, self.target) = self.parameters((int, Vector2D), ('Depth', 'Target Coordinates'), (3339, (10, 715)))
        self.mouth = Vector2D(0, 0)

        self.cave = Map2D(max(self.target.x * 2, 150), max(self.target.y * 2, 150))

        for coord in self.cave.iterate_through():
            if coord in [self.mouth, self.target]:
                geologic_index = 0
            elif coord.y == 0:
                geologic_index = coord.x * 16807
            elif coord.x == 0:
                geologic_index = coord.y * 48271
            else:
                left: Cell = self.cave.value_at(coord + Vector2D(-1, 0))
                top: Cell = self.cave.value_at(coord + Vector2D(0, -1))
                geologic_index = left.erosion * top.erosion

            current = Cell((geologic_index + self.depth) % 20183)
            self.cave.set_value_at(coord, current)

        # self.cave.draw()

    def part1(self):
        fields = [pos for pos in self.cave.iterate_through()
                  if pos < self.target if pos.x <= self.target.x and pos.y <= self.target.y]
        return sum(self.cave.value_at(pos).type() for pos in fields)

    def part2(self):
        rocky, wet, narrow = 0, 1, 2
        torch, climbing_gear, neither = 0, 1, 2
        item_matrix = {
            rocky: (torch, climbing_gear),
            wet: (climbing_gear, neither),
            neither: (torch, neither)
        }

        network = nx.Graph()
        for pos in self.cave.iterate_through():
            valid_items = item_matrix[self.cave.value_at(pos).type()]
            network.add_edge(*[(pos.x, pos.y, item) for item in valid_items], weight=7)
            for n in [p for p in self.cave.neighbors(pos, ignore=[None])]:
                valid_items_new = item_matrix[self.cave.value_at(n).type()]
                for item in set(valid_items).intersection(set(valid_items_new)):
                    network.add_edge((pos.x, pos.y, item), (n.x, n.y, item), weight=1)

        start_state = (self.mouth.y, self.mouth.y, torch)
        end_state = (self.target.x, self.target.y, torch)
        return nx.dijkstra_path_length(network, start_state, end_state)
