import numpy as np


def tree_house_computations(path, mode):
    with open(path) as file:
        input_data = list(map(lambda l: l.replace('\n', ''), file.readlines()))
    grid = np.array(list(map(lambda l: [int(x) for x in l], input_data)))
    outcome = 0
    for x in range(0, grid.shape[0]):
        for y in range(0, grid.shape[1]):
            north = grid[:x, y]
            south = grid[x+1:, y]
            west = grid[x, :y]
            east = grid[x, y+1:]
            match mode:
                case "visible_trees":
                    if x in [0, grid.shape[0]-1] or y in [0, grid.shape[1]-1] or \
                            grid[x, y] > min(0 if north.size == 0 else max(north), 0 if south.size == 0 else max(south),
                                             0 if west.size == 0 else max(west), 0 if east.size == 0 else max(east)):
                        outcome += 1
                case "scenic_score":
                    north_score = 0
                    for tree in np.flip(north):
                        north_score += 1
                        if tree >= grid[x, y]:
                            break
                    west_score = 0
                    for tree in np.flip(west):
                        west_score += 1
                        if tree >= grid[x, y]:
                            break
                    east_score = 0
                    for tree in east:
                        east_score += 1
                        if tree >= grid[x, y]:
                            break
                    south_score = 0
                    for tree in south:
                        south_score += 1
                        if tree >= grid[x, y]:
                            break
                    scenic_score = north_score * west_score * east_score * south_score
                    if scenic_score > outcome:
                        outcome = scenic_score
    return outcome
