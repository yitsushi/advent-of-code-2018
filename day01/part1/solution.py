#!/usr/bin/env python3

with open('../input') as f:
    content = [int(n) for n in f.read().split('\n') if n != '']

print(sum(content))
