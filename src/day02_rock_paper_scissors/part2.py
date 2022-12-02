from src.day02_rock_paper_scissors.enum_RPS import RPS


def game_engine(path):
    outcome = 0
    strategy = {'A': RPS.ROCK, 'B': RPS.PAPER, 'C': RPS.SCISSORS}
    with open(path) as file:
        for line in file:
            opponent, desired_outcome = line.replace('\n', '').split(" ")
            match desired_outcome:
                case 'X':
                    if strategy[opponent] == RPS.ROCK:
                        player = RPS.SCISSORS
                    else:
                        player = RPS(strategy[opponent].value - 1)
                case 'Y':
                    player = strategy[opponent]
                case 'Z':
                    if strategy[opponent] == RPS.SCISSORS:
                        player = RPS.ROCK
                    else:
                        player = RPS(strategy[opponent].value + 1)
                case _:
                    raise ValueError
            # noinspection PyTypeChecker
            outcome += player.value + 6 * (player > strategy[opponent]) + \
                3 * (player == strategy[opponent])
    return outcome
