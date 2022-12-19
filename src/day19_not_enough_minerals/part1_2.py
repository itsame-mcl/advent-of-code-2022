from src.day19_not_enough_minerals.data_model import Robot, Blueprint, Inventory
from typing import List, Union
from copy import copy
from re import findall


def get_blueprints(path):
    blueprints = []
    with open(path) as file:
        for line in file:
            id_and_costs = list(map(lambda string: int(string), findall(r'\d+', line)))
            blueprints.append(Blueprint(*id_and_costs))
    return blueprints


def prune_options(inventory: Inventory, blueprint: Blueprint, options: List[Union[Robot, None]]) ->\
        List[Union[Robot, None]]:
    if Robot.GEODE in options:
        options = [Robot.GEODE]
    elif Robot.OBSIDIAN in options:
        options.remove(None)
        if Robot.ORE in options:
            options.remove(Robot.ORE)
    if inventory.obsidian_robot >= blueprint.obsidian_for_geode_robot and Robot.OBSIDIAN in options:
        options.remove(Robot.OBSIDIAN)
    if inventory.clay_robot >= blueprint.clay_for_obsidian_robot and Robot.CLAY in options:
        options.remove(Robot.CLAY)
    if inventory.ore_robot >= blueprint.max_ore_cost and Robot.ORE in options:
        options.remove(Robot.ORE)
    if inventory.ore >= blueprint.max_ore_cost and None in options:
        # noinspection PyTypeChecker
        options.remove(None)
    return options


def maximize_geodes(inventory: Inventory, blueprint: Blueprint, minutes_left, skipped=None, current_max=0):
    if skipped is None:
        skipped = []
    max_geodes = inventory.geode
    upper_geodes_bound = inventory.geode + inventory.geode_robot * minutes_left + minutes_left*(minutes_left+1)/2
    if upper_geodes_bound < current_max:
        return 0
    if minutes_left > 0:
        options = prune_options(inventory, blueprint, inventory.can_afford(blueprint))
        for options_skipped in skipped:
            options.remove(options_skipped)
        inventory.collect_minerals()
        for option in options:
            new_inventory = copy(inventory)
            if option is not None:
                new_inventory.buy_robot(option, blueprint)
            else:
                skipped = options[:].remove(None)
            final_geodes_with_buy = maximize_geodes(new_inventory, blueprint, minutes_left-1, skipped, max_geodes)
            if final_geodes_with_buy > max_geodes:
                max_geodes = final_geodes_with_buy
    return max_geodes


def maximize_for_all_blueprints(path, slicing=None, depth=24):
    blueprints = get_blueprints(path)
    outcome = 1 if slicing is not None else 0
    slicing_param = min(len(blueprints), slicing if slicing is not None else len(blueprints))
    for blueprint in blueprints[:slicing_param]:
        start = Inventory()
        result = maximize_geodes(start, blueprint, depth)
        if slicing is None:
            outcome += blueprint.id * result
        else:
            outcome *= result
    return outcome
