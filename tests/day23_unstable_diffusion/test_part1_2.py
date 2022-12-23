import unittest
import os
from src.day23_unstable_diffusion.spreading_elves import SpreadingElves


class TestDay22(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_str_controller(self):
        controller = SpreadingElves(os.path.join(self.dirname, "small_sample_part1_2.txt"))
        self.assertEqual("##\n#.\n..\n##\n", str(controller))

    def test_part1_with_sample(self):
        controller = SpreadingElves(os.path.join(self.dirname, "sample_part1_2.txt"))
        controller.do_round(10)
        res = controller.compute_empty_tiles()
        self.assertEqual(110, res)

    def test_part1_with_input(self):
        controller = SpreadingElves(os.path.join(self.dirname, "input_part1_2.txt"))
        controller.do_round(10)
        res = controller.compute_empty_tiles()
        self.assertEqual(4162, res)

    def test_part2_with_sample(self):
        controller = SpreadingElves(os.path.join(self.dirname, "sample_part1_2.txt"))
        controller.run_to_steady_state()
        res = controller.rounds
        self.assertEqual(20, res)

    def test_part2_with_input(self):
        controller = SpreadingElves(os.path.join(self.dirname, "input_part1_2.txt"))
        controller.run_to_steady_state()
        res = controller.rounds
        self.assertEqual(986, res)


if __name__ == '__main__':
    unittest.main()
