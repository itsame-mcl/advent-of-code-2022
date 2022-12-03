import unittest
from src.day03_rucksack_reorganization.part2 import sum_badges


class TestDay3Part2(unittest.TestCase):
    def test_part2_with_sample(self):
        res = sum_badges("day03_rucksack_reorganization/sample_part1_2.txt")
        self.assertEqual(70, res)

    def test_part2_with_input(self):
        res = sum_badges("day03_rucksack_reorganization/input_part1_2.txt")
        self.assertEqual(2973, res)


if __name__ == '__main__':
    unittest.main()
