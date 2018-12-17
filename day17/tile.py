from enum import Enum


class Tile(Enum):
    EMPTY = 0
    CLAY = 1
    WATER = 2
    WATER_ROUTE = 3
    SPRING = 4

    @staticmethod
    def render_map():
        return {
            Tile.EMPTY: '.',
            Tile.CLAY: '#',
            Tile.WATER: '~',
            Tile.SPRING: '+',
            Tile.WATER_ROUTE: '|'
        }

    @staticmethod
    def obstacles():
        return [Tile.CLAY, Tile.WATER]

    @staticmethod
    def free_to_flow():
        return [Tile.EMPTY, Tile.WATER_ROUTE]
