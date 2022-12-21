from collections import namedtuple
from typing import Union
from parse import compile
from z3 import Real, Solver

OperationMonkey = namedtuple("OperationMonkey", "first second operation")
ValueMonkey = namedtuple("ValueMonkey", "value")


def get_monkeys(path):
    parse_value = compile("{name:4l}: {value:d}")
    parse_operation = compile("{name:4l}: {first:4l} {operation} {second:4l}")
    monkeys: dict[str, Union[ValueMonkey, OperationMonkey]] = {}
    with open(path) as file:
        for line in file:
            line = line.replace('\n', '')
            with_value = parse_value.parse(line)
            with_operation = parse_operation.parse(line)
            if with_value:
                monkeys[with_value.named['name']] = ValueMonkey(value=with_value.named['value'])
            if with_operation:
                monkeys[with_operation.named['name']] = OperationMonkey(first=with_operation.named['first'],
                                                                        second=with_operation.named['second'],
                                                                        operation=with_operation.named['operation'])
    return monkeys


def set_problem_and_solve(monkeys: dict[str, Union[ValueMonkey, OperationMonkey]], objective):
    z3_monkeys = {}
    solver = Solver()
    for monkey_name in monkeys.keys():
        z3_monkeys[monkey_name] = Real(monkey_name)
    if objective == 'humn':
        monkeys['root'] = OperationMonkey._replace(monkeys['root'], operation='=')
        del monkeys['humn']
        del z3_monkeys['root']
    for name, monkey in monkeys.items():
        if isinstance(monkey, ValueMonkey):
            solver.add(z3_monkeys[name] == monkey.value)
        if isinstance(monkey, OperationMonkey):
            match monkey.operation:
                case '+':
                    solver.add(z3_monkeys[name] == z3_monkeys[monkey.first] + z3_monkeys[monkey.second])
                case '-':
                    solver.add(z3_monkeys[name] == z3_monkeys[monkey.first] - z3_monkeys[monkey.second])
                case '*':
                    solver.add(z3_monkeys[name] == z3_monkeys[monkey.first] * z3_monkeys[monkey.second])
                case '/':
                    solver.add(z3_monkeys[name] == z3_monkeys[monkey.first] / z3_monkeys[monkey.second])
                case '=':
                    solver.add(z3_monkeys[monkey.first] == z3_monkeys[monkey.second])
                case _:
                    raise ValueError
    solver.check()
    return solver.model()[z3_monkeys[objective]].as_long()


def solve_with_z3(path, objective):
    monkeys = get_monkeys(path)
    return set_problem_and_solve(monkeys, objective)
