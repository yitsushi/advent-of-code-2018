from typing import List, Dict, Callable
from .instruction import Instruction


class Device(object):
    __source: List[Instruction]
    __ip_index: int
    __registers: List[int]

    def __init__(self):
        self.__registers = [0] * 6
        self.__ip_index = 0
        self.__source = []

    def registers(self) -> List[int]:
        return self.__registers

    def set_register(self, index: int, value: int):
        self.__registers[index] = value

    def load_program(self, _source: List[Instruction], _ip_index: int):
        self.__source = _source
        self.__ip_index = _ip_index

    def get_source_line(self, index):
        return self.__source[index]

    def run(self):
        print('# Run: {}'.format(len(self.__source)))
        while not self.__is_out_of_program():
            self.__execute(self.__source[self.__registers[self.__ip_index]])
            self.__registers[self.__ip_index] += 1

    def __is_out_of_program(self):
        return (self.__registers[self.__ip_index] < 0) or\
               (self.__registers[self.__ip_index] >= len(self.__source))

    def __execute(self, _ins: Instruction):
        _op = self.__ops()[_ins.opcode]
        _op(_ins)

    def __ops(self) -> Dict[str, Callable]:
        return {
            "addr": self.__op_addr,
            "addi": self.__op_addi,
            "mulr": self.__op_mulr,
            "muli": self.__op_muli,
            "banr": self.__op_banr,
            "bani": self.__op_bani,
            "borr": self.__op_borr,
            "bori": self.__op_bori,
            "setr": self.__op_setr,
            "seti": self.__op_seti,
            "gtir": self.__op_gtir,
            "gtri": self.__op_gtri,
            "gtrr": self.__op_gtrr,
            "eqir": self.__op_eqir,
            "eqri": self.__op_eqri,
            "eqrr": self.__op_eqrr
        }

    # Addition
    def __op_addr(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] + self.__registers[_ins.b]

    def __op_addi(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] + _ins.b

    # Multiplication
    def __op_mulr(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] * self.__registers[_ins.b]

    def __op_muli(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] * _ins.b

    # Bitwise AND
    def __op_banr(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] & self.__registers[_ins.b]

    def __op_bani(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] & _ins.b

    # Bitwise OR
    def __op_borr(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] | self.__registers[_ins.b]

    def __op_bori(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a] | _ins.b

    # Assignment
    def __op_setr(self, _ins: Instruction):
        self.__registers[_ins.c] = self.__registers[_ins.a]

    def __op_seti(self, _ins: Instruction):
        self.__registers[_ins.c] = _ins.a

    # Greater-then testing
    def __op_gtir(self, _ins: Instruction):
        if _ins.a > self.__registers[_ins.b]:
            self.__registers[_ins.c] = 1
        else:
            self.__registers[_ins.c] = 0

    def __op_gtri(self, _ins: Instruction):
        if self.__registers[_ins.a] > _ins.b:
            self.__registers[_ins.c] = 1
        else:
            self.__registers[_ins.c] = 0

    def __op_gtrr(self, _ins: Instruction):
        if self.__registers[_ins.a] > self.__registers[_ins.b]:
            self.__registers[_ins.c] = 1
        else:
            self.__registers[_ins.c] = 0

    # Equality testing
    def __op_eqir(self, _ins: Instruction):
        if _ins.a == self.__registers[_ins.b]:
            self.__registers[_ins.c] = 1
        else:
            self.__registers[_ins.c] = 0

    def __op_eqri(self, _ins: Instruction):
        if self.__registers[_ins.a] == _ins.b:
            self.__registers[_ins.c] = 1
        else:
            self.__registers[_ins.c] = 0

    def __op_eqrr(self, _ins: Instruction):
        if self.__registers[_ins.a] == self.__registers[_ins.b]:
            self.__registers[_ins.c] = 1
        else:
            self.__registers[_ins.c] = 0
