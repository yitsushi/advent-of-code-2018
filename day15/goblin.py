from .character import Character
from .tile import Tile


class Goblin(Character):
    tile_type = Tile.GOBLIN

    def __str__(self):
        return "[{:2d}x{:2d}] Goblin HP:{}".format(self.location.x, self.location.y, self.health_points)
