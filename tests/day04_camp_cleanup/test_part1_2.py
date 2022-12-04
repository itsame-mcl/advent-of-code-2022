import unittest
import os
from src.day04_camp_cleanup.part1_2 import sum_triggers


class TestDay4(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = sum_triggers(os.path.join(self.dirname, "sample_part1_2.txt"), 'subsets')
        self.assertEqual(2, res)

    def test_part1_with_input(self):
        res = sum_triggers(os.path.join(self.dirname, "input_part1_2.txt"), 'subsets')
        self.assertEqual(588, res)

    def test_part2_with_sample(self):
        res = sum_triggers(os.path.join(self.dirname, "sample_part1_2.txt"), 'overlaps')
        self.assertEqual(4, res)

    def test_part2_with_input(self):
        res = sum_triggers(os.path.join(self.dirname, "input_part1_2.txt"), 'overlaps')
        self.assertEqual(911, res)

    def test_part1_2_not_implemented_trigger(self):
        self.assertRaises(NotImplementedError, sum_triggers, os.path.join(self.dirname, "input_part1_2.txt"), 'minimum')


if __name__ == '__main__':
    unittest.main()
