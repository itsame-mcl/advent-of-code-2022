def generate_rocks(shape, top_line):
    match shape:
        case '-':
            rocks = {3+(top_line+4)*1j, 4+(top_line+4)*1j, 5+(top_line+4)*1j, 6+(top_line+4)*1j}
        case '+':
            rocks = {3+(top_line+5)*1j, 4+(top_line+4)*1j, 4+(top_line+5)*1j, 4+(top_line+6)*1j, 5+(top_line+5)*1j}
        case 'L':
            rocks = {3+(top_line+4)*1j, 4+(top_line+4)*1j, 5+(top_line+4)*1j, 5+(top_line+5)*1j, 5+(top_line+6)*1j}
        case 'I':
            rocks = {3+(top_line+4)*1j, 3+(top_line+5)*1j, 3+(top_line+6)*1j, 3+(top_line+7)*1j}
        case _:
            rocks = {3+(top_line+4)*1j, 4+(top_line+4)*1j, 3+(top_line+5)*1j, 4+(top_line+5)*1j}
    return rocks


def lateral_move(current_rocks, new_rocks, lateral_direction):
    final_rocks = new_rocks
    match lateral_direction:
        case '<':
            new_rocks_candidate = {rock - 1 for rock in new_rocks}
            if min({rock.real for rock in new_rocks_candidate}) > 0 and len(
                    current_rocks.intersection(new_rocks_candidate)) == 0:
                final_rocks = new_rocks_candidate
        case '>':
            new_rocks_candidate = {rock + 1 for rock in new_rocks}
            if max({rock.real for rock in new_rocks_candidate}) <= 7 and len(
                    current_rocks.intersection(new_rocks_candidate)) == 0:
                final_rocks = new_rocks_candidate
        case _:
            raise ValueError
    return final_rocks


def downward_move(current_rocks, new_rocks):
    final_rocks = new_rocks
    new_rocks_candidate = {rock - 1j for rock in new_rocks}
    if min({rock.imag for rock in new_rocks_candidate}) > 0 and len(
            current_rocks.intersection(new_rocks_candidate)) == 0:
        final_rocks = new_rocks_candidate
    return final_rocks, new_rocks == final_rocks


def single_rock_falling(current_rocks, shape, jet_pattern, pattern_cursor):
    top_line = max({rock.imag for rock in current_rocks}, default=0)
    new_rocks = generate_rocks(shape, top_line)
    is_at_rest = False
    while not is_at_rest:
        new_rocks = lateral_move(current_rocks, new_rocks, jet_pattern[pattern_cursor])
        pattern_cursor = (pattern_cursor + 1) % len(jet_pattern)
        new_rocks, is_at_rest = downward_move(current_rocks, new_rocks)
    return new_rocks, pattern_cursor


def cycle_finder(steps):
    last_cursors = (steps[-1][1])
    last_top = steps[-1][3]
    cycle_begin = [step for step in steps[:-1] if step[1] == last_cursors and step[3] ^ last_top == set()]
    if cycle_begin:
        cycle_len = steps[-1][0] - cycle_begin[0][0]
        cycle_height = steps[-1][2] - cycle_begin[0][2]
        return cycle_len, cycle_height
    return None, None


def tower_of_rocks(jet_pattern, number_of_rocks):
    shapes = ['-', '+', 'L', 'I', 'O']
    shapes_cursor = 0
    pattern_cursor = 0
    cycle_len = None
    cycle_height = None
    number_of_cycles = 0
    rocks = set()
    steps = list()
    i = 0
    while i < number_of_rocks:
        new_rocks, pattern_cursor = single_rock_falling(rocks, shapes[shapes_cursor], jet_pattern, pattern_cursor)
        shapes_cursor = (shapes_cursor + 1) % len(shapes)
        rocks = rocks.union(new_rocks)
        if cycle_len is None:
            top_line = max({rock.imag for rock in rocks}, default=0)
            top_subset = {rock.real+(rock.imag-(top_line-8))*1j for rock in rocks if rock.imag > top_line - 8}
            steps.append((i, (shapes_cursor, pattern_cursor), int(max({rock.imag for rock in rocks})), top_subset))
            cycle_len, cycle_height = cycle_finder(steps)
            if cycle_len is not None:
                number_of_cycles = (number_of_rocks - i - 1) // cycle_len
                i = i + number_of_cycles * cycle_len
        i += 1
    if cycle_height:
        return int(max({rock.imag for rock in rocks}) + number_of_cycles * cycle_height)
    return int(max({rock.imag for rock in rocks}))
