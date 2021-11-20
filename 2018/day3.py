import re
from collections import defaultdict


def part_one(inp):
    claims = defaultdict(int)
    for ind, x, y, w, h in inp:
        for i in range(w):
            for j in range(h):
                claims[(x + i, y + j)] += 1
        
    return len([i for i in claims.values() if i > 1])


def part_two(inp):
    variants = defaultdict(set)
    claims = defaultdict(int)
    for ind, x, y, w, h in inp:
        for i in range(w):
            for j in range(h):
                claims[(x + i, y + j)] += 1
                variants[ind].add((x + i, y + j))
                
    for k, v in variants.items():
        if all(map(lambda a: claims[a] == 1, v)):
            return k


def main():
    with open(r'input\day3.txt') as fin:
        inp = fin.read().splitlines()

    inp = [tuple(map(int, re.findall(r'\d+', line))) for line in inp]
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
