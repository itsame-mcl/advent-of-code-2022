from numpy import base_repr
from math import pow

snafu_equivalences = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


def snafu_to_decimal(snafu):
    decimal = 0
    for i in range(1, len(snafu)+1):
        decimal += snafu_equivalences[snafu[-i]] * pow(5, i-1)
    return decimal


def decimal_to_snafu(number):
    on_base_5 = list(base_repr(number, 5))
    on_snafu = ''
    for i in range(1, len(on_base_5) + 1):
        match on_base_5[-i]:
            case '3':
                if i < len(on_base_5):
                    on_snafu = '=' + on_snafu
                    on_base_5[-i-1] = str(int(on_base_5[-i-1]) + 1)
                else:
                    on_snafu = '1=' + on_snafu
            case '4':
                if i < len(on_base_5):
                    on_snafu = '-' + on_snafu
                    on_base_5[-i - 1] = str(int(on_base_5[-i - 1]) + 1)
                else:
                    on_snafu = '1-' + on_snafu
            case '5':
                if i < len(on_base_5):
                    on_snafu = '0' + on_snafu
                    on_base_5[-i - 1] = str(int(on_base_5[-i - 1]) + 1)
                else:
                    on_snafu = '10' + on_snafu
            case _:
                on_snafu = on_base_5[-i] + on_snafu
    return on_snafu


def sum_snafu(path):
    with open(path) as file:
        snafu_numbers = list(map(lambda l: l.replace('\n', ''), file.readlines()))
    total_converted_snafu = int(sum(list(map(lambda snafu: snafu_to_decimal(snafu), snafu_numbers))))
    total_snafu = decimal_to_snafu(total_converted_snafu)
    return total_snafu
