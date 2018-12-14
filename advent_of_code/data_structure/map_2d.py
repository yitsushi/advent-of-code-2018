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

    def height(self) -> int:
        return self.__height

    def width(self) -> int:
        return self.__width

    def is_on_map(self, x: int, y: int):
        return 0 <= x < self.__width and 0 <= y < self.__height

    def set_value_at(self, position: Vector2D, value: Any):
        self.__area[position.y][position.x] = value

    def edge_values(self) -> List[Any]:
        """
        Edge (no pun intended) case, but sometimes we can remove items based on these values
        """
        horizontal = self.__area[0] + self.__area[self.__height - 1]
        vertical = [l[0] for l in self.__area] + [l[self.__width - 1] for l in self.__area]
        return horizontal + vertical

    def flatten(self) -> List[Any]:
        return [x for line in self.__area for x in line]

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
