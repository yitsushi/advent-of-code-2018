#!/usr/bin/env python3

with open('../input') as f:
    idList = [id for id in f.read().split('\n') if id != '']

repeating_letters = {}

def check(h, num):
    for c in h:
        if h[c] == num:
            return True
    return False

def hash(word):
    h = {}
    for c in word:
        h[c] = h.get(c, 0) + 1

    return h

has_two = 0
has_three = 0

for id in idList:
    h = hash(id)
    if check(h, 2):
        has_two += 1
    if check(h, 3):
        has_three += 1

print(has_two * has_three)
