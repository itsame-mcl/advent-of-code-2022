import unittest
import os
from src.day20_grove_positioning_system.part1_2 import compute_grove_coordinates


class TestDay20(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = compute_grove_coordinates(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(3, res)

    def test_part1_with_input(self):
        res = compute_grove_coordinates(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(16533, res)

    def test_part2_with_sample(self):
        res = compute_grove_coordinates(os.path.join(self.dirname, "sample_part1_2.txt"), 811589153, 10)
        self.assertEqual(1623178306, res)

    def test_part2_with_input(self):
        res = compute_grove_coordinates(os.path.join(self.dirname, "input_part1_2.txt"), 811589153, 10)
        self.assertEqual(4789999181006, res)


if __name__ == '__main__':
    unittest.main()
