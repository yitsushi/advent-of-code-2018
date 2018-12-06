#!/usr/bin/env python3

material = None

with open('../input') as f:
    material = f.read().strip()

def is_opposite_polarity(a, b):
    return (a.upper() == b.upper()) and (a != b)

def doit(chain):
    i = 0
    while i < len(chain) - 1:
        if is_opposite_polarity(chain[i], chain[i+1]):
            chain = chain[:i] + chain[i+2:]
            i = max(i - 1, 0)
        else:
            i += 1
    return chain

print(len(doit(material)))
