import unittest
import os
from src.day03_rucksack_reorganization.part1 import sum_duplicates


class TestDay3Part1(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = sum_duplicates(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(157, res)

    def test_part1_with_input(self):
        res = sum_duplicates(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(7716, res)


if __name__ == '__main__':
    unittest.main()
