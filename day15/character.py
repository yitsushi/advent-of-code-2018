from advent_of_code.data_structure import Player, Vector2D
from .world_proxy import WorldProxy
from .tile import Tile


class Character(Player):
    health_points: int
    attack_power: int
    __proxy: WorldProxy
    tile_type: Tile

    def __init__(self, _location: Vector2D, _proxy: WorldProxy):
        super().__init__(_location, Vector2D(0, 0))
        self.health_points = 200
        self.attack_power = 3
        self.__proxy = _proxy

    def hp(self):
        return self.health_points

    def ap(self):
        return self.attack_power

    def __lt__(self, other: 'Character'):
        if self.hp() != other.hp():
            return self.hp() < other.hp()
        return self.location < other.location

    def take_damage(self, amount: int):
        self.health_points -= amount

    def attack(self, other: 'Character'):
        other.take_damage(self.ap())

    def round(self):
        # Attack if in range
        enemies = self.__proxy.enemies_in_range(self.location)
        if len(enemies) > 0:
            self.attack(sorted(enemies)[0])
            return

        # Move to range
        route = self.__proxy.find_path_to_enemy(self.location)
        if route is None:
            return
        self.location = route[1]

        # Attack if in range
        enemies = self.__proxy.enemies_in_range(self.location)
        if len(enemies) > 0:
            self.attack(sorted(enemies)[0])
            return
