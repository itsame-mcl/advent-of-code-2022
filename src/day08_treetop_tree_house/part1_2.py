import numpy as np


def generate_grid(path):
    with open(path) as file:
        input_data = list(map(lambda l: l.replace('\n', ''), file.readlines()))
    return np.array(list(map(lambda l: [int(x) for x in l], input_data)))


def grid_walker(grid, fun):
    outcome = []
    for x in range(0, grid.shape[0]):
        for y in range(0, grid.shape[1]):
            north = grid[:x, y]
            south = grid[x + 1:, y]
            west = grid[x, :y]
            east = grid[x, y + 1:]
            outcome.append(fun(grid[x, y], north, south, west, east))
    return outcome


def tree_is_visible(current, north, south, west, east):
    on_edge = min(north.size, south.size, west.size, east.size) == 0
    is_visible = current > min(0 if north.size == 0 else max(north), 0 if south.size == 0 else max(south),
                               0 if west.size == 0 else max(west), 0 if east.size == 0 else max(east))
    return int(on_edge or is_visible)


def visible_trees_from_pos(current, neighbours):
    visibles = 0
    for neighbour in neighbours:
        visibles += 1
        if neighbour >= current:
            break
    return visibles


def scenic_score(current, north, south, west, east):
    partials_scores = [visible_trees_from_pos(current, direction) for direction
                       in [np.flip(north), np.flip(west), south, east]]
    return int(np.prod(partials_scores))


def number_of_visible_trees(path):
    grid = generate_grid(path)
    outcome = grid_walker(grid, tree_is_visible)
    return sum(outcome)


def best_scenic_score(path):
    grid = generate_grid(path)
    outcome = grid_walker(grid, scenic_score)
    return max(outcome)
