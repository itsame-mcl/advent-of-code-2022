import unittest
from src.day03_rucksack_reorganization.part1 import sum_duplicates


class TestDay3Part1(unittest.TestCase):
    def test_part1_with_sample(self):
        res = sum_duplicates("day03_rucksack_reorganization/sample_part1_2.txt")
        self.assertEqual(157, res)

    def test_part1_with_input(self):
        res = sum_duplicates("day03_rucksack_reorganization/input_part1_2.txt")
        self.assertEqual(7716, res)


if __name__ == '__main__':
    unittest.main()
