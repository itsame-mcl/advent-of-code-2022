def game_engine(strategy, path):
    outcome = 0
    with open(path) as file:
        for line in file:
            opponent, player = line.replace('\n', '').split(" ")
            outcome += strategy[player].value + 6 * (strategy[player] > strategy[opponent]) + \
                3 * (strategy[player] == strategy[opponent])
    return outcome
