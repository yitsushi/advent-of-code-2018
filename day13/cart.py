from advent_of_code.data_structure import Player
from typing import Tuple


class Cart(Player):
    TurnRotation: Tuple[int] = [-90, 0, 90]

    def turn_at_intersection(self):
        super().turn(Cart.TurnRotation[self._number_of_turns % len(Cart.TurnRotation)])
