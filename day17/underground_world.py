from advent_of_code import Map2D, Vector2D
from typing import List
from .tile import Tile


class UndergroundWorld(Map2D):
    __skip_points: List[Vector2D] = []
    defaultValue: Tile = Tile.EMPTY
    __spring: Vector2D

    def set_spring(self, _spring: Vector2D):
        self.set_value_at(_spring, Tile.SPRING)
        self.__spring = _spring

    def flow(self, _from: Vector2D = None):
        if _from is None:
            _from = self.__spring

        if _from in self.__skip_points:
            return False

        while True:
            try:
                stale_point = self.next_stale_point(_from)
            except IndexError:
                break

            if stale_point in self.__skip_points:
                return False

            if stale_point == _from:
                return True

            fall_points, hit_the_edge = self.stale_at(stale_point)
            if hit_the_edge and len(fall_points) == 0:
                self.__skip_points.append(_from)
                return False
            if len(fall_points) > 0:
                for p in fall_points:
                    if p in self.__skip_points:
                        continue
                    if self.flow(p):
                        self.flow(_from)
                    else:
                        self.__skip_points.append(p)
                break
        return False

    def next_stale_point(self, _from: Vector2D):
        i = 1
        while True:
            pos = _from + Vector2D(0, i)
            if self.value_at(pos) in Tile.obstacles():
                return pos - Vector2D(0, 1)
            self.set_value_at(pos, Tile.WATER_ROUTE)
            i += 1

    def stale_at(self, pos: Vector2D) -> (List[Vector2D], bool):
        fall_points: List[Vector2D] = []
        fill_points: List[Vector2D] = [pos]
        hit_the_edge = False

        for _i in [-1, 1]:
            i = 0
            while True:
                i += _i
                current = pos + Vector2D(i, 0)
                if self.value_at(current) is None:
                    hit_the_edge = True
                    break
                if self.value_at(current) in Tile.obstacles():
                    break
                if self.value_at(current + Vector2D(0, 1)) in Tile.free_to_flow():
                    fall_points.append(current)
                    break
                fill_points.append(current)

        for p in fill_points + fall_points:
            v = Tile.WATER if len(fall_points) == 0 and not hit_the_edge else Tile.WATER_ROUTE
            self.set_value_at(p, v)

        return fall_points, hit_the_edge
