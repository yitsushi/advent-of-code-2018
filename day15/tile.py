from typing import Dict
from enum import Enum


class Tile(Enum):
    EMPTY = 1
    WALL = 2
    GOBLIN = 3
    ELF = 4

    @staticmethod
    def render_map() -> Dict['Tile', str]:
        return {
            Tile.EMPTY: '.',
            Tile.WALL: '#',
            Tile.GOBLIN: 'G',
            Tile.ELF: 'E'
        }

    @staticmethod
    def from_char(ch: str) -> 'Tile':
        if ch == '.':
            return Tile.EMPTY
        if ch == '#':
            return Tile.WALL
        if ch == 'G':
            return Tile.GOBLIN
        if ch == 'E':
            return Tile.ELF

        raise Exception(f'Unrecognized character: {ch}')
