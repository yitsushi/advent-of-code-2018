class Claim:
    id = 0
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, _id: int, x: int, y: int, _width: int, _height: int):
        self.id = _id
        self.x = x
        self.y = y
        self.width = _width
        self.height = _height
