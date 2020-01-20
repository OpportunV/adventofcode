from collections import defaultdict
from itertools import permutations


def part_one(inp):
    connections = parse_inp(inp)
    return max({sum(map(lambda x, y: connections[x][y] + connections[y][x], names, names[1:] + (names[0],)))
               for names in permutations(connections.keys())})


def part_two(inp):
    connections = parse_inp(inp)
    for name in connections:
        connections[name]['Me'] = 0
    connections['Me'] = {name: 0 for name in connections.keys()}

    return max({sum(map(lambda x, y: connections[x][y] + connections[y][x], names, names[1:] + (names[0],)))
                for names in permutations(connections.keys())})


def parse_inp(inp):
    connections = defaultdict(dict)
    
    for line in inp:
        tmp = line.split()
        name1, name2, amount = tmp[0], tmp[-1][:-1], int(tmp[3])
        connections[name1][name2] = amount if tmp[2] == 'gain' else - amount
    return connections
    

def main():
    with open('d13_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
