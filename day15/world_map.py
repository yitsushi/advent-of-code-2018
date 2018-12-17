from advent_of_code import Map2D
from typing import List, Type, Dict, Any
from .tile import Tile
from .character import Character
from .goblin import Goblin
from .elf import Elf
from .elf_died_exception import ElfDiedException


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
        return [c for c in self.characters if isinstance(c, _type) and c.hp() > 0]

    def characters_in_reading_order(self) -> List[Character]:
        return sorted(self.characters, key=lambda x: x.location)

    def draw(self, replace: Dict[Any, Any] = None, place: List[Any] = None):
        self.snapshot().draw(replace=replace, place=place)

    def round(self):
        elf_indicator = 0
        for ch in self.characters_in_reading_order():
            if ch.hp() < 1:
                continue

            try:
                ch.round()
            except ElfDiedException:
                elf_indicator = -1

            if len(self.list_all(Elf)) < 1:
                print('Goblins won!')
                return self.number_of_rounds, sum([c.hp() for c in self.list_all(Goblin)])
            if len(self.list_all(Goblin)) < 1:
                print('Elves won!')
                return self.number_of_rounds, sum([c.hp() for c in self.list_all(Elf)])

        self.clear_dead_bodies()
        self.number_of_rounds += 1

        return self.number_of_rounds, elf_indicator

    def clear_dead_bodies(self):
        self.characters = [c for c in self.characters if c.hp() > 0]

    def snapshot(self) -> Map2D:
        snapshot: Map2D = Map2D(self.width(), self.height())
        goblin_locations = [c.location for c in self.list_all(Goblin)]
        elf_locations = [c.location for c in self.list_all(Elf)]
        for location in self.iterate_through():
            snapshot.set_value_at(location, self.value_at(location))
            if location in goblin_locations:
                snapshot.set_value_at(location, Tile.GOBLIN)
            if location in elf_locations:
                snapshot.set_value_at(location, Tile.ELF)

        return snapshot
