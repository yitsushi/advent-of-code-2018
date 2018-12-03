#!/usr/bin/env python3

import regex, sys

with open('../input') as f:
    idList = [id for id in f.read().split('\n') if id != '']

for index in range(0, len(idList)):
    current = idList[index]
    for id in idList[index+1:]:
        result = regex.search(r'(%s){e<2}' % (id), current)
        if result is not None:
            i = result.fuzzy_changes[0][0]
            print(current[:i] + current[i+1:])
            sys.exit(0)

