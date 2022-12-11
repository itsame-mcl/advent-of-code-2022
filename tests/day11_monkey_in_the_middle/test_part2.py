import unittest
from src.day11_monkey_in_the_middle.monkey import MonkeyController


class TestDay11Part2(unittest.TestCase):

    def test_part2_with_sample(self):
        monkeys = MonkeyController(False)
        monkeys.add_monkey([79, 98], lambda old: old * 19, 23, 2, 3)
        monkeys.add_monkey([54, 65, 75, 74], lambda old: old + 6, 19, 2, 0)
        monkeys.add_monkey([79, 60, 97], lambda old: old * old, 13, 1, 3)
        monkeys.add_monkey([74], lambda old: old + 3, 17, 0, 1)
        monkeys.do_rounds(10000)
        score = monkeys.compute_monkey_business_level()
        self.assertEqual(2713310158, score)

    def test_part2_with_input(self):
        monkeys = MonkeyController(False)
        monkeys.add_monkey([91, 54, 70, 61, 64, 64, 60, 85], lambda old: old * 13, 2, 5, 2)
        monkeys.add_monkey([82], lambda old: old + 7, 13, 4, 3)
        monkeys.add_monkey([84, 93, 70], lambda old: old + 2, 5, 5, 1)
        monkeys.add_monkey([78, 56, 85, 93], lambda old: old * 2, 3, 6, 7)
        monkeys.add_monkey([64, 57, 81, 95, 52, 71, 58], lambda old: old * old, 11, 7, 3)
        monkeys.add_monkey([58, 71, 96, 58, 68, 90], lambda old: old + 6, 17, 4, 1)
        monkeys.add_monkey([56, 99, 89, 97, 81], lambda old: old + 1, 7, 0, 2)
        monkeys.add_monkey([68, 72], lambda old: old + 8, 19, 6, 0)
        monkeys.do_rounds(10000)
        score = monkeys.compute_monkey_business_level()
        self.assertEqual(16792940265, score)


if __name__ == '__main__':
    unittest.main()
