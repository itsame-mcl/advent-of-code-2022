from src.day19_not_enough_minerals.blueprint import Blueprint
from re import findall
from z3 import IntVector, Optimize, And


def get_blueprints(path):
    blueprints = []
    with open(path) as file:
        for line in file:
            id_and_costs = list(map(lambda string: int(string), findall(r'\d+', line)))
            blueprints.append(Blueprint(*id_and_costs))
    return blueprints


def solve_optimization_problem(blueprint: Blueprint, n):
    solver = Optimize()  # Z3 Optimize solver object
    # Z3 variables vectors
    ore, clay, obsidian, geode = IntVector("ore", n+1),  IntVector("clay", n+1), IntVector("obsidian", n+1),\
        IntVector("geode", n+1)
    ore_robots, clay_robots, obsidian_robots, geode_robots = IntVector("ore_robots", n+1),\
        IntVector("clay_robots", n+1), IntVector("obsidian_robots", n+1), IntVector("geode_robots", n+1)
    new_ore_robots, new_clay_robots, new_obsidian_robots, new_geode_robots = IntVector("new_ore_robots", n+1),\
        IntVector("new_clay_robots", n+1), IntVector("new_obsidian_robots", n+1), IntVector("new_geode_robots", n+1)
    # Initial state
    solver.add(And(ore[0] == 0, clay[0] == 0, obsidian[0] == 0, geode[0] == 0))
    solver.add(And(ore_robots[0] == 1, clay_robots[0] == 0, obsidian_robots[0] == 0, geode_robots[0] == 0))
    solver.add(And(new_ore_robots[0] == 0, new_clay_robots[0] == 0, new_obsidian_robots[0] == 0,
                   new_geode_robots[0] == 0))
    # Equations for each minute
    for t in range(1, n + 1):
        # Resources generation and consumption
        solver.add(ore[t] == ore[t-1] + ore_robots[t-1] - new_ore_robots[t-1] * blueprint.ore_for_ore_robot -
                   new_clay_robots[t-1] * blueprint.ore_for_clay_robot - new_obsidian_robots[t-1] *
                   blueprint.ore_for_obsidian_robot - new_geode_robots[t-1] * blueprint.ore_for_geode_robot)
        solver.add(clay[t] == clay[t-1] + clay_robots[t-1] - new_obsidian_robots[t-1] *
                   blueprint.clay_for_obsidian_robot)
        solver.add(obsidian[t] == obsidian[t-1] + obsidian_robots[t-1] - new_geode_robots[t-1] *
                   blueprint.obsidian_for_geode_robot)
        solver.add(geode[t] == geode[t-1] + geode_robots[t-1])
        # Robots fabrication
        solver.add(ore_robots[t] == ore_robots[t-1] + new_ore_robots[t-1])
        solver.add(clay_robots[t] == clay_robots[t-1] + new_clay_robots[t-1])
        solver.add(obsidian_robots[t] == obsidian_robots[t-1] + new_obsidian_robots[t-1])
        solver.add(geode_robots[t] == geode_robots[t-1] + new_geode_robots[t-1])
        # Buying constraints
        solver.add(new_ore_robots[t] * blueprint.ore_for_ore_robot <= ore[t])
        solver.add(new_clay_robots[t] * blueprint.ore_for_clay_robot <= ore[t])
        solver.add(new_obsidian_robots[t] * blueprint.ore_for_obsidian_robot <= ore[t])
        solver.add(new_geode_robots[t] * blueprint.ore_for_geode_robot <= ore[t])
        solver.add(new_obsidian_robots[t] * blueprint.clay_for_obsidian_robot <= clay[t])
        solver.add(new_geode_robots[t] * blueprint.obsidian_for_geode_robot <= obsidian[t])
        solver.add(And(0 <= new_ore_robots[t], new_ore_robots[t] <= 1))
        solver.add(And(0 <= new_clay_robots[t], new_clay_robots[t] <= 1))
        solver.add(And(0 <= new_obsidian_robots[t], new_obsidian_robots[t] <= 1))
        solver.add(And(0 <= new_geode_robots[t], new_geode_robots[t] <= 1))
        solver.add(new_ore_robots[t] + new_clay_robots[t] + new_obsidian_robots[t] + new_geode_robots[t] <= 1)
    solver.maximize(geode[n])
    solver.check()
    return solver.model()[geode[n]].as_long()


def maximize_for_all_blueprints(path, slicing=None, minutes=24):
    blueprints = get_blueprints(path)
    outcome = 1 if slicing is not None else 0
    slicing_param = min(len(blueprints), slicing if slicing is not None else len(blueprints))
    for blueprint in blueprints[:slicing_param]:
        result = solve_optimization_problem(blueprint, minutes)
        if slicing is None:
            outcome += blueprint.id * result
        else:
            outcome *= result
    return outcome
