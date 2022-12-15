import unittest
import os
from src.day15_beacon_exclusion_zone.part1_2 import compute_single_row_exclusion, find_distress_beacon


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = compute_single_row_exclusion(os.path.join(self.dirname, "sample_part1_2.txt"), 10)
        self.assertEqual(26, res)

    def test_part1_with_input(self):
        res = compute_single_row_exclusion(os.path.join(self.dirname, "input_part1_2.txt"), 2000000)
        self.assertEqual(4793062, res)

    def test_part2_with_sample(self):
        res = find_distress_beacon(os.path.join(self.dirname, "sample_part1_2.txt"), 20)
        self.assertEqual(56000011, res)

    def test_part2_with_sample_not_found(self):
        res = find_distress_beacon(os.path.join(self.dirname, "sample_part1_2.txt"), 10)
        self.assertEqual(None, res)

    @unittest.skip("Too long to compute ~= 2 mn")
    def test_part2_with_input(self):
        res = find_distress_beacon(os.path.join(self.dirname, "input_part1_2.txt"), 4000000)
        self.assertEqual(10826395253551, res)


if __name__ == '__main__':
    unittest.main()
