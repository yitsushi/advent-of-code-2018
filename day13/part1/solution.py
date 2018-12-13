#!/usr/bin/env python3

import advent_of_code as aoc
from advent_of_code import data_structure as ds
from typing import List, Dict, Tuple
from enum import Enum


class Tile(Enum):
    EMPTY = 0             # ' '
    ROUTE_HORIZONTAL = 1  # -
    ROUTE_VERTICAL = 2    # |
    TURN = 3              # \ /
    INTERSECT = 4         # +

    @staticmethod
    def from_char(char: str):
        if char == ' ':
            return Tile.EMPTY
        elif char == '-':
            return Tile.ROUTE_HORIZONTAL
        elif char == '|':
            return Tile.ROUTE_VERTICAL
        elif char == '+':
            return Tile.INTERSECT
        elif char in ['/', '\\']:
            return Tile.TURN
        else:
            raise Exception(f'Unexpected character: {char}')

    @staticmethod
    def reverse(facing: ds.Vector2D):
        if facing.x != 0:
            return Tile.ROUTE_VERTICAL
        elif facing.y != 0:
            return Tile.ROUTE_HORIZONTAL
        else:
            raise Exception(f'Unexpected facing: {facing}')

    @staticmethod
    def by_direction(facing: ds.Vector2D):
        if facing.x == 0:
            return Tile.ROUTE_VERTICAL
        elif facing.y == 0:
            return Tile.ROUTE_HORIZONTAL
        else:
            raise Exception(f'Unexpected facing: {facing}')


class Cart:
    TurnRotation: Tuple[int] = [-90, 0, 90]

    location: ds.Vector2D
    facing: ds.Vector2D

    __number_of_turns: int
    __number_of_steps: int

    def __init__(self, _location: ds.Vector2D, _facing: ds.Vector2D):
        self.location = _location
        self.facing = _facing
        self.__number_of_turns = 0
        self.__number_of_steps = 0

    def __lt__(self, other):
        return self.location < other.location

    def __str__(self):
        return "{} <{}> <{}>".format(id(self), self.location, self.facing)

    def step(self):
        self.location += self.facing
        self.__number_of_steps += 1

    def turn(self):
        self.facing.rotate(Cart.TurnRotation[self.__number_of_turns % len(Cart.TurnRotation)])
        self.__number_of_turns += 1


class WorldMap(ds.Map2D):
    defaultValue = Tile.EMPTY
    area: List[List[Tile]]
    carts: List[Cart]

    def __init__(self, _width: int, _height: int):
        super(WorldMap, self).__init__(_width, _height)
        self.carts = []

    def add_cart(self, _cart: Cart):
        self.carts.append(_cart)

    def has_cart_at(self, position: ds.Vector2D):
        return any([c.location == position for c in self.carts])


(input_file, ) = aoc.parameters()
lines = [line for line in aoc.read_input(input_file)]

world = WorldMap(max([len(line) for line in lines]), len(lines))

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        current = lines[y][x]
        if current in ['^', 'v', '>', '<']:
            direction = ds.Vector2D(0, 0)
            if current == '<':
                direction.x = -1
            elif current == '>':
                direction.x = 1
            elif current == '^':
                direction.y = -1
            else:
                direction.y = 1

            world.add_cart(Cart(ds.Vector2D(x, y), direction))

            current = '|' if current in ['^', 'v'] else '-'
        world.set_value_at(ds.Vector2D(x, y), Tile.from_char(current))

replace_map: Dict[Tile, str] = {
    Tile.ROUTE_HORIZONTAL: '-',
    Tile.ROUTE_VERTICAL: '|',
    Tile.EMPTY: ' ',
    Tile.TURN: '+',
    Tile.INTERSECT: '+'
}

crashHappened = False
while not crashHappened:
    world.carts.sort()
    for cart in world.carts:
        if world.has_cart_at(cart.location + cart.facing):
            crashHappened = True
            print(" >>> CRASH:", cart.location + cart.facing)
            break
        cart.step()
        current = world.value_at(cart.location)
        if current == Tile.TURN:
            cart.facing.rotate(90)
            looking_for = [Tile.by_direction(cart.facing), Tile.INTERSECT]
            if world.value_at(cart.location + cart.facing) not in looking_for:
                cart.facing.rotate(180)
        elif current == Tile.INTERSECT:
            cart.turn()

    # world.draw(replace=replace_map, place=world.carts)
