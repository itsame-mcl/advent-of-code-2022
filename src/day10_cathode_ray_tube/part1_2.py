def do_cycles(path):
    cycle = 0
    register = 1
    states = {}
    with open(path) as file:
        for line in file:
            instruction = line.replace('\n', '').split(' ')
            match instruction:
                case ['noop']:
                    states[str(cycle + 1)] = register
                    cycle += 1
                case ['addx', value] if value.lstrip('-').isnumeric():
                    states[str(cycle + 1)] = register
                    states[str(cycle + 2)] = register
                    cycle += 2
                    register += int(value)
    return states


def compute_signal_strength(path):
    states = do_cycles(path)
    return 20 * states['20'] + 60 * states['60'] + 100 * states['100'] + 140 * states['140'] +\
        180 * states['180'] + 220 * states['220']


def draw_crt(path):
    states = do_cycles(path)
    crt = str()
    for line in range(0, 6):
        for position in range(1, 41):
            if position in range(states[str(line*40+position)], states[str(line*40+position)]+3):
                crt += '#'
            else:
                crt += '.'
        crt += '\n'

    return crt
