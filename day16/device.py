from typing import List


class Device:
    registers: List[int]

    def __init__(self, initial_register_values: List[int] = None):
        if initial_register_values is None:
            initial_register_values = [0, 0, 0, 0]
        self.registers = initial_register_values
