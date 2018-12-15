from advent_of_code import BaseSolution
from advent_of_code.data_structure import Vector2D
from .world_map import WorldMap
from .world_proxy import WorldProxy
from .tile import Tile
from .elf import Elf
from .goblin import Goblin


class Solution(BaseSolution):
    world: WorldMap

    def setup(self):
        (input_file, ) = self.parameters()
        lines = list(self.read_input(input_file))

        self.world = WorldMap(len(lines[0]), len(lines))

        elf_proxy = WorldProxy(Elf, Goblin, self.world)
        goblin_proxy = WorldProxy(Goblin, Elf, self.world)

        for y in range(0, len(lines)):
            for x in range(0 , len(lines[y])):
                location = Vector2D(x, y)
                value = Tile.from_char(lines[y][x])

                if value == Tile.ELF:
                    self.world.add_character(Elf(location, elf_proxy))
                    value = Tile.EMPTY
                elif value == Tile.GOBLIN:
                    self.world.add_character(Goblin(location, goblin_proxy))
                    value = Tile.EMPTY

                self.world.set_value_at(location, value)

    def part1(self):
        while True:
            self.world.clear_dead_bodies()
            if len(self.world.list_all(Elf)) < 1:
                total_hp_left = sum([c.hp() for c in self.world.list_all(Goblin)])
                print('Goblins won!')
                break
            if len(self.world.list_all(Goblin)) < 1:
                total_hp_left = sum([c.hp() for c in self.world.list_all(Elf)])
                print('Elves won!')
                break

            '''
            print(self.world.number_of_rounds)
            self.world.draw(replace=Tile.render_map())
            print()
            '''
            self.world.round()

        self.world.draw(replace=Tile.render_map())
        print('Number of rounds: ', self.world.number_of_rounds)
        print('HP left: ', total_hp_left)
        return self.world.number_of_rounds * total_hp_left
