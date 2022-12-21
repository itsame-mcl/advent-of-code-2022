import unittest
import os
from src.day21_monkey_math.part1_2 import solve_with_z3


class TestDay21(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_with_invalid_sample(self):
        self.assertRaises(ValueError, solve_with_z3, os.path.join(self.dirname, "invalid_sample_part1_2.txt"), 'root')

    def test_part1_with_sample(self):
        res = solve_with_z3(os.path.join(self.dirname, "sample_part1_2.txt"), 'root')
        self.assertEqual(152, res)

    def test_part1_with_input(self):
        res = solve_with_z3(os.path.join(self.dirname, "input_part1_2.txt"), 'root')
        self.assertEqual(331319379445180, res)

    def test_part2_with_sample(self):
        res = solve_with_z3(os.path.join(self.dirname, "sample_part1_2.txt"), 'humn')
        self.assertEqual(301, res)

    def test_part2_with_input(self):
        res = solve_with_z3(os.path.join(self.dirname, "input_part1_2.txt"), 'humn')
        self.assertEqual(3715799488132, res)


if __name__ == '__main__':
    unittest.main()
