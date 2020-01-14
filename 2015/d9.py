from collections import defaultdict
from itertools import permutations


def part_one(inp):
    flights, cities = parse_inp(inp)
    paths = set()
    for path in permutations(cities):
        paths.add(sum(map(lambda x, y: flights[x][y], path[:-1], path[1:])))
    return min(paths)


def part_two(inp):
    flights, cities = parse_inp(inp)
    paths = set()
    for path in permutations(cities):
        paths.add(sum(map(lambda x, y: flights[x][y], path[:-1], path[1:])))
    return max(paths)


def parse_inp(inp):
    flights = defaultdict(dict)
    cities = set()
    for line in inp:
        origin, _, destination, _, dist = line.split()
        cities.add(origin)
        cities.add(destination)
        dist = int(dist)
        flights[origin][destination] = dist
        flights[destination][origin] = dist
    
    return flights, cities


def main():
    with open('d9_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
