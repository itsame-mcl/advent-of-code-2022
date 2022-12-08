import unittest
import os
from src.day08_treetop_tree_house.part1_2 import number_of_visible_trees, best_scenic_score


class TestDay8(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = number_of_visible_trees(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(21, res)

    def test_part1_with_input(self):
        res = number_of_visible_trees(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(1843, res)

    def test_part2_with_sample(self):
        res = best_scenic_score(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(8, res)

    def test_part2_with_input(self):
        res = best_scenic_score(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(180000, res)


if __name__ == '__main__':
    unittest.main()
