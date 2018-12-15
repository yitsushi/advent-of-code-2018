from .character import Character
from .tile import Tile

class Elf(Character):
    tile_type = Tile.ELF

    def __str__(self):
        return "[{:2d}x{:2d}] Elf HP:{}".format(self.location.x, self.location.y, self.health_points)
