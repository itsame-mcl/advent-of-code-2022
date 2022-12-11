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

    def inspect_item(self, item, worry_decrease):
        new = self.operation(item)
        new = new//3 if worry_decrease else new
        other = self.if_true if new % self.divisible_by == 0 else self.if_false
        self.throw_to_other(new, other)
        self.items.remove(item)
        self.inspected += 1

    def inspect_all_items(self, worry_decrease):
        for item in self.items[:]:
            self.inspect_item(item, worry_decrease)


class MonkeyGroup:
    def __init__(self):
        self.monkeys = []

    def add_monkey(self, items, operation, divisible_by, if_true, if_false):
        new_monkey = Monkey(self, items, operation, divisible_by, if_true, if_false)
        self.monkeys.append(new_monkey)

    def get_monkey(self, index):
        return self.monkeys[index]

    def do_rounds(self, n = 1, worry_decrease = True):
        for _ in range(0,n):
            for monkey in self.monkeys:
                monkey.inspect_all_items(worry_decrease)

    def compute_monkey_business_level(self):
        scores = [monkey.inspected for monkey in self.monkeys]
        scores.sort(reverse=True)
        return scores[0] * scores[1]
