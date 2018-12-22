from dataclasses import dataclass


@dataclass
class Cell:
    erosion: int

    def type(self):
        return self.erosion % 3

    def map_tile_format(self):
        return str(self)

    def __str__(self):
        mod = self.type()
        if mod == 0:
            return '.'
        elif mod == 1:
            return '='
        else:
            return '|'
