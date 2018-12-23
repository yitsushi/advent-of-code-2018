from advent_of_code import Vector3D


class Bot(Vector3D):
    __range: int

    def range(self):
        return self.__range

    def set_range(self, r: int):
        self.__range = r

    def __lt__(self, other: 'Bot'):
        if self.range() != other.range():
            return self.range() < other.range()

        return super().__lt__(other)
