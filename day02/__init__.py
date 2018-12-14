from advent_of_code import BaseSolution
from typing import List
import regex


class Solution(BaseSolution):
    idList: List[str]

    def setup(self):
        (input_file, ) = self.parameters()

        self.idList = list(self.read_input(input_file))

    def part1(self) -> int:
        has_two = 0
        has_three = 0

        for _id in self.idList:
            h = {}
            for c in set(_id):
                h[c] = _id.count(c)

            has_two += int(2 in set(h.values()))
            has_three += int(3 in set(h.values()))

        return has_two * has_three

    def part2(self) -> str:
        for index in range(0, len(self.idList)):
            current = self.idList[index]
            for _id in self.idList[index+1:]:
                result = regex.search(r'(%s){e<2}' % _id, current)
                if result is not None:
                    i = result.fuzzy_changes[0][0]
                    return current[:i] + current[i+1:]
