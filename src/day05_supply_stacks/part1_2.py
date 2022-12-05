from queue import LifoQueue


def top_crates(path, block=False):
    outcome = ""
    with open(path) as file:
        input_data = list(map(lambda l: l.replace('\n', ''), file.readlines()))
    pivot_line = input_data.index('')
    initial_state = input_data[:(pivot_line-1)]
    operations = input_data[(pivot_line+1):]
    stacks = [LifoQueue() for _ in range(0, (len(initial_state[-1])+1)//4)]
    for line in reversed(initial_state):
        for i in range(0, len(stacks)):
            if (i*4 + 1) < len(line) and line[i*4 + 1] != ' ':
                stacks[i].put_nowait(line[i*4 + 1])
    for line in operations:
        operation = line.split(" ")
        if block:
            block_items = []
            for _ in range(0, int(operation[1])):
                block_items.append(stacks[int(operation[3])-1].get_nowait())
            for item in reversed(block_items):
                stacks[int(operation[5]) - 1].put_nowait(item)
        else:
            for _ in range(0, int(operation[1])):
                stacks[int(operation[5])-1].put_nowait(stacks[int(operation[3])-1].get_nowait())
    for stack in stacks:
        outcome += stack.get_nowait()
    return outcome
