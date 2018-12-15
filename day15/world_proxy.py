from advent_of_code.data_structure import Vector2D
from advent_of_code.data_structure import Map2D
from typing import Type, List
from .tile import Tile


class WorldProxy:
    __class: Type
    __enemy: Type
    __world: Map2D

    def __init__(self, _class: Type, _enemy: Type, _world: Map2D):
        self.__class = _class
        self.__enemy = _enemy
        self.__world = _world

    def enemies_in_range(self, location: Vector2D):
        return [c for c in self.__world.list_all(self.__enemy)
                if c.location in self.__world.neighbors(location, ignore=[Tile.WALL])]

    def closet_enemy_target_location(self, location: Vector2D):
        all_enemies = self.__world.list_all(self.__enemy)
        if len(all_enemies) < 1:
            return None

        possibilities = [(l, c) for c in all_enemies for l in self.__world.neighbors(c.location, ignore=[Tile.WALL])]
        occupied_spots = [c.location for c in self.__world.list_all(None)]
        possible_targets = sorted([((l[0]-location).manhattan(), l[0], l[1])
                                   for l in possibilities if l[0] not in occupied_spots])
        if len(possible_targets) < 1:
            return None

        if len(possible_targets) < 2:
            return possible_targets[0]

        closest = min(possible_targets)
        all_closest = [v for v in possible_targets if v[0] == closest[0]]
        if len(all_closest) < 2:
            return all_closest[0]

        '''
        Shit! I have to propagate down the enemy too, or I can't compare their HP :(
        '''
        all_closest.sort(key=lambda x: x[2].hp())
        return all_closest[0]

    def find_path(self, _from: Vector2D, _to: Vector2D):
        m: Map2D = self.__world.snapshot()
        return m.shortest_path(_from, _to, obstacles=[Tile.WALL, self.__class.tile_type])
