from copy import deepcopy


class Monkey:
    def __init__(self, group, items, operation, divisible_by, if_true, if_false):
        self.inspected = 0
        self.group = group
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false

    def catch_from_other(self, item):
        self.items.append(item)

    def throw_to_other(self, item, other):
        other_monkey = self.group.get_monkey(other)
        other_monkey.catch_from_other(item)

    def inspect_item(self, item):
        new = self.operation(item)
        new = new//3 if self.group.worry_decrease else new
        other = self.if_true if new % self.divisible_by == 0 else self.if_false
        self.throw_to_other(new, other)
        self.items.remove(item)
        self.inspected += 1

    def inspect_all_items(self):
        for item in self.items[:]:
            self.inspect_item(item)


class ZNZMonkey(Monkey):
    def inspect_item(self, item):
        match self.operation.split(" "):
            case["+", value]:
                item.add(int(value))
            case["*", value]:
                item.multiply(int(value))
            case["^", value]:
                item.power(int(value))
            case _:
                raise ValueError
        other = self.if_true if item.get_value(self.divisible_by) == 0 else self.if_false
        self.throw_to_other(deepcopy(item), other)
        self.items.remove(item)
        self.inspected += 1


class MonkeyController:
    def __init__(self, worry_decrease=True, znz_monkeys=False):
        self.monkeys = []
        self.worry_decrease = worry_decrease
        self.zn_monkeys = znz_monkeys

    def add_monkey(self, items, operation, divisible_by, if_true, if_false):
        if self.zn_monkeys:
            new_monkey = ZNZMonkey(self, items, operation, divisible_by, if_true, if_false)

        else:
            new_monkey = Monkey(self, items, operation, divisible_by, if_true, if_false)
        self.monkeys.append(new_monkey)

    def get_monkey(self, index):
        return self.monkeys[index]

    def do_rounds(self, n=1):
        for _ in range(0, n):
            for monkey in self.monkeys:
                monkey.inspect_all_items()

    def compute_monkey_business_level(self):
        scores = [monkey.inspected for monkey in self.monkeys]
        scores.sort(reverse=True)
        return scores[0] * scores[1]
