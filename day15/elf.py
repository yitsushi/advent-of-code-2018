from advent_of_code import Vector2D
from .character import Character
from .tile import Tile
from .elf_died_exception import ElfDiedException
from .world_proxy import WorldProxy


class Elf(Character):
    tile_type = Tile.ELF

    def __init__(self, _location: Vector2D, _proxy: WorldProxy, _power: int):
        super().__init__(_location, _proxy)
        self.attack_power = _power

    def __str__(self):
        return "[{:2d}x{:2d}] Elf HP:{}".format(self.location.x, self.location.y, self.health_points)

    def take_damage(self, amount: int):
        self.health_points -= amount
        if self.health_points < 1:
            raise ElfDiedException()
