from collections import namedtuple

Instruction = namedtuple('Instruction', 'opcode a b c')

"""
# I leave it here because why not. Now I have control over the data
# so I can use namedtuples instead of a whole new class.
# Downside: I can't use type hinting, so nor PyCharm nor Vim can
#           give me visual warning if values are not integers.
#
# TODO: Next thing to learn and get a deeper knowledge: @dataclass
class Instruction:
    opcode: str
    a: int
    b: int
    c: int

    def __init__(self, opcode: str, a: int, b: int, c: int):
        self.opcode = opcode
        self.a = a
        self.b = b
        self.c = c
"""
