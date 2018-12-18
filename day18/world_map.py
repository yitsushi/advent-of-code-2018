from advent_of_code import Map2D
from .tile import Tile


class WorldMap(Map2D):
    defaultValue = Tile.OPEN

    def round(self):
        snapshot = self.snapshot()
        for pos in snapshot.iterate_through():
            values = [snapshot.value_at(p) for p in snapshot.neighbors(pos, ignore=[None], only_cardinals=False)]
            if snapshot.value_at(pos) == Tile.OPEN and values.count(Tile.TREES) > 2:
                self.set_value_at(pos, Tile.TREES)
            elif snapshot.value_at(pos) == Tile.TREES and values.count(Tile.LUMBERYARD) > 2:
                self.set_value_at(pos, Tile.LUMBERYARD)
            if snapshot.value_at(pos) == Tile.LUMBERYARD:
                if values.count(Tile.LUMBERYARD) > 0 and values.count(Tile.TREES) > 0:
                    self.set_value_at(pos, Tile.LUMBERYARD)
                else:
                    self.set_value_at(pos, Tile.OPEN)
