import unittest
import os
from src.day21_monkey_math.part1_2 import run_computation, solve_root_equality


class TestDay21(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = run_computation(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(152, res)

    def test_part1_with_input(self):
        res = run_computation(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(331319379445180, res)

    def test_part2_with_sample(self):
        res = solve_root_equality(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(301, res)

    def test_part2_with_input(self):
        res = solve_root_equality(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(3715799488132, res)


if __name__ == '__main__':
    unittest.main()
