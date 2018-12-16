from typing import Dict, List
from .device import Device
from .instruction import Instruction


class OpcodeMap:
    int_to_opcode_map: Dict[int, callable]
    possible_mapping: Dict[int, List[callable]]

    @staticmethod
    def initialize():
        OpcodeMap.int_to_opcode_map = {}
        OpcodeMap.possible_mapping = {}
        for i in range(0, 16):
            operations = [
                OpcodeMap.addr, OpcodeMap.addi,
                OpcodeMap.mulr, OpcodeMap.muli,
                OpcodeMap.banr, OpcodeMap.bani,
                OpcodeMap.borr, OpcodeMap.bori,
                OpcodeMap.setr, OpcodeMap.seti,
                OpcodeMap.gtir, OpcodeMap.gtri, OpcodeMap.gtrr,
                OpcodeMap.eqir, OpcodeMap.eqri, OpcodeMap.eqrr
            ]
            OpcodeMap.possible_mapping[i] = operations

    @staticmethod
    def execute(_dev: Device, _ins: Instruction):
        if _ins.opcode in OpcodeMap.int_to_opcode_map:
            op = OpcodeMap.int_to_opcode_map[_ins.opcode]
            _dev.registers[_ins.c] = op(_dev, _ins)
            return
        print(OpcodeMap.possible_mapping[_ins.opcode])
        raise Exception(f'Execution error. {_ins.opcode} is not defined.')

    @staticmethod
    def test(_dev: Device, _ins: Instruction, _expected: Device, reduce: bool = False):
        if reduce and _ins.opcode in OpcodeMap.int_to_opcode_map:
            return 1

        valid: List[callable] = []
        expected_value = _expected.registers[_ins.c]
        for op in OpcodeMap.possible_mapping[_ins.opcode]:
            if expected_value == op(_dev, _ins):
                valid.append(op)

        if len(valid) == 1:
            op = valid[0]
            OpcodeMap.int_to_opcode_map[_ins.opcode] = op
            if reduce:
                for code in OpcodeMap.possible_mapping:
                    if op in OpcodeMap.possible_mapping[code]:
                        OpcodeMap.possible_mapping[code].remove(op)

        if reduce:
            OpcodeMap.possible_mapping[_ins.opcode] = valid

        return len(valid)

    # Addition
    @staticmethod
    def addr(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] + _dev.registers[_ins.b]

    @staticmethod
    def addi(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] + _ins.b

    # Multiplication
    @staticmethod
    def mulr(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] * _dev.registers[_ins.b]

    @staticmethod
    def muli(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] * _ins.b

    # Bitwise AND
    @staticmethod
    def banr(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] & _dev.registers[_ins.b]

    @staticmethod
    def bani(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] & _ins.b

    # Bitwise OR
    @staticmethod
    def borr(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] | _dev.registers[_ins.b]

    @staticmethod
    def bori(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a] | _ins.b

    # Assignment
    @staticmethod
    def setr(_dev: Device, _ins: Instruction):
        return _dev.registers[_ins.a]

    def seti(_dev: Device, _ins: Instruction):
        return _ins.a

    # Greater-then testing
    @staticmethod
    def gtir(_dev: Device, _ins: Instruction):
        if _ins.a > _dev.registers[_ins.b]:
            return 1
        return 0

    @staticmethod
    def gtri(_dev: Device, _ins: Instruction):
        if _dev.registers[_ins.a] > _ins.b:
            return 1
        return 0

    @staticmethod
    def gtrr(_dev: Device, _ins: Instruction):
        if _dev.registers[_ins.a] > _dev.registers[_ins.b]:
            return 1
        return 0

    # Equality testing
    @staticmethod
    def eqir(_dev: Device, _ins: Instruction):
        if _ins.a == _dev.registers[_ins.b]:
            return 1
        return 0

    @staticmethod
    def eqri(_dev: Device, _ins: Instruction):
        if _dev.registers[_ins.a] == _ins.b:
            return 1
        return 0

    @staticmethod
    def eqrr(_dev: Device, _ins: Instruction):
        if _dev.registers[_ins.a] == _dev.registers[_ins.b]:
            return 1
        return 0


OpcodeMap.initialize()
