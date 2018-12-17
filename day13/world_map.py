from advent_of_code import Map2D, Vector2D
from typing import List, Dict
from .tile import Tile
from .cart import Cart


class WorldMap(Map2D):
    defaultValue = Tile.EMPTY
    carts: List[Cart]
    replace_map: Dict[Tile, str]

    def __init__(self, _width: int, _height: int):
        super().__init__(_width, _height)
        self.carts = []

        self.replace_map = {
            Tile.ROUTE_HORIZONTAL: '-',
            Tile.ROUTE_VERTICAL: '|',
            Tile.EMPTY: ' ',
            Tile.TURN: '+',
            Tile.INTERSECT: '+'
        }

    def add_cart(self, _cart: Cart):
        self.carts.append(_cart)

    def has_cart_at(self, position: Vector2D):
        return any([c.location == position for c in self.carts])
