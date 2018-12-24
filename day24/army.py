from typing import List, Tuple
from .attack_type import AttackType


class Army:
    IMMUNE = 'Immune System'
    INFECTION = 'Infection'

    __type: str
    __units: int
    __hp_pet_unit: int
    __weaknesses: List[AttackType]
    __immunities: List[AttackType]
    __ap: int
    __attack_type: AttackType
    __initiative: int

    def __init__(self, _type: str, _units: int, _hp: int,
                 _weakness: List[AttackType], _immune: List[AttackType],
                 _ap: int, _attack_type: AttackType,
                 _init: int):
        self.__type = _type
        self.__units, self.__hp_pet_unit, self.__ap = _units, _hp, _ap
        self.__weaknesses = _weakness
        self.__immunities = _immune
        self.__attack_type = _attack_type
        self.__initiative = _init

    def boost(self, amount: int):
        self.__ap += amount

    def collective_ap(self) -> int:
        return self.units() * self.__ap

    def collective_hp(self) -> int:
        return self.units() * self.__hp_pet_unit

    def is_immune_to(self, t: AttackType) -> bool:
        return t in self.__immunities

    def is_weak_to(self, t: AttackType) -> bool:
        return t in self.__weaknesses

    def attack_type(self) -> AttackType:
        return self.__attack_type

    def type(self) -> str:
        return self.__type

    def initiative(self) -> int:
        return self.__initiative

    def can_attack(self, other: 'Army') -> bool:
        if self.type() == other.type():
            return False

        if other.is_immune_to(self.attack_type()):
            return False

        return True

    def attack_priority(self, other: 'Army') -> Tuple[int, int, int]:
        return self.damage_against(other), other.collective_ap(), other.initiative()

    def damage_against(self, other: 'Army') -> int:
        if other.is_immune_to(self.attack_type()):
            return 0
        damage = self.collective_ap()
        if other.is_weak_to(self.attack_type()):
            damage *= 2

        return damage

    def units(self) -> int:
        return self.__units

    def take_damage(self, amount: int) -> Tuple[bool, int]:
        killed = min(self.units(), amount // self.__hp_pet_unit)
        self.__units -= killed
        return self.is_dead(), killed

    def is_dead(self) -> bool:
        return self.collective_hp() == 0

    def attack(self, other: 'Army') -> Tuple[bool, int]:
        if other.is_dead():
            return True, 0

        amount = self.damage_against(other)

        return other.take_damage(amount)

    def __lt__(self, other: 'Army'):
        if self.collective_ap() != other.collective_ap():
            return self.collective_ap() < other.collective_ap()
        return self.initiative() < other.initiative()

    def __gt__(self, other: 'Army'):
        if self.collective_ap() != other.collective_ap():
            return self.collective_ap() > other.collective_ap()
        return self.initiative() > other.initiative()

    def __str__(self):
        if self.is_dead():
            return '[{:d}]<{:s}>(dead)'.format(id(self), self.type())

        return '[{:d}]<{:s}>({:d})'.format(id(self), self.type(), self.units())
