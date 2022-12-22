from re import findall


def parse_input(path):
    tiles = set()
    walls = set()
    pattern = []
    y = 1
    map_parsed = False
    with open(path) as file:
        for line in file:
            line = line.replace('\n', '')
            if line != '' and not map_parsed:
                for x in range(len(line)):
                    if line[x] == '.':
                        tiles.add((x+1)+y*1j)
                    if line[x] == '#':
                        walls.add((x+1)+y*1j)
                y += 1
            if line != '' and map_parsed:
                pattern = findall(r'\d+|[RL]', line)
            if line == '':
                map_parsed = True
    return tiles, walls, pattern


def wrap(position: complex, direction: complex, tiles: set[complex], walls: set[complex]):
    board = tiles.union(walls)
    match direction:
        case 1:
            final = min([tile.real for tile in board if tile.imag == position.imag]) + position.imag * 1j
        case - 1:
            final = max([tile.real for tile in board if tile.imag == position.imag]) + position.imag * 1j
        case 1j:
            final = position.real + min([tile.imag for tile in board if tile.real == position.real]) * 1j
        case - 1j:
            final = position.real + max([tile.imag for tile in board if tile.real == position.real]) * 1j
    return final


def move(start: complex, direction: complex, tiles: set[complex], walls: set[complex]):
    final = start + direction
    if final not in tiles.union(walls):
        final = wrap(final, direction, tiles, walls)
    if final in tiles:
        return final
    return start


def follow_directions(path):
    tiles, walls, pattern = parse_input(path)
    position = min([tile.real for tile in tiles if tile.imag == 1]) + 1j
    facing = {1: 0, -1j: 1, -1: 2, 1j: 3}
    direction = 1
    for instruction in pattern:
        if instruction == 'R':
            direction = direction * 1j
        elif instruction == 'L':
            direction = direction * -1j
        else:
            for _ in range(int(instruction)):
                new_position = move(position, direction, tiles, walls)
                if new_position == position:
                    break
                else:
                    position = new_position
    return position.imag * 1000 + position.real * 4 + facing[direction]
