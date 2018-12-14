from advent_of_code import BaseSolution
from typing import List, Tuple
from .node import Node


class Solution(BaseSolution):
    root_node: Node

    def setup(self):
        (input_file, ) = self.parameters()
        numbers = [int(n) for n in self.read_input(input_file, separator=' ')]
        (self.root_node, _) = self.read(numbers)

    def read(self, _numbers: List[int]) -> Tuple[Node, List[int]]:
        current_node = Node()
        number_of_children = _numbers.pop(0)
        number_of_meta = _numbers.pop(0)

        for n in range(0, number_of_children):
            (child, _numbers) = self.read(_numbers)
            current_node.add_child(child)

        for n in range(0, number_of_meta):
            current_node.add_meta(_numbers.pop(0))

        return current_node, _numbers

    def part1(self):
        return self.root_node.sum_of_all_meta()

    def part2(self):
        return self.root_node.sum_of_all_meta_based_on_children()
