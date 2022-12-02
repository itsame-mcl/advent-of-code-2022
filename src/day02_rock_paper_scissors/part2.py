from src.day02_rock_paper_scissors.enum_choice import Choice


def game_engine(path):
    outcome = 0
    strategy = {'A': Choice.ROCK, 'B': Choice.PAPER, 'C': Choice.SCISSORS}
    with open(path) as file:
        for line in file:
            opponent, desired_outcome = line.replace('\n', '').split(" ")
            match desired_outcome:
                case 'X':
                    if strategy[opponent] == Choice.ROCK:
                        player = Choice.SCISSORS
                    else:
                        player = Choice(strategy[opponent].value - 1)
                case 'Y':
                    player = strategy[opponent]
                case 'Z':
                    if strategy[opponent] == Choice.SCISSORS:
                        player = Choice.ROCK
                    else:
                        player = Choice(strategy[opponent].value + 1)
                case _:
                    raise ValueError
            # noinspection PyTypeChecker
            outcome += player.value + 6 * (player > strategy[opponent]) + \
                3 * (player == strategy[opponent])
    return outcome
