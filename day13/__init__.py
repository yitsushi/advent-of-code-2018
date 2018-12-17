from advent_of_code import BaseSolution, Vector2D
from typing import Generator
from .cart import Cart
from .tile import Tile
from .world_map import WorldMap


class Solution(BaseSolution):
    world: WorldMap

    def setup(self):
        (input_file, ) = self.parameters()
        lines = [line for line in self.read_input(input_file)]

        self.world = WorldMap(max([len(line) for line in lines]), len(lines))

        for y in range(0, len(lines)):
            for x in range(0, len(lines[y])):
                current = lines[y][x]
                if current in ['^', 'v', '>', '<']:
                    direction = Vector2D(0, 0)
                    if current == '<':
                        direction.x = -1
                    elif current == '>':
                        direction.x = 1
                    elif current == '^':
                        direction.y = -1
                    else:
                        direction.y = 1

                    self.world.add_cart(Cart(Vector2D(x, y), direction))

                    current = '|' if current in ['^', 'v'] else '-'
                self.world.set_value_at(Vector2D(x, y), Tile.from_char(current))

    def execute(self) -> Generator:
        while len(self.world.carts) > 0:
            for current_cart in sorted(self.world.carts):
                current_cart.step()
                carts_at_location = [c for c in self.world.carts if c.location == current_cart.location]
                if len(carts_at_location) > 1:
                    yield carts_at_location
                current = self.world.value_at(current_cart.location)
                if current == Tile.TURN:
                    current_cart.velocity.rotate(90)
                    looking_for = [Tile.by_direction(current_cart.velocity), Tile.INTERSECT]
                    if self.world.value_at(current_cart.location + current_cart.velocity) not in looking_for:
                        current_cart.velocity.rotate(180)
                elif current == Tile.INTERSECT:
                    current_cart.turn_at_intersection()

            # world.draw(replace=self.world.replace_map, place=self.world.carts)

    def part1(self):
        for crashed_carts in self.execute():
            return crashed_carts.pop(0).location

    def part2(self):
        for crashed_carts in self.execute():
            for c in crashed_carts:
                self.world.carts.remove(c)

            if len(self.world.carts) == 1:
                return self.world.carts.pop(0).location
