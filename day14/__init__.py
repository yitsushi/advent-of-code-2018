from advent_of_code import BaseSolution
from typing import List, Tuple


class Solution(BaseSolution):
    recipes: List[int]
    elves: List[int]
    sequence_to_see: List[int]
    number_of_recipes: int
    target: int

    def setup(self):
        (value, ) = self.parameters((str, ), ('Number of Recipes', ), ('846601', ))

        self.recipes = [3, 7]
        self.elves = [0, 1]
        self.number_of_recipes = int(value)
        self.sequence_to_see = [int(ch) for ch in value]
        self.target = 10

    def cook(self) -> Tuple[int, int]:
        sum_of_the_round = 0
        for i in range(0, len(self.elves)):
            index = self.elves[i] % len(self.recipes)
            current_score = self.recipes[index]
            sum_of_the_round += current_score
            self.elves[i] = index + current_score + 1
        new_recipes = divmod(sum_of_the_round, 10) if sum_of_the_round >= 10 else (sum_of_the_round, )
        self.recipes.extend(new_recipes)
        return new_recipes

    def part1(self) -> str:
        while len(self.recipes) < self.number_of_recipes + self.target:
            self.cook()

        return "".join([str(ch) for ch in self.recipes[self.number_of_recipes:]])

    def part2(self) -> int:
        while True:
            last_added = self.cook()
            if self.sequence_to_see[-1] in last_added:
                if self.recipes[-len(self.sequence_to_see):] == self.sequence_to_see:
                    break
                if self.recipes[-len(self.sequence_to_see)-1:-1] == self.sequence_to_see:
                    break

        rounds = len(self.recipes) - len(self.sequence_to_see)
        if self.recipes[-len(self.sequence_to_see):] != self.sequence_to_see:
            rounds -= 1

        return rounds
