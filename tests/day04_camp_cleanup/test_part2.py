import unittest
import os
from src.day04_camp_cleanup.part2 import sum_overlaps


class TestDay4Part2(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = sum_overlaps(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(4, res)

    def test_part1_with_input(self):
        res = sum_overlaps(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(911, res)


if __name__ == '__main__':
    unittest.main()
