#!/usr/bin/env python3

import advent_of_code as aoc

(input_file, ) = aoc.parameters()
material = list(aoc.read_input(input_file))[0]

def is_opposite_polarity(a, b):
    return (a.upper() == b.upper()) and (a != b)

def test(chain, to_remove):
    chain = chain.replace(to_remove, '').replace(to_remove.upper(), '')
    i = 0
    while i < len(chain) - 1:
        if is_opposite_polarity(chain[i], chain[i+1]):
            chain = chain[:i] + chain[i+2:]
            i = max(i - 1, 0)
        else:
            i += 1
    return chain

shortest = min([len(test(material, ch)) for ch in set(list(material.lower()))])
print(shortest)
