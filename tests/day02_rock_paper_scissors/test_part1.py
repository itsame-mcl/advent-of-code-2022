import unittest
from src.day02_rock_paper_scissors.enum_RPS import RPS
from src.day02_rock_paper_scissors.part1 import game_engine


class TestDay2Part1(unittest.TestCase):
    def test_part1_with_sample(self):
        strategy = {'A': RPS.ROCK, 'B': RPS.PAPER, 'C': RPS.SCISSORS,
                    'X': RPS.ROCK, 'Y': RPS.PAPER, 'Z': RPS.SCISSORS}
        res = game_engine(strategy, "day02_rock_paper_scissors/sample_part1_2.txt")
        self.assertEqual(15, res)

    def test_part1_with_input(self):
        strategy = {'A': RPS.ROCK, 'B': RPS.PAPER, 'C': RPS.SCISSORS,
                    'X': RPS.ROCK, 'Y': RPS.PAPER, 'Z': RPS.SCISSORS}
        res = game_engine(strategy, "day02_rock_paper_scissors/input_part1_2.txt")
        self.assertEqual(12276, res)


if __name__ == '__main__':
    unittest.main()
