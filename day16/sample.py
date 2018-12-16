from .instruction import Instruction
from .device import Device
from .opcode_map import OpcodeMap


class Sample:
    before: Device
    after: Device
    ins: Instruction

    def __init__(self, before, after, ins: Instruction):
        self.before = before
        self.after = after
        self.ins = ins

    def train(self):
        return OpcodeMap.test(self.before, self.ins, self.after, reduce=True)

    def test(self):
        return OpcodeMap.test(self.before, self.ins, self.after)
