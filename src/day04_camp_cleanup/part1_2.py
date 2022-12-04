def sum_triggers(path, trigger):
    outcome = 0
    with open(path) as file:
        for line in file:
            limits = line.replace('\n', '').replace(',', '-').split('-')
            first = set(range(int(limits[0]), int(limits[1]) + 1))
            second = set(range(int(limits[2]), int(limits[3]) + 1))
            match trigger:
                case 'subsets':
                    is_triggered = first.issubset(second) or second.issubset(first)
                case 'overlaps':
                    is_triggered = len(first.intersection(second)) > 0
                case _:
                    raise NotImplementedError
            if is_triggered:
                outcome += 1
    return outcome
