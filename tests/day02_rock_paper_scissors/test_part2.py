import unittest
import os
from src.day02_rock_paper_scissors.part2 import game_engine


class TestDay2Part2(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part2_with_sample(self):
        res = game_engine(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(12, res)

    def test_part2_with_input(self):
        res = game_engine(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(9975, res)

    def test_part2_fail(self):
        self.assertRaises(ValueError, game_engine, os.path.join(self.dirname, "fail_part2.txt"))


if __name__ == '__main__':
    unittest.main()
