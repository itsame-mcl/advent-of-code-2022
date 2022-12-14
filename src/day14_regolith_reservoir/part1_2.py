def compute_rocks_between(first, second):
    first = [int(first[0]), int(first[1])]
    second = [int(second[0]), int(second[1])]
    rocks = set()
    if first[0] == second[0]:
        x = first[0]
        for y in range(min(first[1], second[1]), max(first[1], second[1])+1):
            rocks.add(x+y*1j)
    if first[1] == second[1]:
        y = first[1]
        for x in range(min(first[0], second[0]), max(first[0], second[0])+1):
            rocks.add(x+y*1j)
    return rocks


def populate_rocks(path):
    with open(path) as file:
        rocks = set()
        for line in file:
            line = line.replace('\n', '').split(' -> ')
            for i in range(1, len(line)):
                first = line[i-1].split(',')
                second = line[i].split(',')
                rocks.update(compute_rocks_between(first, second))
    return rocks


def find_baseline(rocks):
    depth = set(map(lambda x: x.imag, rocks))
    return max(depth)


def sand_fall(rocks, baseline, floor):
    is_at_rest = False
    falls_into_void = False
    position = 500+0*1j
    while not is_at_rest and not falls_into_void:
        if floor and (position+1j).imag == baseline:
            is_at_rest = True
        elif position+1j not in rocks:
            position = position + 1j
        elif position - 1 + 1j not in rocks:
            position = position - 1 + 1j
        elif position + 1 + 1j not in rocks:
            position = position + 1 + 1j
        else:
            is_at_rest = True
        if position.imag == baseline:
            falls_into_void = True
    return position


def saturate_with_resting_sand(path, floor=False):
    rocks = populate_rocks(path)
    baseline = find_baseline(rocks)
    if floor:
        baseline += 2
    falls_into_void = False
    is_at_source = False
    sands = 0
    while not falls_into_void and not is_at_source:
        new_sand = sand_fall(rocks, baseline, floor)
        if new_sand.imag != baseline:
            sands += 1
            rocks.add(new_sand)
        else:
            falls_into_void = True
        if new_sand == 500+0*1j:
            is_at_source = True
    return sands
