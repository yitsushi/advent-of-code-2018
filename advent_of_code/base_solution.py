import sys
import os
import re
from typing import Tuple, List, Any, Generator


class BaseSolution(object):
    __parameters: List[str]
    __base: str
    report_time: callable

    def __init__(self, _base: str, report_time: callable, _parameters: List[str]):
        self.__base = _base
        self.report_time = report_time
        self.__parameters = _parameters

    def setup(self):
        pass

    def part1(self):
        raise NotImplementedError('Solution is not implemented yet!')

    def part2(self):
        raise NotImplementedError('Solution is not implemented yet!')

    def parameters(self, parameter_types: Tuple = (str,),
                   names: Tuple = ("Input File", ),
                   default: Tuple = ('input', )) -> List[Any]:
        try:
            if len(default) != len(parameter_types) or len(names) != len(parameter_types):
                print("Wrong function call: ({}, {}, {})".format(parameter_types, names, default))
                sys.exit(-1)

            number_of_nones = default.count(None)
            if len(self.__parameters) < number_of_nones:
                raise Exception("Wrong number of arguments!")

            for i in range(len(self.__parameters), len(parameter_types)):
                self.__parameters.append(default[i])

            return list([t(v) for t, v in zip(parameter_types, self.__parameters[0:len(parameter_types)])])

        except Exception as exp:
            print(f" !!! {exp}")
            max_name_length = max([len(v) for v in names]) + 3
            template = f'%{max_name_length}s %s = %s'
            pairs = zip(names, parameter_types, [v or "(required)" for v in default])
            ktv = [template % (k, t, v) for k, t, v in pairs]
            print("Required parameters:\n\t{}".format('\n\t'.join(ktv)))
            sys.exit(-1)

    def read_input(self, path: str,
                   separator: str = '\n',
                   ignore: List = None) -> Generator[str, None, None]:

        if ignore is None:
            ignore = ['']

        path = os.path.join(self.__base, path)

        with open(path) as f:
            content: List[str] = f.read().split(separator)
            for section in content:
                if section not in ignore:
                    yield section

    @staticmethod
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
