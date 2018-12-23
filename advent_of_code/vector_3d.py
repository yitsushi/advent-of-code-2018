class Vector3D:
    x: int
    y: int
    z: int

    def __init__(self, _x: int, _y: int, _z: int):
        (self.x, self.y, self.z) = _x, _y, _z

    def __eq__(self, other: 'Vector3D'):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other: 'Vector3D'):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3D'):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return '{:d}x{:d}x{:d}'.format(self.x, self.y, self.z)

    def __lt__(self, other: 'Vector3D'):
        if self.z != other.z:
            return self.z < other.z
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

    def manhattan(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)
