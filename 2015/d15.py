import numpy as np


def part_one(inp):
    ingredients = parse_inp(inp)
    scores = set()
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                totals = a * ingredients[0] + b * ingredients[1] + c * ingredients[2] + d * ingredients[3]
                if np.any(totals < 0):
                    continue
                scores.add(totals[0] * totals[1] * totals[2] * totals[3])
    return max(scores)


def part_two(inp):
    ingredients = parse_inp(inp)
    scores = set()
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                totals = a * ingredients[0] + b * ingredients[1] + c * ingredients[2] + d * ingredients[3]
                if np.any(totals < 0) or totals[-1] != 500:
                    continue
                scores.add(totals[0] * totals[1] * totals[2] * totals[3])
    return max(scores)


def parse_inp(inp):
    ingredients = []
    for line in inp:
        tmp = line.split()
        others = np.array([int(tmp[2][:-1]), int(tmp[4][:-1]), int(tmp[6][:-1]), int(tmp[8][:-1]), int(tmp[10])])
        ingredients.append(others)
    return ingredients


def main():
    with open('d15_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
