from advent_of_code import BaseSolution
from typing import List, Iterable, Set
from .army import Army
from .attack_type import AttackType
from .fight_pair import FightPair
from .give_up import GiveUp


class Solution(BaseSolution):
    groups: List[Army]

    def setup(self):
        self.groups = []
        (input_file, ) = self.parameters()
        line_format = r'(\d+) units each with (\d+) hit points (\(([^\)]+)\) )?with ' \
                      r'an attack that does (\d+) (\w+) damage at initiative (\d+)'
        prop_format = r'(\w+) to (.+)'
        _t: str
        for line in self.read_input(input_file):
            if line == 'Immune System:':
                _t = Army.IMMUNE
                continue
            elif line == 'Infection:':
                _t = Army.INFECTION
                continue

            if _t is None:
                raise Exception('Unit Type is not defined.')

            parts = self.parse(line, line_format, (int, int, str, str, int, str, int))
            immune, weak = [], []

            if parts[2] != str(None):
                for s in parts[3].split('; '):
                    v, values = self.parse(s, prop_format, (str, str))
                    value_list = [AttackType.from_str(x) for x in values.split(', ')]
                    if v == 'immune':
                        immune = value_list
                    else:
                        weak = value_list

            self.groups.append(Army(_t, parts[0], parts[1],
                                    weak, immune, parts[4],
                                    AttackType.from_str(parts[5]), (parts[6])))

    def types_alive(self) -> Set[str]:
        return set([g.type() for g in self.groups])

    def fight(self) -> Iterable[Army]:
        while len(self.types_alive()) > 1:
            # Target Selection Phase
            fight_pairs: List[FightPair] = []
            already_targeted = set()

            for group in sorted(self.groups, reverse=True):
                possible_targets = [g for g in self.groups if group.can_attack(g) and g not in already_targeted]
                target: Army = None
                possible_targets.sort(key=lambda x: group.attack_priority(x), reverse=True)
                if len(possible_targets) > 0:
                    target = possible_targets[0]

                if target is not None:
                    already_targeted.add(target)
                    fight_pairs.append(FightPair(group, target, group.initiative()))

            # Fight Phase
            fight_pairs.sort(key=lambda x: x.initiative, reverse=True)

            if len(fight_pairs) == 0:
                raise GiveUp(f'It seems, it is a draw. No one can attack.')
            unit_killed_this_round = False
            for fight in fight_pairs:
                if fight.army.is_dead() or fight.target.is_dead():
                    continue
                died, unit_killed = fight.army.attack(fight.target)
                if unit_killed > 0:
                    unit_killed_this_round = True
                if died:
                    self.groups.remove(fight.target)
                    yield fight.target

            if not unit_killed_this_round:
                raise GiveUp(f'It seems, it is a draw. No unit was killed in this round.')

    def boost_all_immune(self, value):
        for g in self.groups:
            if g.type() == Army.IMMUNE:
                g.boost(value)

    def part1(self):
        for dead in self.fight():
            print(dead)

        return sum(group.units() for group in self.groups)

    def part2(self):
        boost = 0

        step = 1000
        while True:
            boost += step
            print(" >>> Boost value:", boost)
            self.setup()
            self.boost_all_immune(boost)
            try:
                for _ in self.fight():
                    pass
            except GiveUp as e:
                print(e)
                continue
            if self.types_alive().pop() == Army.IMMUNE:
                if step == 1:
                    return sum(group.units() for group in self.groups)
                boost -= step
                step = max(1, step // 10)
