import unittest
import os
from collections import namedtuple
from advent_of_code import BaseSolution


class TestBaseSolution(unittest.TestCase):
    def test_parse(self):
        s = 'Sammy <13x32> HP:200 AP:8'
        solution = BaseSolution('', lambda v: v, [])
        name, x, y, hp, ap = solution.parse(s,
                                            r'([A-Za-z]+) <([0-9-]+)x([0-9-]+)> HP:([0-9]+) AP:([0-9]+)',
                                            (str, int, int, int, int))

        self.assertEqual(name, 'Sammy')
        self.assertEqual(x, 13)
        self.assertEqual(y, 32)
        self.assertEqual(hp, 200)
        self.assertEqual(ap, 8)

        s = 'No more games!'
        with self.assertRaises(SystemExit):
            solution.parse(s,
                           r'([A-Za-z]+) <([0-9-]+)x([0-9-]+)> HP:([0-9]+) AP:([0-9]+)',
                           (str, int, int, int, int))

    def test_exit_on_invalid_arguments(self):
        solution = BaseSolution('', lambda x: x, [])

        with self.assertRaises(SystemExit):
            solution.parameters((int,), ('Just a number',), (None, ))

    def test_exit_on_invalid_function_call(self):
        solution = BaseSolution('', lambda x: x, [])

        with self.assertRaises(SystemExit):
            solution.parameters((int, str), ('Just a number',), (None,))

    def test_workflow(self):
        class MySolution(BaseSolution):
            unit: unittest.TestCase

            def setup(self):
                super().setup()
                # Read parameters
                (input_file, players, limit) = self.parameters((str, int, int),
                                                               ('Input File', 'Number of Players', 'Range Limit'),
                                                               (None, 10, 5_000))

                self.unit.assertEqual(input_file, 'test_base_solution_1')
                self.unit.assertEqual(players, 8)
                self.unit.assertEqual(limit, 5_000)

                # Read and parse input file
                NPC = namedtuple('NPC', 'name x y hp ap')
                npc_list = []
                for line in self.read_input(input_file):
                    npc_list.append(
                        NPC(*solution.parse(line,
                                            r'([A-Za-z]+) <([0-9-]+)x([0-9-]+)> HP:([0-9]+) AP:([0-9]+)',
                                            (str, int, int, int, int))))

                self.unit.assertGreater(len(npc_list), 0)

            def part1(self):
                super().part1()

            def part2(self):
                super().part2()

        parameters = ['test_base_solution_1', 8]
        fixture_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
        solution = MySolution(fixture_directory, lambda x: x, parameters)
        solution.unit = self
        solution.setup()

        with self.assertRaises(NotImplementedError):
            solution.part1()
        with self.assertRaises(NotImplementedError):
            solution.part2()
