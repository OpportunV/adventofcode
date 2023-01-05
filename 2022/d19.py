import multiprocessing
import re
from collections import defaultdict
from copy import deepcopy
from functools import reduce

from typing import Dict

END_TIME = 32


class ResourceType:
    ORE = 'ore'
    CLAY = 'clay'
    OBSIDIAN = 'obsidian'
    GEODE = 'geode'
    ALL = ['geode', 'obsidian', 'clay', 'ore']


class Game:
    AVAILABLE_ROBOTS: Dict[str, Dict[str, int]]
    MAX: Dict[int, Dict[str, int]] = defaultdict(dict)
    MAX_GEODES: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
    
    def __init__(self, id_, start=0, robots=None, resources=None, to_skip=None):
        self.id = id_
        self.robots = {
            ResourceType.ORE: 1,
            ResourceType.CLAY: 0,
            ResourceType.OBSIDIAN: 0,
            ResourceType.GEODE: 0,
        } if robots is None else deepcopy(robots)
        
        self.resources = {
            ResourceType.ORE: 0,
            ResourceType.CLAY: 0,
            ResourceType.OBSIDIAN: 0,
            ResourceType.GEODE: 0,
        } if resources is None else deepcopy(resources)
        
        self.to_skip = set() if to_skip is None else deepcopy(to_skip)
        self.time = start
    
    def simulate(self):
        if Game.MAX_GEODES[self.id][self.time] > self.resources[ResourceType.GEODE]:
            return self.resources[ResourceType.GEODE]
        
        Game.MAX_GEODES[self.id][self.time] = self.resources[ResourceType.GEODE]
        
        if self.time == END_TIME - 1:
            self.gather_resources()
            return self.resources[ResourceType.GEODE]
        
        geodes = []
        options = self.get_build_options()
        self.gather_resources()
        robots = deepcopy(self.robots)
        resources = deepcopy(self.resources)
        game = Game(self.id, self.time + 1, robots, resources, set(options))
        geodes.append(game.simulate())
        for option in options:
            robots = deepcopy(self.robots)
            resources = deepcopy(self.resources)
            if option is not None:
                robots[option] += 1
                current_robot = Game.AVAILABLE_ROBOTS[option]
                for res_type in ResourceType.ALL:
                    resources[res_type] -= current_robot[res_type]
            
            game = Game(self.id, self.time + 1, robots, resources)
            geodes.append(game.simulate())
        
        return max(geodes)
    
    def gather_resources(self):
        self.resources[ResourceType.ORE] += self.robots[ResourceType.ORE]
        self.resources[ResourceType.CLAY] += self.robots[ResourceType.CLAY]
        self.resources[ResourceType.OBSIDIAN] += self.robots[ResourceType.OBSIDIAN]
        self.resources[ResourceType.GEODE] += self.robots[ResourceType.GEODE]
    
    def get_build_options(self):
        options = []
        for resource_type in ResourceType.ALL:
            robot = Game.AVAILABLE_ROBOTS[resource_type]
            can_build = False
            
            if self.robots[resource_type] < Game.MAX[self.id][resource_type] \
                    and all([self.resources[res_type] >= robot[res_type] for res_type in ResourceType.ALL]) \
                    and resource_type not in self.to_skip:
                can_build = True
            
            if can_build:
                options.append(resource_type)
        
        if ResourceType.GEODE in options:
            options = [ResourceType.GEODE]
        
        if ((self.robots[ResourceType.CLAY] > 3 or self.robots[ResourceType.OBSIDIAN] > 0
             or ResourceType.OBSIDIAN in options) and ResourceType.ORE in options):
            options.remove(ResourceType.ORE)
        
        if ((self.robots[ResourceType.OBSIDIAN] > 3 or self.robots[ResourceType.GEODE] > 0)
                and ResourceType.CLAY in options):
            options.remove(ResourceType.CLAY)
        
        return options


def get_blueprint_quality_level(blueprint):
    costs = list(map(int, re.findall(r'\d+', blueprint)))
    available_robots = {
        ResourceType.ORE: defaultdict(int, {ResourceType.ORE: costs[1]}),
        ResourceType.CLAY: defaultdict(int, {ResourceType.ORE: costs[2]}),
        ResourceType.OBSIDIAN: defaultdict(int, {ResourceType.ORE: costs[3], ResourceType.CLAY: costs[4]}),
        ResourceType.GEODE: defaultdict(int, {ResourceType.ORE: costs[5], ResourceType.OBSIDIAN: costs[6]}),
    }
    Game.AVAILABLE_ROBOTS = available_robots
    Game.MAX[costs[0]] = {
        ResourceType.ORE: max(available_robots[ResourceType.CLAY][ResourceType.ORE],
                              available_robots[ResourceType.OBSIDIAN][ResourceType.ORE],
                              available_robots[ResourceType.GEODE][ResourceType.ORE]),
        ResourceType.CLAY: available_robots[ResourceType.OBSIDIAN][ResourceType.CLAY],
        ResourceType.OBSIDIAN: available_robots[ResourceType.GEODE][ResourceType.OBSIDIAN],
        ResourceType.GEODE: float("inf")
    }
    Game.MAX_GEODES[costs[0]] = defaultdict(int)
    game = Game(costs[0])
    geodes = game.simulate()
    return costs[0], geodes


def part_one(inp):
    pool = multiprocessing.Pool(processes=6)
    outputs = pool.map(get_blueprint_quality_level, inp)
    return sum([a * b for a, b in outputs])


def part_two(inp):
    pool = multiprocessing.Pool(processes=3)
    outputs = pool.map(get_blueprint_quality_level, inp[:3])
    return reduce(lambda x, total: x * total, outputs)


def main():
    with open(r'd19_input.txt') as fin:
        inp = fin.read().splitlines()
    
    # print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
