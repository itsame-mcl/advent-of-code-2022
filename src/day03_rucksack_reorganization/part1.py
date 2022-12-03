def sum_duplicates(path):
    outcome = 0
    with open(path) as file:
        for line in file:
            items = line.replace('\n', '')
            common_item = list(set(items[:len(items)//2]).intersection(items[len(items)//2:]))
            ascii_code_item = ord(common_item[0])
            outcome += ascii_code_item - 96 if ascii_code_item >= 97 else ascii_code_item - 38
    return outcome
