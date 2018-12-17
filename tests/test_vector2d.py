import unittest
from collections import namedtuple
from advent_of_code import Vector2D


class TestVector2D(unittest.TestCase):
    def test_addition(self):
        Case = namedtuple('Case', 'a b c')
        cases = [
            Case(Vector2D(5, 6), Vector2D(2, 5), Vector2D(7, 11)),
            Case(Vector2D(-5, 6), Vector2D(2, 5), Vector2D(-3, 11)),
            Case(Vector2D(0, 0), Vector2D(1, 1), Vector2D(1, 1)),
            Case(Vector2D(-5, -6), Vector2D(2, 5), Vector2D(-3, -1)),
            Case(Vector2D(-5, -6), Vector2D(-2, 5), Vector2D(-7, -1)),
            Case(Vector2D(-5, -6), Vector2D(-2, -5), Vector2D(-7, -11)),
        ]

        for case in cases:
            result = case.a + case.b
            self.assertEqual(
                result,
                case.c,
                f'<{case.a}> + <{case.b}> should be <{case.c}>, but it is <{result}>')

    def test_subtraction(self):
        Case = namedtuple('Case', 'a b c')
        cases = [
            Case(Vector2D(5, 6), Vector2D(2, 5), Vector2D(3, 1)),
            Case(Vector2D(-5, 6), Vector2D(2, 5), Vector2D(-7, 1)),
            Case(Vector2D(0, 0), Vector2D(1, 1), Vector2D(-1, -1)),
            Case(Vector2D(-5, -6), Vector2D(2, 5), Vector2D(-7, -11)),
            Case(Vector2D(-5, -6), Vector2D(-2, 5), Vector2D(-3, -11)),
            Case(Vector2D(-5, -6), Vector2D(-2, -5), Vector2D(-3, -1)),
        ]

        for case in cases:
            result = case.a - case.b
            self.assertEqual(
                result,
                case.c,
                f'<{case.a}> - <{case.b}> should be <{case.c}>, but it is <{result}>')

    def test_rotation(self):
        Case = namedtuple('Case', 'vector degrees expected')
        cases = [
            Case(Vector2D(5, 6), 90, Vector2D(-6, 5)),
            Case(Vector2D(5, 6), -90, Vector2D(6, -5)),
            Case(Vector2D(5, 6), 180, Vector2D(-5, -6)),
            Case(Vector2D(5, 6), -180, Vector2D(-5, -6)),
            Case(Vector2D(5, 6), 45, Vector2D(-1, 8)),
            Case(Vector2D(5, 6), 360, Vector2D(5, 6)),
        ]

        for case in cases:
            case.vector.rotate(case.degrees)
            self.assertEqual(case.vector, case.expected, f'wanted: {case.expected}, got: {case.vector}')

    def test_manhattan(self):
        Case = namedtuple('Case', 'vector expected')
        cases = [
            Case(Vector2D(5, 6), 11),
            Case(Vector2D(5, -6), 11),
            Case(Vector2D(-5, 6), 11),
            Case(Vector2D(-5, -6), 11)
        ]

        for case in cases:
            value = case.vector.manhattan()
            self.assertEqual(value, case.expected, f'wanted: {case.expected}, got: {value}')

    def test_comparison(self):
        Case = namedtuple('Case', 'a b method')
        cases = [
            Case(Vector2D(5, 6), Vector2D(1, 4), self.assertFalse),
            Case(Vector2D(5, -6), Vector2D(6, 1), self.assertTrue),
            Case(Vector2D(-5, 6), Vector2D(1, 6), self.assertTrue),
            Case(Vector2D(-5, -6), Vector2D(-8, -6), self.assertFalse)
        ]

        for case in cases:
            case.method(case.a < case.b)
