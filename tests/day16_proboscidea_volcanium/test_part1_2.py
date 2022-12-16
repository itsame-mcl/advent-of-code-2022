import unittest
import os
from src.day16_proboscidea_volcanium.part1_2 import release_most_pressure


class TestDay16(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = release_most_pressure(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(1651, res)

    def test_part1_with_input(self):
        res = release_most_pressure(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(2077, res)

    def test_part2_with_sample(self):
        res = release_most_pressure(os.path.join(self.dirname, "sample_part1_2.txt"), True)
        self.assertEqual(1707, res)

    @unittest.skip("Too long to compute (~ 1 mn)")
    def test_part2_with_input(self):
        res = release_most_pressure(os.path.join(self.dirname, "input_part1_2.txt"), True)
        self.assertEqual(2741, res)


if __name__ == '__main__':
    unittest.main()
