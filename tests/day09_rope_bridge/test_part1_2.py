import unittest
import os
from src.day09_rope_bridge.part1_2 import visited_positions


class TestDay9(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_with_invalid_sample(self):
        self.assertRaises(ValueError, visited_positions, os.path.join(self.dirname, "invalid_sample.txt"), 2)

    def test_part1_with_sample(self):
        res = visited_positions(os.path.join(self.dirname, "sample_part1.txt"), 2)
        self.assertEqual(13, res)

    def test_part1_with_input(self):
        res = visited_positions(os.path.join(self.dirname, "input_part1_2.txt"), 2)
        self.assertEqual(6642, res)

    def test_part2_with_sample(self):
        res = visited_positions(os.path.join(self.dirname, "sample_part2.txt"), 10)
        self.assertEqual(36, res)

    def test_part2_with_input(self):
        res = visited_positions(os.path.join(self.dirname, "input_part1_2.txt"), 10)
        self.assertEqual(2765, res)


if __name__ == '__main__':
    unittest.main()
