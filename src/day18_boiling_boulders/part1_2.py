def get_cubes(path):
    cubes = set()
    with open(path) as file:
        for line in file:
            coords = line.replace('\n', '').split(',')
            cubes.add((int(coords[0]), int(coords[1]), int(coords[2])))
    return cubes


def get_neighbors(cube):
    return {(cube[0]+1, cube[1], cube[2]), (cube[0]-1, cube[1], cube[2]),
            (cube[0], cube[1]+1, cube[2]), (cube[0], cube[1]-1, cube[2]),
            (cube[0], cube[1], cube[2]+1), (cube[0], cube[1], cube[2]-1)}


def obsidian_surface(path):
    cubes = get_cubes(path)
    surface = 0
    for cube in cubes:
        neighbors = get_neighbors(cube)
        surface += 6 - len(cubes.intersection(neighbors))
    return surface


def get_bounds(lava):
    x_min = min(cube[0] for cube in lava)
    y_min = min(cube[1] for cube in lava)
    z_min = min(cube[2] for cube in lava)
    x_max = max(cube[0] for cube in lava)
    y_max = max(cube[1] for cube in lava)
    z_max = max(cube[2] for cube in lava)
    return x_min, x_max, y_min, y_max, z_min, z_max


def initial_water(x_min, x_max, y_min, y_max, z_min, z_max):
    water = set()
    for x in range(x_min-1, x_max+2):
        water.add((x, y_min, z_min))
        water.add((x, y_max, z_min))
        water.add((x, y_min, z_max))
        water.add((x, y_max, z_max))
    for y in range(y_min-1, y_max+2):
        water.add((x_min, y, z_min))
        water.add((x_max, y, z_min))
        water.add((x_min, y, z_max))
        water.add((x_max, y, z_max))
    for z in range(z_min-1, z_max+2):
        water.add((x_min, y_min, z))
        water.add((x_max, y_min, z))
        water.add((x_min, y_max, z))
        water.add((x_max, y_max, z))
    return water


def flood_fill(lava):
    bounds = get_bounds(lava)
    water = initial_water(*bounds)
    water_len = 0
    while len(water) != water_len:
        water_len = len(water)
        new_water = set()
        for cube in water:
            neighbors = get_neighbors(cube)
            for neighbor in neighbors:
                in_x = bounds[0]-1 <= neighbor[0] <= bounds[1]+1
                in_y = bounds[2]-1 <= neighbor[1] <= bounds[3]+1
                in_z = bounds[4]-1 <= neighbor[2] <= bounds[5]+1
                in_lava = True if neighbor in lava else False
                if in_x and in_y and in_z and not in_lava:
                    new_water.add(neighbor)
        water.update(new_water)
    return water


def obsidian_exterior_surface(path):
    lava = get_cubes(path)
    water = flood_fill(lava)
    surface = 0
    for cube in lava:
        neighbors = get_neighbors(cube)
        for neighbor in neighbors:
            if neighbor in water:
                surface += 1
    return surface
