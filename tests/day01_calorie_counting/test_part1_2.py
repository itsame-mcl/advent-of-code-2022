import unittest
import src.day01_calorie_counting.part1_2 as src


class TestDay1(unittest.TestCase):
    def test_part1_with_sample(self):
        res = src.max_calories("day01_calorie_counting/sample_part1_2.txt")
        self.assertEqual(24000, res)

    def test_part1_with_input(self):
        res = src.max_calories("day01_calorie_counting/input_part1_2.txt")
        self.assertEqual(69693, res)

    def test_part2_with_sample(self):
        res = src.max_calories("day01_calorie_counting/sample_part1_2.txt", 3)
        self.assertEqual(45000, res)

    def test_part2_with_input(self):
        res = src.max_calories("day01_calorie_counting/input_part1_2.txt", 3)
        self.assertEqual(200945, res)


if __name__ == '__main__':
    unittest.main()
