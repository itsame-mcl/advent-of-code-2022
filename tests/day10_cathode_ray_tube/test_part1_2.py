import unittest
import os
from src.day10_cathode_ray_tube.part1_2 import compute_signal_strength, draw_crt


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_part1_with_sample(self):
        res = compute_signal_strength(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(13140, res)

    def test_part1_with_input(self):
        res = compute_signal_strength(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(14360, res)

    def test_part2_with_sample(self):
        res = draw_crt(os.path.join(self.dirname, "sample_part1_2.txt"))
        expected ="##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######.....\n"
        self.assertEqual(expected, res)

    def test_part2_with_input(self):
        res = draw_crt(os.path.join(self.dirname, "input_part1_2.txt"))
        expected = "###...##..#..#..##..####.###..####.####.\n#..#.#..#.#.#..#..#.#....#..#.#.......#.\n###..#....##...#..#.###..#..#.###....#..\n#..#.#.##.#.#..####.#....###..#.....#...\n#..#.#..#.#.#..#..#.#....#.#..#....#....\n###...###.#..#.#..#.####.#..#.####.####.\n"
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
