from ast import literal_eval
from functools import cmp_to_key


def cmp(left, right):
    return (left > right) - (left < right)


def compare_values(left, right):
    index = 0
    while True:
        left_is_list = False
        right_is_list = False
        left_is_out_of_items = False
        right_is_out_of_items = False
        try:
            left_is_list = isinstance(left[index], list)
        except IndexError:
            left_is_out_of_items = True
        try:
            right_is_list = isinstance(right[index], list)
        except IndexError:
            right_is_out_of_items = True
        match [left_is_out_of_items, right_is_out_of_items]:
            case [True, True]:
                return 0
            case [True, False]:
                return -1
            case [False, True]:
                return 1
            case _:
                match [left_is_list, right_is_list]:
                    case [True, True]:
                        res = compare_values(left[index], right[index])
                    case [True, False]:
                        res = compare_values(left[index], [right[index]])
                    case [False, True]:
                        res = compare_values([left[index]], right[index])
                    case _:
                        res = cmp(left[index], right[index])
        if res != 0:
            return res
        index += 1


def check_signal(path):
    with open(path) as file:
        outcome = 0
        block_index = 1
        left = None
        for line in file:
            line = line.replace('\n', '')
            if line != '':
                if left is None:
                    left = literal_eval(line)
                else:
                    right = literal_eval(line)
                    if compare_values(left, right) == -1:
                        outcome += block_index
                    block_index += 1
                    left = None
    return outcome


def find_decoder_key(path):
    with open(path) as file:
        signals = file.readlines()
        signals = list(map(lambda l: l.replace('\n', ''), signals))
        signals = list(filter(lambda l: l != '', signals))
        signals = list(map(lambda l: literal_eval(l), signals))
        signals.append([[2]])
        signals.append([[6]])
        signals = sorted(signals, key=cmp_to_key(compare_values))
        return (signals.index([[2]]) + 1) * (signals.index([[6]]) + 1)
