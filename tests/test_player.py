import unittest
from collections import namedtuple
from typing import List
from advent_of_code import Player, Vector2D


class TestPlayer(unittest.TestCase):
    def test_movement(self):
        Case = namedtuple('Case', 'location facing steps expected_location expected_facing')

        cases: List[Case] = [
            Case(Vector2D(0, 0), Vector2D(1, 0), 5, Vector2D(5, 0), Vector2D(1, 0)),
            Case(Vector2D(0, 0), Vector2D(-1, 0), 5, Vector2D(-5, 0), Vector2D(-1, 0)),
            Case(Vector2D(5, 2), Vector2D(3, 1), 3, Vector2D(14, 5), Vector2D(3, 1))
        ]

        for case in cases:
            player = Player(case.location, case.facing)
            player.step(case.steps)
            self.assertEqual(player.location, case.expected_location,
                             f'wanted: {case.expected_location}, got: {player.location}')
            self.assertEqual(player.velocity, case.expected_facing,
                             f'wanted: {case.expected_facing}, got: {player.velocity}')
            self.assertEqual(player.number_of_steps(), case.steps,
                             f'wanted: {case.steps}, got: {player.number_of_steps()}')
            self.assertEqual(player.number_of_turns(), 0,
                             f'wanted: 0, got: {player.number_of_turns()}')

    def test_turn(self):
        Case = namedtuple('Case', 'location facing steps expected_location expected_facing')

        cases: List[Case] = [
            Case(Vector2D(0, 0), Vector2D(1, 0), 5, Vector2D(1, 0), Vector2D(0, 1)),
            Case(Vector2D(0, 0), Vector2D(-1, 0), 5, Vector2D(-1, 0), Vector2D(0, -1)),
            Case(Vector2D(5, 2), Vector2D(3, 1), 3, Vector2D(4, 5), Vector2D(1, -3))
        ]

        for case in cases:
            player = Player(case.location, case.facing)
            for _ in range(0, case.steps):
                player.step()
                player.turn(90)
            self.assertEqual(player.location, case.expected_location,
                             f'wanted: {case.expected_location}, got: {player.location}')
            self.assertEqual(player.velocity, case.expected_facing,
                             f'wanted: {case.expected_facing}, got: {player.velocity}')
            self.assertEqual(player.number_of_steps(), case.steps,
                             f'wanted: {case.steps}, got: {player.number_of_steps()}')
            self.assertEqual(player.number_of_turns(), case.steps,
                             f'wanted: {case.steps}, got: {player.number_of_turns()}')

    def test_comparison(self):
        self.assertTrue(
            Player(Vector2D(1, 0), Vector2D(1, 0)) < Player(Vector2D(2, 0), Vector2D(1, 0)))
        self.assertFalse(
            Player(Vector2D(1, 5), Vector2D(1, 0)) < Player(Vector2D(2, 0), Vector2D(1, 0)))
        self.assertTrue(
            Player(Vector2D(1, 3), Vector2D(1, 0)) < Player(Vector2D(3, 6), Vector2D(1, 0)))

    def test_string_format(self):
        p = Player(Vector2D(1, 0), Vector2D(-1, 0))
        obj_id = id(p)

        self.assertEqual(str(p), f'{obj_id} <1x0> <-1x0>')
