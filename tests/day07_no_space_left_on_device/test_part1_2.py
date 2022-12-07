import unittest
import os
from src.day07_no_space_left_on_device.part1_2 import find_little_dirs, free_space


class TestDay7(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = find_little_dirs(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(95437, res)

    def test_part1_with_input(self):
        res = find_little_dirs(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(1792222, res)

    def test_part2_with_sample(self):
        res = free_space(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(24933642, res)

    def test_part2_with_input(self):
        res = free_space(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(1112963, res)


if __name__ == '__main__':
    unittest.main()
