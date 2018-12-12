#!/usr/bin/env python3

import sys
import re
from typing import Tuple, List, Any, Generator


def parameters(parameter_types: Tuple = (str,),
               names: Tuple = ("Input File", ),
               default: Tuple = (None, )) -> List[Any]:
    try:
        if len(default) != len(parameter_types) or len(names) != len(parameter_types):
            print("Wrong function call: ({}, {}, {})".format(parameter_types, names, default))
            sys.exit(-1)

        number_of_nones = default.count(None)
        if len(sys.argv) <= number_of_nones:
            raise Exception("Wrong number of arguments!")

        for i in range(len(sys.argv)-1, len(parameter_types)):
            sys.argv.append(default[i])

        return list([t(v) for t, v in zip(parameter_types, sys.argv[1:len(parameter_types)+1])])

    except Exception as exp:
        print(f" !!! {exp}")
        max_name_length = max([len(v) for v in names]) + 3
        template = f'%{max_name_length}s %s = %s'
        pairs = zip(names, parameter_types, [v or "(required)" for v in default])
        ktv = [template % (k, t, v) for k, t, v in pairs]
        print("Required parameters:\n\t{}".format('\n\t'.join(ktv)))
        sys.exit(-1)


def read_input(path: str,
               separator: str = '\n',
               ignore: List = None) -> Generator:
    if ignore is None:
        ignore = ['']
    with open(path) as f:
        content = f.read().split(separator)
        for section in content:
            if section not in ignore:
                yield section


def parse(content: str,
          search_pattern: str,
          types: Tuple) -> List[Any]:
    try:
        search_result = re.search(re.compile(search_pattern), content)
        if search_result is None:
            raise Exception('No match!')
        return list([t(v) for t, v in zip(types, search_result.groups())])
    except Exception as exp:
        print(f'!!! Parse error {exp}')
        print(f'Content: {content}')
        print(f'Pattern: {search_pattern}')
        sys.exit(-1)


if __name__ == '__main__':
    sys.argv = [sys.argv[0]]
    sys.argv.append('day01/input')
    (input_file,) = parameters()
    try:
        numbers = [int(line) for line in read_input(input_file)]
        print('Sample:')
        print(numbers[:5])
    except Exception as e:
        print(f'!!! Error happend with "int" array read :: {e}')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('day02/input')
    (input_file, ) = parameters()
    try:
        codes = [line for line in read_input(input_file)]
        print('Sample:')
        print(codes[:5])
    except:
        print('!!! Error happend with "string" array read')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('day03/input')
    (input_file, ) = parameters()
    pattern = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
    try:
        claims = [parse(line, pattern, (int, int, int, int, int))
                  for line in read_input(input_file)]
        print('Sample:')
        print(claims[:5])
    except:
        print('!!! Error happend with parsed content')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('day08/input')
    (input_file, ) = parameters()
    try:
        numbers = [int(line) for line in read_input(input_file, separator=' ')]
        print('Sample:')
        print(numbers[:5])
    except:
        print('!!! Error happend with "int" array read space separated')
        sys.exit(-1)

    sys.argv = [sys.argv[0]]
    sys.argv.append('day08/input')
    sys.argv.append('1000')
    sys.argv.append('2000')
    (input_file, width, height) = parameters((str, int, int),
                                             ('Input File', 'Width', 'Height'),
                                             (None, 1000, 1000))

    print("{:s} | {:d}x{:d}".format(input_file, width, height))

