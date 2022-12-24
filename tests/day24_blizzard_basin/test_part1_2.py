import unittest
import os
from src.day24_blizzard_basin.part1_2 import find_shortest_path


class TestDay24(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = find_shortest_path(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(18, res)

    @unittest.skip("Quite long to compute (~ 1 min)")
    def test_part1_with_input(self):
        res = find_shortest_path(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(230, res)

    def test_part2_with_sample(self):
        res = find_shortest_path(os.path.join(self.dirname, "sample_part1_2.txt"), True)
        self.assertEqual(54, res)

    @unittest.skip("Quite long to compute (~ 1 min)")
    def test_part2_with_input(self):
        res = find_shortest_path(os.path.join(self.dirname, "input_part1_2.txt"), True)
        self.assertEqual(713, res)


if __name__ == '__main__':
    unittest.main()
