import unittest
from src.day11_monkey_in_the_middle.monkey import MonkeyController
from src.day11_monkey_in_the_middle.znz_integer import ZNZInteger


class TestDay11Part2(unittest.TestCase):

    def test_part2_with_invalid_sample(self):
        monkeys = MonkeyController(False, True)
        monkeys.add_monkey([ZNZInteger(79, [13, 17, 19, 23]), ZNZInteger(98, [13, 17, 19, 23])],
                           "/ 2", 23, 0, 0)
        self.assertRaises(ValueError, monkeys.do_rounds)

    def test_part2_with_sample(self):
        monkeys = MonkeyController(False, True)
        monkeys.add_monkey([ZNZInteger(79, [13, 17, 19, 23]), ZNZInteger(98, [13, 17, 19, 23])],
                           "* 19", 23, 2, 3)
        monkeys.add_monkey([ZNZInteger(54, [13, 17, 19, 23]), ZNZInteger(65, [13, 17, 19, 23]),
                            ZNZInteger(75, [13, 17, 19, 23]), ZNZInteger(74, [13, 17, 19, 23])],
                           "+ 6", 19, 2, 0)
        monkeys.add_monkey([ZNZInteger(79, [13, 17, 19, 23]), ZNZInteger(60, [13, 17, 19, 23]),
                            ZNZInteger(97, [13, 17, 19, 23])], "^ 2", 13, 1, 3)
        monkeys.add_monkey([ZNZInteger(74, [13, 17, 19, 23])], "+ 3", 17, 0, 1)
        monkeys.do_rounds(10000)
        score = monkeys.compute_monkey_business_level()
        self.assertEqual(2713310158, score)

    def test_part2_with_input(self):
        monkeys = MonkeyController(False, True)
        monkeys.add_monkey([ZNZInteger(91, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(54, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(70, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(61, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(64, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(64, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(60, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(85, [2, 3, 5, 7, 11, 13, 17, 19])], "* 13", 2, 5, 2)
        monkeys.add_monkey([ZNZInteger(82, [2, 3, 5, 7, 11, 13, 17, 19])], "+ 7", 13, 4, 3)
        monkeys.add_monkey([ZNZInteger(84, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(93, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(70, [2, 3, 5, 7, 11, 13, 17, 19])], "+ 2", 5, 5, 1)
        monkeys.add_monkey([ZNZInteger(78, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(56, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(85, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(93, [2, 3, 5, 7, 11, 13, 17, 19])], "* 2", 3, 6, 7)
        monkeys.add_monkey([ZNZInteger(64, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(57, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(81, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(95, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(52, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(71, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(58, [2, 3, 5, 7, 11, 13, 17, 19])], "^ 2", 11, 7, 3)
        monkeys.add_monkey([ZNZInteger(58, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(71, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(96, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(58, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(68, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(90, [2, 3, 5, 7, 11, 13, 17, 19])], "+ 6", 17, 4, 1)
        monkeys.add_monkey([ZNZInteger(56, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(99, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(89, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(97, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(81, [2, 3, 5, 7, 11, 13, 17, 19])], "+ 1", 7, 0, 2)
        monkeys.add_monkey([ZNZInteger(68, [2, 3, 5, 7, 11, 13, 17, 19]),
                            ZNZInteger(72, [2, 3, 5, 7, 11, 13, 17, 19])], "+ 8", 19, 6, 0)
        monkeys.do_rounds(10000)
        score = monkeys.compute_monkey_business_level()
        self.assertEqual(16792940265, score)


if __name__ == '__main__':
    unittest.main()
