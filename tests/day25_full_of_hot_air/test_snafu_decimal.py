import unittest
import os
from src.day25_full_of_hot_air.snafu_decimal import sum_snafu, decimal_to_snafu


class TestDay25(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_decimal_to_snafu(self):
        self.assertEqual('1', decimal_to_snafu(1))
        self.assertEqual('2', decimal_to_snafu(2))
        self.assertEqual('1=', decimal_to_snafu(3))
        self.assertEqual('1-', decimal_to_snafu(4))
        self.assertEqual('10', decimal_to_snafu(5))
        self.assertEqual('11', decimal_to_snafu(6))
        self.assertEqual('12', decimal_to_snafu(7))
        self.assertEqual('2=', decimal_to_snafu(8))
        self.assertEqual('2-', decimal_to_snafu(9))
        self.assertEqual('20', decimal_to_snafu(10))
        self.assertEqual('1=0', decimal_to_snafu(15))
        self.assertEqual('1-0', decimal_to_snafu(20))
        self.assertEqual('10-', decimal_to_snafu(24))
        self.assertEqual('1=11-2', decimal_to_snafu(2022))
        self.assertEqual('1-0---0', decimal_to_snafu(12345))
        self.assertEqual('1121-1110-1=0', decimal_to_snafu(314159265))

    def test_with_sample(self):
        res = sum_snafu(os.path.join(self.dirname, "sample.txt"))
        self.assertEqual('2=-1=0', res)

    def test_with_input(self):
        res = sum_snafu(os.path.join(self.dirname, "input.txt"))
        self.assertEqual('2-2=21=0021=-02-1=-0', res)


if __name__ == '__main__':
    unittest.main()
