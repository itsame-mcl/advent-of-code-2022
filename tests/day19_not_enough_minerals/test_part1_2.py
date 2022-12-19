import unittest
import os
from src.day19_not_enough_minerals.part1_2 import maximize_for_all_blueprints


class TestDay19(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = maximize_for_all_blueprints(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(33, res)

    def test_part1_with_input(self):
        res = maximize_for_all_blueprints(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(817, res)

    @unittest.skip("Quite long to compute (~ 45 sec)")
    def test_part2_with_sample(self):
        res = maximize_for_all_blueprints(os.path.join(self.dirname, "sample_part1_2.txt"), 3, 32)
        self.assertEqual(3472, res)

    def test_part2_with_input(self):
        res = maximize_for_all_blueprints(os.path.join(self.dirname, "input_part1_2.txt"), 3, 32)
        self.assertEqual(4216, res)


if __name__ == '__main__':
    unittest.main()
