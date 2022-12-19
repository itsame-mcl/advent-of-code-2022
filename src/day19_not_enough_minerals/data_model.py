from enum import Enum
from dataclasses import dataclass, field
from functools import total_ordering


class Robot(Enum):
    ORE = 'ore'
    CLAY = 'clay'
    OBSIDIAN = 'obsidian'
    GEODE = 'geode'


@dataclass
class Blueprint:
    id: int
    ore_for_ore_robot: int
    ore_for_clay_robot: int
    ore_for_obsidian_robot: int
    clay_for_obsidian_robot: int
    ore_for_geode_robot: int
    obsidian_for_geode_robot: int
    max_ore_cost: int = field(init=False)

    def __post_init__(self):
        self.max_ore_cost = max(self.ore_for_ore_robot, self.ore_for_clay_robot, self.ore_for_obsidian_robot,
                                self.ore_for_geode_robot)


@dataclass
@total_ordering
class Inventory:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0
    ore_robot: int = 1
    clay_robot: int = 0
    obsidian_robot: int = 0
    geode_robot: int = 0

    def can_afford(self, blueprint: Blueprint):
        affordable = []
        if self.ore >= blueprint.ore_for_geode_robot and self.obsidian >= blueprint.obsidian_for_geode_robot:
            affordable.append(Robot.GEODE)
        if self.ore >= blueprint.ore_for_obsidian_robot and self.clay >= blueprint.clay_for_obsidian_robot:
            affordable.append(Robot.OBSIDIAN)
        if self.ore >= blueprint.ore_for_clay_robot:
            affordable.append(Robot.CLAY)
        if self.ore >= blueprint.ore_for_ore_robot:
            affordable.append(Robot.ORE)
        affordable.append(None)
        return affordable

    def buy_robot(self, robot_type: Robot, blueprint: Blueprint):
        match robot_type:
            case Robot.ORE:
                self.ore -= blueprint.ore_for_ore_robot
                self.ore_robot += 1
            case Robot.CLAY:
                self.ore -= blueprint.ore_for_clay_robot
                self.clay_robot += 1
            case Robot.OBSIDIAN:
                self.ore -= blueprint.ore_for_obsidian_robot
                self.clay -= blueprint.clay_for_obsidian_robot
                self.obsidian_robot += 1
            case Robot.GEODE:
                self.ore -= blueprint.ore_for_obsidian_robot
                self.obsidian -= blueprint.obsidian_for_geode_robot
                self.geode_robot += 1

    def collect_minerals(self):
        self.ore += self.ore_robot
        self.clay += self.clay_robot
        self.obsidian += self.obsidian_robot
        self.geode += self.geode_robot

    def __lt__(self, other):
        le_ore_robot = self.ore_robot <= other.ore_robot
        le_clay_robot = self.clay_robot <= other.clay_robot
        le_obsidian_robot = self.obsidian_robot <= other.obsidian_robot
        le_geode_robot = self.geode_robot <= other.geode_robot
        lt_ore = self.ore < other.ore
        lt_clay = self.clay < other.clay
        lt_obsidian = self.obsidian < other.obsidian
        lt_geode = self.geode < other.geode
        return all([le_ore_robot, le_clay_robot, le_obsidian_robot, le_geode_robot,
                    lt_ore, lt_clay, lt_obsidian, lt_geode])
