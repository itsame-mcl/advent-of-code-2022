import unittest
import os
from src.day14_regolith_reservoir.part1_2 import saturate_with_resting_sand


class TestDay14(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = saturate_with_resting_sand(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(24, res)

    def test_part1_with_input(self):
        res = saturate_with_resting_sand(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(1406, res)

    def test_part2_with_sample(self):
        res = saturate_with_resting_sand(os.path.join(self.dirname, "sample_part1_2.txt"), True)
        self.assertEqual(93, res)

    def test_part2_with_input(self):
        res = saturate_with_resting_sand(os.path.join(self.dirname, "input_part1_2.txt"), True)
        self.assertEqual(20870, res)


if __name__ == '__main__':
    unittest.main()
