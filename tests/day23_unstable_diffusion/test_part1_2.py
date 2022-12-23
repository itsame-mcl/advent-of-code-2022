import unittest
import os
from src.day23_unstable_diffusion.elves import ElvesController
from src.day23_unstable_diffusion.part1_2 import do_rounds_and_compute_empty_tiles,\
    do_complete_simulation_and_compute_rounds


class TestDay22(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)

    def test_str_controller(self):
        controller = ElvesController(os.path.join(self.dirname, "small_sample_part1_2.txt"))
        self.assertEqual("##\n#.\n..\n##\n", str(controller))

    def test_part1_with_sample(self):
        res = do_rounds_and_compute_empty_tiles(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(110, res)

    def test_part1_with_input(self):
        res = do_rounds_and_compute_empty_tiles(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(4162, res)

    def test_part2_with_sample(self):
        res = do_complete_simulation_and_compute_rounds(os.path.join(self.dirname, "sample_part1_2.txt"))
        self.assertEqual(20, res)

    @unittest.skip("Very long to compute (~ 20 min)")
    def test_part2_with_input(self):
        res = do_complete_simulation_and_compute_rounds(os.path.join(self.dirname, "input_part1_2.txt"))
        self.assertEqual(986, res)


if __name__ == '__main__':
    unittest.main()
