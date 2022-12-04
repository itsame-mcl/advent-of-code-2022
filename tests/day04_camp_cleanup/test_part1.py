import unittest
import os
from src.day04_camp_cleanup.part1 import sum_subsets


class TestDay4Part1(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = sum_subsets(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(2, res)

    def test_part1_with_input(self):
        res = sum_subsets(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(588, res)


if __name__ == '__main__':
    unittest.main()
