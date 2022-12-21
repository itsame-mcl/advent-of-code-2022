import math
from collections import namedtuple
from parse import compile
from copy import copy

Monkey = namedtuple("Monkey", "first second operation")


def get_monkeys(path):
    parse_value = compile("{name:4l}: {value:d}")
    parse_operation = compile("{name:4l}: {first:4l} {operation_type} {second:4l}")
    operations: dict[str, Monkey] = {}
    values: dict[str, int] = {}
    with open(path) as file:
        for line in file:
            line = line.replace('\n', '')
            with_value = parse_value.parse(line)
            with_operation = parse_operation.parse(line)
            if with_value:
                values[with_value.named['name']] = with_value.named['value']
            if with_operation:
                match with_operation.named['operation_type']:
                    case '+':
                        op = lambda first, second: first + second
                    case '-':
                        op = lambda first, second: first - second
                    case '*':
                        op = lambda first, second: first * second
                    case '/':
                        op = lambda first, second: first / second
                operations[with_operation.named['name']] = Monkey(first=with_operation.named['first'],
                                                                  second=with_operation.named['second'],
                                                                  operation=op)
    return values, operations


def compute_root_value(values, operations, human=None):
    local_values = copy(values)
    local_operations = copy(operations)
    if human:
        local_values['humn'] = human
        local_operations['root'] = Monkey._replace(local_operations['root'],
                                                   operation=lambda first, second: first - second)
    while 'root' not in local_values:
        operations_round = copy(local_operations)
        for name, operation in operations_round.items():
            if operation.first in local_values and operation.second in local_values:
                local_values[name] = operation.operation(local_values[operation.first], local_values[operation.second])
                del local_operations[name]
    return local_values['root']


def run_computation(path):
    values, operations = get_monkeys(path)
    return compute_root_value(values, operations)


def solve_root_equality(path):
    values, operations = get_monkeys(path)
    space_dimension = 1
    lower_bound = -1
    higher_bound = 1
    # Assume the function is monotonous
    is_increasing = compute_root_value(values, operations, higher_bound) >\
                    compute_root_value(values, operations, lower_bound)
    while compute_root_value(values, operations, lower_bound) *\
            compute_root_value(values, operations, higher_bound) > 0:
        space_dimension += 1
        lower_bound = -math.pow(10, space_dimension)
        higher_bound = math.pow(10, space_dimension)
    root_difference, dichotomous_value = None, None
    while root_difference != 0:
        dichotomous_value = (lower_bound + higher_bound) // 2
        # Assume 0 is a discontinuity of the function
        dichotomous_value = 1 if dichotomous_value == 0 else dichotomous_value
        root_difference = compute_root_value(values, operations, dichotomous_value)
        if (is_increasing and root_difference < 0) or (not is_increasing and root_difference > 0):
            lower_bound = dichotomous_value + 1
        else:
            higher_bound = dichotomous_value - 1
    return dichotomous_value
