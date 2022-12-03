import unittest
import os
from src.day02_rock_paper_scissors.enum_RPS import RPS
from src.day02_rock_paper_scissors.part1 import game_engine


class TestDay2Part1(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)
        self.strategy = {'A': RPS.ROCK, 'B': RPS.PAPER, 'C': RPS.SCISSORS,
                         'X': RPS.ROCK, 'Y': RPS.PAPER, 'Z': RPS.SCISSORS}

    def test_part1_with_sample(self):
        res = game_engine(self.strategy, os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(15, res)

    def test_part1_with_input(self):
        res = game_engine(self.strategy, os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(12276, res)


if __name__ == '__main__':
    unittest.main()
