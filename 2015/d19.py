import re
from collections import defaultdict


def part_one(inp):
    reactions = defaultdict(list)
    for line in inp:
        if '=>' in line:
            tmp = line.split('=>')
            reactions[tmp[0].strip()].append(tmp[1].strip())
    molecule = inp[-1]
    produces = set()
    for reagent, products in reactions.items():
        for product in products:
            for i in range(0, molecule.count(reagent)):
                cur = replace_at_pos(molecule, reagent, product, i)
                produces.add(cur)
    return len(produces)


def part_two(inp):
    reactions = {}
    for line in inp:
        if '=>' in line:
            tmp = line.split('=>')
            reactions[tmp[1].strip()] = tmp[0].strip()
    keys = sorted(reactions, key=lambda x: -len(x))
    molecule = inp[-1]
    total = 0
    while molecule != 'e':
        for key in keys:
            if key in molecule:
                molecule = molecule.replace(key, reactions[key], 1)
                total += 1
    return total


def replace_at_pos(string, sub, new, pos):
    where = [m.start() for m in re.finditer(sub, string)][pos - 1]
    left = string[:where]
    right = string[where:].replace(sub, new, 1)
    return left + right


def main():
    with open('d19_input.txt') as fin:
        inp = fin.read().splitlines()
        
#     inp = '''H => HO
# H => OH
# O => HH
#
# HOH'''.splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
