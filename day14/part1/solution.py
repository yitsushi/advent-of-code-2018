#!/usr/bin/env python3

import advent_of_code as aoc

(number_of_recipes, target) = aoc.parameters((int, int), ('Number of Recipes', 'Next N recipes'), (846601, 10))

recipes = [3, 7]
elves = [0, 1]

while len(recipes) < number_of_recipes + target:
    sum_of_the_round = 0
    for i in range(0, len(elves)):
        index = elves[i] % len(recipes)
        current_score = recipes[index]
        sum_of_the_round += current_score
        elves[i] = index + current_score + 1
    [recipes.append(int(ch)) for ch in str(sum_of_the_round)]

print("".join([str(ch) for ch in recipes[number_of_recipes:]]))
