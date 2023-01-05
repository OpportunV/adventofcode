import re
from collections import defaultdict


class Cave:
    __slots__ = ('rates', 'paths', 'distances', 'results', 'valve_to_bits')
    
    def __init__(self, inp):
        self.rates = {}
        self.paths = {}
        self.valve_to_bits = {}
        self.distances = defaultdict(lambda: int(1e5))
        self.results = defaultdict(int)
        self.parse(inp)
        for valve, others in self.paths.items():
            for other in others:
                self.distances[valve, other] = 1
        
        for i in self.paths:
            for j in self.paths:
                for k in self.paths:
                    self.distances[j, k] = min(self.distances[j, k], self.distances[i, j] + self.distances[i, k])
        
        for i, valve in enumerate(self.paths):
            self.valve_to_bits[valve] = 1 << i
    
    def parse(self, inp):
        for line in inp:
            cur, *others = re.findall(r'[A-Z]{2}', line)
            rate = int(re.findall(r'\d+', line)[0])
            self.paths[cur] = others
            self.rates[cur] = rate
    
    def walk(self, current_valve, time_left, pressure, opened):
        self.results[opened] = max(self.results[opened], pressure)
        
        for other_valve, rate in self.rates.items():
            if rate == 0:
                continue
            
            new_time = time_left - self.distances[current_valve, other_valve] - 1
            if self.valve_to_bits[other_valve] & opened or new_time <= 0:
                continue
            
            self.walk(other_valve, new_time, pressure + rate * new_time, opened | self.valve_to_bits[other_valve])


def part_one(inp):
    cave = Cave(inp)
    cave.walk('AA', 30, 0, 0)
    return max(cave.results.values())


def part_two(inp):
    cave = Cave(inp)
    cave.walk('AA', 26, 0, 0)
    
    max_pressure = 0
    for opened1, pressure1 in cave.results.items():
        for opened2, pressure2 in cave.results.items():
            if opened1 & opened2 == 0:
                max_pressure = max(max_pressure, pressure1 + pressure2)
        
    return max_pressure


def main():
    with open(r'd16_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
