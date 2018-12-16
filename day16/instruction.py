
class Instruction:
    opcode: int
    a: int
    b: int
    c: int

    def __init__(self, opcode, a, b, c):
        self.opcode = opcode
        self.a = a
        self.b = b
        self.c = c
