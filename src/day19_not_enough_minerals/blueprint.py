from enum import Enum
from dataclasses import dataclass


@dataclass
class Blueprint:
    id: int
    ore_for_ore_robot: int
    ore_for_clay_robot: int
    ore_for_obsidian_robot: int
    clay_for_obsidian_robot: int
    ore_for_geode_robot: int
    obsidian_for_geode_robot: int
