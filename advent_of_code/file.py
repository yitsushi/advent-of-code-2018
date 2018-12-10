#!/usr/bin/env python3

import sys, re
from typing import Tuple, List, Pattern

def parameters(number_of_parameters:int = 1, parameter_types:Tuple = (str,)):
    if len(sys.argv) <= number_of_parameters:
        print(f"Required parameters {parameter_types}.")
        sys.exit(-1)

    params = list([t(v) for t, v in zip(parameter_types, sys.argv[1:number_of_parameters+1])])

    if len(params) == 1:
        return params[0]

    return params

def read_input(path:str, separator:str = '\n', ignore:List = ['']):
    with open(path) as f:
        content = f.read().split(separator)
        for section in content:
            if section not in ignore:
                yield section

def parse(content:str, pattern:Pattern, types:Tuple):
    try:
        return list([t(v) for t,v in zip(types, re.search(pattern, content).groups())])
    except Exception as e:
        print(f'!!! Parse error {e}')
        print(f'Content: {content}')
        print(f'Pattern: {pattern}')
        sys.exit(-1)

if __name__ == '__main__':
    sys.argv = [sys.argv[0]]
    sys.argv.append('../day01/input')
    input_file = parameters(1, (str,))
    try:
        numbers = [int(line) for line in read_input(input_file)]
        print('Sample:')
        print(numbers[:5])
    except Exception as e:
        print(f'!!! Error happend with "int" array read :: {e}')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('../day02/input')
    input_file = parameters(1, (str,))
    try:
        codes = [line for line in read_input(input_file)]
        print('Sample:')
        print(codes[:5])
    except:
        print('!!! Error happend with "string" array read')
        sys.exit(-1)

    # TODO: parse
    sys.argv = [sys.argv[0]]
    sys.argv.append('../day03/input')
    input_file = parameters(1, (str,))
    pattern = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
    try:
        claims = [parse(line, pattern, (int, int, int, int, int)) for line in read_input(input_file)]
        print('Sample:')
        print(claims[:5])
    except:
        print('!!! Error happend with parsed content')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('../day08/input')
    input_file = parameters(1, (str,))
    try:
        numbers = [int(line) for line in read_input(input_file, separator=' ')]
        print('Sample:')
        print(numbers[:5])
    except:
        print('!!! Error happend with "int" array read space separated')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('../day08/input')
    sys.argv.append('1000')
    sys.argv.append('2000')
    input_file, width, height = parameters(3, (str, int, int))

    print("{:s} | {:d}x{:d}".format(input_file, width, height))

