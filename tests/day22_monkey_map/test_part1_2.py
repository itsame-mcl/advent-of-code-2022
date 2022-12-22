import unittest
import os
from src.day22_monkey_map.part1_2 import follow_directions


class TestDay22(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = follow_directions(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(6032, res)

    def test_part1_with_input(self):
        res = follow_directions(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(149138, res)


if __name__ == '__main__':
    unittest.main()
