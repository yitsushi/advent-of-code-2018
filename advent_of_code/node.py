from typing import List, Any


class Node:
    children: List
    __value: Any

    def __init__(self, value: Any):
        self.children = []
        self.__value = value

    def add_child(self, child: 'Node'):
        self.children.append(child)

    def value(self):
        return self.__value
