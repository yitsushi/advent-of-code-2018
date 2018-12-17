import unittest
from advent_of_code import SumTable, Vector2D
from random import randint

class TestSumTable(unittest.TestCase):
    def test_area(self):
        test_data = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]
        table = SumTable(9, 9)
        for y in range(0, len(test_data)):
            table.set_row(y, test_data[y])

        table.calculate()

        # First row
        expected = sum(test_data[0])
        self.assertEqual(table.area(Vector2D(0, 0), Vector2D(8, 0)), expected)

        # First Column
        expected = sum([row[0] for row in test_data])
        self.assertEqual(table.area(Vector2D(0, 0), Vector2D(0, 8)), expected)

        # Somewhere in the middle
        x1, y1 = randint(0, 3), randint(0, 3)
        x2, y2 = randint(5, 8), randint(5, 8)

        expected = sum([v for row in test_data[y1:y2+1] for v in row[x1:x2+1]])
        self.assertEqual(table.area(Vector2D(x1, y1), Vector2D(x2, y2)), expected)

    def test_array(self):
        test_data = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]
        test_sum_data = [
            [1, 3, 6, 10, 15, 21, 28, 36, 45],
            [3, 8, 15, 24, 35, 48, 63, 80, 90],
            [6, 15, 27, 42, 60, 81, 105, 123, 135],
            [10, 24, 42, 64, 90, 120, 145, 165, 180],
            [15, 35, 60, 90, 125, 156, 183, 206, 225],
            [21, 48, 81, 120, 156, 189, 219, 246, 270],
            [28, 63, 105, 145, 183, 219, 253, 285, 315],
            [36, 80, 123, 165, 206, 246, 285, 323, 360],
            [45, 90, 135, 180, 225, 270, 315, 360, 405]
        ]
        table = SumTable(9, 9)
        for y in range(0, len(test_data)):
            table.set_row(y, test_data[y])

        table.calculate()

        print(table.sum_array())

        self.assertListEqual(table.array(), test_data)
        self.assertListEqual(table.sum_array(), test_sum_data)
