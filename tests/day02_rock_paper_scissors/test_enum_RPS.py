import unittest
from src.day02_rock_paper_scissors.enum_RPS import RPS
from parameterized import parameterized_class


@parameterized_class(('first', 'second', 'expected_lt', 'expected_eq', 'expected_gt'), [
    (RPS.ROCK, RPS.ROCK, False, True, False),
    (RPS.ROCK, RPS.PAPER, True, False, False),
    (RPS.ROCK, RPS.SCISSORS, False, False, True),
    (RPS.PAPER, RPS.ROCK, False, False, True),
    (RPS.PAPER, RPS.PAPER, False, True, False),
    (RPS.PAPER, RPS.SCISSORS, True, False, False),
    (RPS.SCISSORS, RPS.ROCK, True, False, False),
    (RPS.SCISSORS, RPS.PAPER, False, False, True),
    (RPS.SCISSORS, RPS.SCISSORS, False, True, False)
])
class TestEnumChoice(unittest.TestCase):
    def test_lt(self):
        self.assertEqual(self.expected_lt, self.first < self.second)

    def test_eq(self):
        self.assertEqual(self.expected_eq, self.first == self.second)

    def test_gt(self):
        self.assertEqual(self.expected_gt, self.first > self.second)


if __name__ == '__main__':
    unittest.main()
