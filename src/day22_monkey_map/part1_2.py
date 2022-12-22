from re import findall


def offset_and_get_face(position, cube):
    for face in cube.keys():
        position_offset = position - face
        if 0 <= position_offset.real < cube[face]['size'] and 0 <= position_offset.imag < cube[face]['size']:
            return position_offset, cube[face]


def rotate_and_move_to_another_face(position_offset, direction, face):
    corrections = {1: -face['size'], 1j: -face['size']*1j, -1: face['size'], -1j: face['size']*1j}
    center = ((face['size'] - 1) / 2 + ((face['size'] - 1) / 2) * 1j)
    position_centered = position_offset - center
    destination_offset, rotation = face[direction]
    direction_after_rotation = direction * rotation
    position_after_rotation = (position_centered * rotation) + center + destination_offset + corrections[direction_after_rotation]
    return position_after_rotation, direction_after_rotation


def parse_map_line(line, y):
    tiles = set()
    walls = set()
    for x in range(len(line)):
        if line[x] == '.':
            tiles.add((x + 1) + y * 1j)
        if line[x] == '#':
            walls.add((x + 1) + y * 1j)
    return tiles, walls


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
                new_tiles, new_walls = parse_map_line(line, y)
                tiles.update(new_tiles)
                walls.update(new_walls)
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


def proceed_around_cube(position: complex, direction: complex, cube):
    position_offset, face = offset_and_get_face(position, cube)
    position_after, direction_after = rotate_and_move_to_another_face(position_offset, direction, face)
    return position_after, direction_after


def move(start: complex, direction: complex, tiles: set[complex], walls: set[complex]):
    final = start + direction
    if final not in tiles.union(walls):
        final = wrap(final, direction, tiles, walls)
    if final in tiles:
        return final
    return start


def move_around_cube(start: complex, direction: complex, tiles: set[complex], walls: set[complex], cube):
    final = start + direction
    final_direction = direction
    if final not in tiles.union(walls):
        start_rotated, final_direction = proceed_around_cube(start, direction, cube)
        final = start_rotated + final_direction
    if final in tiles:
        return final, final_direction
    return start, direction


def follow_directions(path, cube=None):
    tiles, walls, pattern = parse_input(path)
    position = min([tile.real for tile in tiles if tile.imag == 1]) + 1j
    facing = {1: 0, 1j: 1, -1: 2, -1j: 3}
    direction = 1
    for instruction in pattern:
        if instruction == 'R':
            direction = direction * 1j
        elif instruction == 'L':
            direction = direction * -1j
        else:
            for _ in range(int(instruction)):
                if not cube:
                    new_position = move(position, direction, tiles, walls)
                else:
                    new_position, new_direction = move_around_cube(position, direction, tiles, walls, cube)
                if new_position == position:
                    break
                else:
                    position = new_position
                    if cube:
                        direction = new_direction
    return position.imag * 1000 + position.real * 4 + facing[direction]
