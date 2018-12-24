from enum import Enum


class AttackType(Enum):
    FIRE = 0
    COLD = 1
    SLASH = 2
    BLUDGEON = 3
    RADIATION = 4

    @staticmethod
    def from_str(s: str):
        if s == 'fire':
            return AttackType.FIRE
        if s == 'cold':
            return AttackType.COLD
        if s == 'slashing':
            return AttackType.SLASH
        if s == 'bludgeoning':
            return AttackType.BLUDGEON
        if s == 'radiation':
            return AttackType.RADIATION
        raise Exception(f'Unexpected Attack Type: {s}')
