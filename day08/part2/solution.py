#!/usr/bin/env python3

import advent_of_code as aoc
from typing import List


class Node:
    children = None
    meta = None

    def __init__(self):
        self.children = []
        self.meta = []

    def add_child(self, child):
        self.children.append(child)

    def add_meta(self, meta: List[int]):
        self.meta.append(meta)

    def sum_of_sub_meta(self):
        if len(self.children) == 0:
            return sum(self.meta)

        value = 0
        for n in self.meta:
            if n > len(self.children):
                continue
            value += self.children[n-1].sum_of_sub_meta()
        return value


def parse(_numbers):
    node = Node()
    number_of_children = _numbers.pop(0)
    number_of_meta = _numbers.pop(0)

    for n in range(0, number_of_children):
        (child, _numbers) = parse(_numbers)
        node.add_child(child)

    for n in range(0, number_of_meta):
        node.add_meta(_numbers.pop(0))

    return node, _numbers


(input_file, ) = aoc.parameters()
numbers = [int(n) for n in aoc.read_input(input_file, separator=' ')]

(root, _) = parse(numbers)

print(root.sum_of_sub_meta())
