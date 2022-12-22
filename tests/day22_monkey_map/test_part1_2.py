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

    def test_part2_with_sample(self):
        cube = {9+1j: {'size': 4, -1j: (1+5j, -1), 1: (13+9j, -1), -1: (5+5j, -1j)},
                1+5j: {'size': 4, -1j: (9+1j, -1), -1: (13+9j, 1j), 1j: (9+9j, -1)},
                5+5j: {'size': 4, -1j: (9+1j, 1j), 1j: (9+9j, -1j)},
                9+5j: {'size': 4, 1: (13+9j, 1j)},
                9+9j: {'size': 4, -1: (5+5j, 1j), 1j: (1+5j, -1)},
                13+9j: {'size': 4, -1j: (9+5j, -1j), 1: (9+1j, -1), 1j: (1+5j, -1j)}}
        res = follow_directions(os.path.join(self.dirname, "sample_part1_2.txt"), cube)
        self.assertEqual(5031, res)

    def test_part2_with_input(self):
        cube = {51+1j: {'size': 50, -1j: (1+151j, 1j), -1: (1+101j, -1)},
                101+1j: {'size': 50, -1j: (1+151j, 1), 1: (51+101j, -1), 1j: (51+51j, 1j)},
                51+51j: {'size': 50, -1: (1+101j, -1j), 1: (101+1j, -1j)},
                1+101j: {'size': 50, -1: (51+1j, -1), -1j: (51+51j, 1j)},
                51+101j: {'size': 50, 1: (101+1j, -1), 1j: (1+151j, 1j)},
                1+151j: {'size': 50, -1: (51+1j, -1j), 1: (51+101j, -1j), 1j: (101+1j, 1)}}
        res = follow_directions(os.path.join(self.dirname, "input_part1_2.txt"), cube)
        self.assertEqual(153203, res)


if __name__ == '__main__':
    unittest.main()
