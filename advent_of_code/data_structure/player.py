from .vector_2d import Vector2D


class Player:
    location: Vector2D
    velocity: Vector2D

    _number_of_turns: int
    _number_of_steps: int

    def __init__(self, _location: Vector2D, _velocity: Vector2D):
        self.location = _location
        self.velocity = _velocity
        self._number_of_turns = 0
        self._number_of_steps = 0

    def __lt__(self, other):
        return self.location < other.location

    def __str__(self):
        return "{} <{}> <{}>".format(id(self), self.location, self.velocity)

    def number_of_steps(self) -> int:
        return self._number_of_steps

    def number_of_turns(self) -> int:
        return self._number_of_turns

    def step(self, count: int = 1):
        self.location += Vector2D(self.velocity.x * count, self.velocity.y * count)
        self._number_of_steps += count

    def turn(self, degrees: int):
        self.velocity.rotate(degrees)
        self._number_of_turns += 1
