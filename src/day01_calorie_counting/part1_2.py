def max_calories(path, top=1):
    elfes = []
    with open(path) as file:
        count = 0
        for line in file:
            if line == "\n":
                elfes.append(count)
                count = 0
            else:
                count += int(line)
    elfes.append(count)
    elfes = sorted(elfes, reverse=True)
    return sum(elfes[0:top])
