from advent_of_code.data_structure import Map2D
from typing import List, Type, Dict, Any
from .tile import Tile
from .character import Character
from .goblin import Goblin
from .elf import Elf


class WorldMap(Map2D):
    defaultValue: Tile = Tile.EMPTY
    characters: List[Character]
    number_of_rounds: int

    def __init__(self, _width: int, _height: int):
        super().__init__(_width, _height)
        self.characters = []
        self.number_of_rounds = 0

    def add_character(self, c: Character):
        self.characters.append(c)

    def list_all(self, _type: Type = None):
        if _type is None:
            _type = Character
        return [c for c in self.characters if isinstance(c, _type)]

    def characters_in_reading_order(self) -> List[Character]:
        return sorted(self.characters, key=lambda x: x.location)

    def draw(self, replace: Dict[Any, Any] = None, place: List[Any] = None):
        self.snapshot().draw(replace=replace, place=place)

    def round(self):
        for ch in self.characters_in_reading_order():
            # print(ch)
            ch.round()
        self.number_of_rounds += 1

    def clear_dead_bodies(self):
        self.characters = [c for c in self.characters if c.hp() > 0]

    def snapshot(self) -> Map2D:
        snapshot: Map2D = Map2D(self.width(), self.height())
        goblin_locations = [c.location for c in self.characters if isinstance(c, Goblin)]
        elf_locations = [c.location for c in self.characters if isinstance(c, Elf)]
        for location in self.iterate_through():
            snapshot.set_value_at(location, self.value_at(location))
            if location in goblin_locations:
                snapshot.set_value_at(location, Tile.GOBLIN)
            if location in elf_locations:
                snapshot.set_value_at(location, Tile.ELF)

        return snapshot
