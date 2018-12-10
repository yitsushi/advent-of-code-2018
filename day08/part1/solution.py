#!/usr/bin/env python3

class Node:
    children = None
    meta = None

    def __init__(self):
        self.children = []
        self.meta = []

    def add_child(self, child):
        self.children.append(child)

    def add_meta(self, meta):
        self.meta.append(meta)

    def sum_of_sub_meta(self):
        value = sum(self.meta)
        for child in self.children:
            value += child.sum_of_sub_meta()
        return value

def parse(numbers):
    node = Node()
    number_of_children = numbers.pop(0)
    number_of_meta = numbers.pop(0)

    for n in range(0, number_of_children):
        (child, numbers) = parse(numbers)
        node.add_child(child)

    for n in range(0, number_of_meta):
        node.add_meta(numbers.pop(0))

    return (node, numbers)

with open('../input') as f:
    numbers = [int(n) for n in f.read().split(' ') if n != '']

(root, _) = parse(numbers)

print(root.sum_of_sub_meta())
