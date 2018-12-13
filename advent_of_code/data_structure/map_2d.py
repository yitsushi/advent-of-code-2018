from typing import List, Any, Dict
from .vector_2d import Vector2D


class Map2D:
    defaultValue: 0
    __area: List[List[Any]]
    __width: int
    __height: int

    def __init__(self, _width: int, _height: int):
        self.__width = _width
        self.__height = _height
        self.__area = [[self.defaultValue] * _width for _ in range(0, _height)]

    def value_at(self, position: Vector2D):
        if 0 <= position.x < self.__width and 0 <= position.y < self.__height:
            return self.__area[position.y][position.x]

        return None

    def set_value_at(self, position: Vector2D, value: Any):
        self.__area[position.y][position.x] = value

    def draw(self, replace: Dict[Any, Any] = None, place: List[Any] = None):
        if replace is None:
            replace = {}
        if place is None:
            place = []

        for y in range(0, self.__height):
            for x in range(0, self.__width):
                pos = Vector2D(x, y)
                value = self.value_at(pos)

                if pos in [item.location for item in place]:
                    print("o", end='')
                elif value in replace:
                    print(replace[value], end='')
                else:
                    print(value, end='')
            print()

