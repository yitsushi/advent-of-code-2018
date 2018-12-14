from advent_of_code.data_structure import Node as BaseNode
from typing import List


class Node(BaseNode):
    children: List['Node']
    meta: List[int]

    def __init__(self):
        super().__init__()
        self.meta = []

    def add_meta(self, meta: int):
        self.meta.append(meta)

    def sum_of_all_meta(self) -> int:
        value = sum(self.meta)
        for child in self.children:
            value += child.sum_of_all_meta()
        return value

    def sum_of_all_meta_based_on_children(self) -> int:
        if len(self.children) == 0:
            return sum(self.meta)

        value = 0
        for n in self.meta:
            if n > len(self.children):
                continue
            value += self.children[n-1].sum_of_all_meta_based_on_children()
        return value
