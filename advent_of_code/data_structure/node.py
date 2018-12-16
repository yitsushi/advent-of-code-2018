from typing import List


class Node:
    children: List

    def __init__(self):
        self.children = []

    def add_child(self, child: 'Node'):
        self.children.append(child)
