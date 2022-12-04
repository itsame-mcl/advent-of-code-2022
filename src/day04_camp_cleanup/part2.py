def sum_overlaps(path):
    outcome = 0
    with open(path) as file:
        for line in file:
            limits = line.replace('\n', '').replace(',', '-').split('-')
            first = set(range(int(limits[0]), int(limits[1]) + 1))
            second = set(range(int(limits[2]), int(limits[3]) + 1))
            if len(first.intersection(second)) > 0:
                outcome += 1
    return outcome
