#!/usr/bin/env python3

import advent_of_code as aoc

(sequence_to_see, ) = aoc.parameters((str, ), ('Number of Recipes', ), ('846601', ))

recipes = [3, 7]
elves = [0, 1]

sequence_to_see = [int(ch) for ch in sequence_to_see]

while recipes[-len(sequence_to_see):] != sequence_to_see and recipes[-len(sequence_to_see)-1:-1] != sequence_to_see:
    sum_of_the_round = 0
    for i in range(0, len(elves)):
        index = elves[i] % len(recipes)
        current_score = recipes[index]
        sum_of_the_round += current_score
        elves[i] = index + current_score + 1
    recipes.extend(divmod(sum_of_the_round, 10) if sum_of_the_round >= 10 else (sum_of_the_round, ))

rounds = len(recipes) - len(sequence_to_see)
if recipes[-len(sequence_to_see):] != sequence_to_see:
    rounds -= 1

print(rounds)
