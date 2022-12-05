import unittest
import os
from src.day05_supply_stacks.part1 import top_crates


class TestDay5Part1(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = top_crates(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual("CMZ", res)

    def test_part1_with_input(self):
        res = top_crates(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual("QPJPLMNNR", res)


if __name__ == '__main__':
    unittest.main()
