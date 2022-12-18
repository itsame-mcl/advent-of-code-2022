import unittest
import os
from src.day18_boiling_boulders.part1_2 import obsidian_surface, obsidian_exterior_surface


class TestDay18(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = obsidian_surface(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(64, res)

    def test_part1_with_input(self):
        res = obsidian_surface(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(3610, res)

    def test_part2_with_sample(self):
        res = obsidian_exterior_surface(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(58, res)

    def test_part2_with_input(self):
        res = obsidian_exterior_surface(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(2082, res)


if __name__ == '__main__':
    unittest.main()
