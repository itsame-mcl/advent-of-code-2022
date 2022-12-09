from src.day09_rope_bridge.rope import Rope


def visited_positions(path, rope_len):
    rope = Rope(rope_len)
    positions = [rope.tail_position()]
    with open(path) as file:
        for line in file:
            direction, repetition = line.replace('\n', '').split(' ')
            for _ in range(0, int(repetition)):
                rope.move(direction)
                positions.append(rope.tail_position())
    return len(set(positions))
