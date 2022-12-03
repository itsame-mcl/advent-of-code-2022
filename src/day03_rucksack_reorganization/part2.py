def sum_badges(path):
    outcome = 0
    input_file = open(path)
    ruckpacks = input_file.readlines()
    input_file.close()
    ruckpacks = list(map(lambda l: l.replace('\n', ''), ruckpacks))
    for x in range(0, len(ruckpacks), 3):
        common_item = list(set(ruckpacks[x]) & set(ruckpacks[x+1]) & set(ruckpacks[x+2]))
        ascii_code_item = ord(common_item[0])
        outcome += ascii_code_item - 96 if ascii_code_item >= 97 else ascii_code_item - 38
    return outcome
