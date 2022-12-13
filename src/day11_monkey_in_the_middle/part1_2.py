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
        new = new % self.group.modulo
        other = self.if_true if new % self.divisible_by == 0 else self.if_false
        self.throw_to_other(new, other)
        self.items.remove(item)
        self.inspected += 1

    def inspect_all_items(self):
        for item in self.items[:]:
            self.inspect_item(item)


class MonkeyController:
    def __init__(self, worry_decrease=True):
        self.monkeys = []
        self.modulo = 1
        self.worry_decrease = worry_decrease

    def add_monkey(self, items, operation, divisible_by, if_true, if_false):
        new_monkey = Monkey(self, items, operation, divisible_by, if_true, if_false)
        self.monkeys.append(new_monkey)
        self.modulo = self.modulo * divisible_by

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
