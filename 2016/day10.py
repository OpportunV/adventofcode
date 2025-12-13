from collections import defaultdict, deque

import aoc


def part_both(inp):
    inventories = defaultdict(list)
    moves = {}
    for line in inp:
        if 'value' in line:
            val, bot = aoc.get_nums(line)
            inventories[f'bot {bot}'].append(val)
        else:
            split = line.split()
            moves[f'{split[0]} {split[1]}'] = (f'{split[5]} {split[6]}', f'{split[10]} {split[11]}')

    to_visit = deque()
    for owner, values in inventories.items():
        if len(values) == 2:
            to_visit.append(owner)

    while to_visit:
        cur = to_visit.popleft()
        values = inventories[cur]
        low, high = sorted(values)
        if low == 17 and high == 61:
            print(cur)

        low_to, high_to = moves[cur]
        inventories[low_to].append(low)
        inventories[high_to].append(high)
        if len(inventories[low_to]) == 2:
            to_visit.append(low_to)
        if len(inventories[high_to]) == 2:
            to_visit.append(high_to)

    return inventories['output 0'][0] * inventories['output 1'][0] * inventories['output 2'][0]


def main():
    with open('input/day10.txt') as fin:
        inp = fin.read().splitlines()

    print(part_both(inp))


if __name__ == '__main__':
    main()
