from enum import Enum


class Tile(Enum):
    OPEN = 0
    TREES = 1
    LUMBERYARD = 2

    @staticmethod
    def render_map():
        return {
            Tile.OPEN: '.',
            Tile.TREES: '|',
            Tile.LUMBERYARD: '#'
        }

    @staticmethod
    def from_char(ch: str) -> 'Tile':
        if ch == '#':
            return Tile.LUMBERYARD
        if ch == '|':
            return Tile.TREES
        if ch == '.':
            return Tile.OPEN

        raise Exception(f'Unrecognized character: {ch}')

    @staticmethod
    def to_string(t: 'Tile') -> str:
        rm = Tile.render_map()
        return rm[t]
