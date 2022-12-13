import unittest
import os
from src.day13_distress_signal.part1_2 import check_signal, find_decoder_key


class TestDay13(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = check_signal(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(13, res)

    def test_part1_with_input(self):
        res = check_signal(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(6484, res)

    def test_part2_with_sample(self):
        res = find_decoder_key(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(140, res)

    def test_part2_with_input(self):
        res = find_decoder_key(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(19305, res)


if __name__ == '__main__':
    unittest.main()
