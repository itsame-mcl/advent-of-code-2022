import unittest
import os
from src.day01_calorie_counting.part1_2 import max_calories


class TestDay1(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = max_calories(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(24000, res)

    def test_part1_with_input(self):
        res = max_calories(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(69693, res)

    def test_part2_with_sample(self):
        res = max_calories(os.path.join(self.dirname, "sample_part1_2.txt"), 3)
        self.assertEqual(45000, res)

    def test_part2_with_input(self):
        res = max_calories(os.path.join(self.dirname, "input_part1_2.txt"), 3)
        self.assertEqual(200945, res)


if __name__ == '__main__':
    unittest.main()
