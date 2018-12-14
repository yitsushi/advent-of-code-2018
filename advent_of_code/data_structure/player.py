from .vector_2d import Vector2D


class Player:
    location: Vector2D
    facing: Vector2D

    _number_of_turns: int
    _number_of_steps: int

    def __init__(self, _location: Vector2D, _facing: Vector2D):
        self.location = _location
        self.facing = _facing
        self._number_of_turns = 0
        self._number_of_steps = 0

    def __lt__(self, other):
        return self.location < other.location

    def __str__(self):
        return "{} <{}> <{}>".format(id(self), self.location, self.facing)

    def step(self):
        self.location += self.facing
        self._number_of_steps += 1

    def turn(self, degrees: int):
        self.facing.rotate(degrees)
        self._number_of_turns += 1
