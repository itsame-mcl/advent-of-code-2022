def sum_duplicates(path):
    outcome = 0
    with open(path) as file:
        for line in file:
            items = line.replace('\n', '')
            first_half, second_half = [*items[:len(items)//2]], [*items[len(items)//2:]]
            common_item = list(set(first_half).intersection(second_half))
            ascii_code_item = ord(common_item[0])
            outcome += ascii_code_item - 96 if ascii_code_item >= 97 else ascii_code_item - 38
    return outcome
