from advent_of_code import BaseSolution, Vector2D
from .world_map import WorldMap
from .world_proxy import WorldProxy
from .tile import Tile
from .elf import Elf
from .goblin import Goblin
from .elf_died_exception import ElfDiedException


class Solution(BaseSolution):
    world: WorldMap

    def setup(self, elf_power: int = 3):
        (input_file, ) = self.parameters()
        lines = list(self.read_input(input_file))

        self.world = WorldMap(len(lines[0]), len(lines))

        elf_proxy = WorldProxy(Elf, Goblin, self.world)
        goblin_proxy = WorldProxy(Goblin, Elf, self.world)

        for y in range(0, len(lines)):
            for x in range(0, len(lines[y])):
                location = Vector2D(x, y)
                value = Tile.from_char(lines[y][x])

                if value == Tile.ELF:
                    self.world.add_character(Elf(location, elf_proxy, elf_power))
                    value = Tile.EMPTY
                elif value == Tile.GOBLIN:
                    self.world.add_character(Goblin(location, goblin_proxy))
                    value = Tile.EMPTY

                self.world.set_value_at(location, value)

    def play(self, stop_if_an_elf_dies: bool = False):
        while True:
            rounds, remaining_hp = self.world.round()
            if remaining_hp < 0 and stop_if_an_elf_dies:
                raise ElfDiedException()
            if remaining_hp > 0:
                print('Number of rounds: ', rounds)
                print('HP left: ', remaining_hp)
                return rounds * remaining_hp

    def part1(self):
        return self.play()

    def part2(self):
        x = 4
        while True:
            print(f'Elf power: {x}')
            self.setup(x)
            try:
                return self.play(stop_if_an_elf_dies=True)
            except ElfDiedException:
                x += 1
                continue
