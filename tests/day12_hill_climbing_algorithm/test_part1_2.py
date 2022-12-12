import unittest
import os
from src.day12_hill_climbing_algorithm.part1_2 import next_lower_letter, find_shortest_path


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_next_lower_letter(self):
        self.assertEqual('b', next_lower_letter('a'))
        self.assertEqual('m', next_lower_letter('L'))
        self.assertEqual('z', next_lower_letter('z'))
        self.assertEqual('z', next_lower_letter('Z'))

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
