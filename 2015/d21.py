from itertools import combinations


def part_one(inp, boss):
    weapons, armor, rings = parse_shop(inp)
    total = set()
    player = {}
    for weapon in weapons:
        for arm in armor:
            for rngs in combinations(rings, 2):
                player['dmg'] = weapon[1] + rngs[0][1] + rngs[1][1]
                player['arm'] = arm[2] + rngs[0][2] + rngs[1][2]
                player['HP'] = 100
                if simulate(boss.copy(), player):
                    total.add(weapon[0] + arm[0] + rngs[0][0] + rngs[1][0])
    
    return min(total)


def part_two(inp, boss):
    weapons, armor, rings = parse_shop(inp)
    total = set()
    player = {}
    for weapon in weapons:
        for arm in armor:
            for rngs in combinations(rings, 2):
                player['dmg'] = weapon[1] + rngs[0][1] + rngs[1][1]
                player['arm'] = arm[2] + rngs[0][2] + rngs[1][2]
                player['HP'] = 100
                if not simulate(boss.copy(), player):
                    total.add(weapon[0] + arm[0] + rngs[0][0] + rngs[1][0])
    
    return max(total)


def parse_shop(inp):
    weapons = set()
    armor = set()
    rings = set()
    for line in inp:
        if line:
            if ':' in line:
                current = line.split(':')[0].lower()
            else:
                tmp = line.split()
                eval(current).add(tuple(int(i) for i in tmp[-3:]))
    armor.add((0, 0, 0))
    rings.add((0, 0, 0))
    return weapons, armor, rings


def simulate(boss, player):
    while True:
        boss['HP'] -= max(1, player['dmg'] - boss['arm'])
        if boss['HP'] <= 0:
            return True
        player['HP'] -= max(1, boss['dmg'] - player['arm'])
        if player['HP'] <= 0:
            return False
    

def main():
    with open('d21_input.txt') as fin:
        inp = fin.read().splitlines()

    boss = {
        'HP': 103,
        'dmg': 9,
        'arm': 2
    }
    
    print(part_one(inp, boss))
    print(part_two(inp, boss))
    
    
if __name__ == '__main__':
    main()

