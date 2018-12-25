from advent_of_code import BaseSolution
from typing import List
import networkx as nx
from .time_space_vector import TimeSpaceVector


class Solution(BaseSolution):
    points: List[TimeSpaceVector]
    network: nx.Graph

    def setup(self):
        (input_file, ) = self.parameters()
        lines = self.read_input(input_file)
        self.points = [TimeSpaceVector(*[int(x) for x in line.split(',')]) for line in lines]

        self.network = nx.Graph()
        for p1 in self.points:
            for p2 in self.points:
                if self.manhattan(p1, p2) <= 3:
                    self.network.add_edge(p1, p2)

    @staticmethod
    def manhattan(v1: TimeSpaceVector, v2: TimeSpaceVector):
        return abs(v1.x - v2.x) + abs(v1.y - v2.y) + abs(v1.z - v2.z) + abs(v1.t - v2.t)

    def part1(self):
        return nx.number_connected_components(self.network)

    def part2(self):
        return 'Done! ;)'
