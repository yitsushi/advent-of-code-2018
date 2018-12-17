from advent_of_code import Vector2D
from enum import Enum


class Tile(Enum):
    EMPTY = 0             # ' '
    ROUTE_HORIZONTAL = 1  # -
    ROUTE_VERTICAL = 2    # |
    TURN = 3              # \ /
    INTERSECT = 4         # +

    @staticmethod
    def from_char(char: str):
        if char == ' ':
            return Tile.EMPTY
        elif char == '-':
            return Tile.ROUTE_HORIZONTAL
        elif char == '|':
            return Tile.ROUTE_VERTICAL
        elif char == '+':
            return Tile.INTERSECT
        elif char in ['/', '\\']:
            return Tile.TURN
        else:
            raise Exception(f'Unexpected character: {char}')

    @staticmethod
    def reverse(facing: Vector2D):
        if facing.x != 0:
            return Tile.ROUTE_VERTICAL
        elif facing.y != 0:
            return Tile.ROUTE_HORIZONTAL
        else:
            raise Exception(f'Unexpected facing: {facing}')

    @staticmethod
    def by_direction(facing: Vector2D):
        if facing.x == 0:
            return Tile.ROUTE_VERTICAL
        elif facing.y == 0:
            return Tile.ROUTE_HORIZONTAL
        else:
            raise Exception(f'Unexpected facing: {facing}')
