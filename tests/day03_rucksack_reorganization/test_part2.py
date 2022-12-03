import unittest
import os
from src.day03_rucksack_reorganization.part2 import sum_badges


class TestDay3Part2(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part2_with_sample(self):
        res = sum_badges(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(70, res)

    def test_part2_with_input(self):
        res = sum_badges(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(2973, res)


if __name__ == '__main__':
    unittest.main()
