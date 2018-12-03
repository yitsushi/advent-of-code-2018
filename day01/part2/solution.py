#!/usr/bin/env python3

with open('../input') as f:
    content = [int(n) for n in f.read().split('\n') if n != '']

frequencies = {}
summary = 0
inProgress = True

while inProgress:
    for n in content:
        summary += n
        if str(summary) in frequencies:
            inProgress = False
            break
        frequencies[str(summary)] = True

print(summary)
