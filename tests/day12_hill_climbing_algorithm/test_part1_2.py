import unittest
import os
from src.day12_hill_climbing_algorithm.part1_2 import find_shortest_path


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = find_shortest_path(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(31, res)

    def test_part1_with_input(self):
        res = find_shortest_path(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(370, res)

    def test_part2_with_sample(self):
        res = find_shortest_path(os.path.join(self.dirname, "sample_part1_2.txt"), True)
        self.assertEqual(29, res)

    def test_part2_with_input(self):
        res = find_shortest_path(os.path.join(self.dirname, "input_part1_2.txt"), True)
        self.assertEqual(363, res)


if __name__ == '__main__':
    unittest.main()
