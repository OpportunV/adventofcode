from collections import defaultdict


def part_one(field):
    states = set()
    while True:
        state = tuple(tuple(i) for i in field)
        if state in states:
            total = 0
            for i in range(len(field)):
                for j in range(len(field[0])):
                    if field[i][j] == '#':
                        total += 2 ** (i * len(field) + j)
            return total
        states.add(state)
        tmp = [['.' for _ in range(len(field))] for _ in range(len(field[0]))]
        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == '#' and sum(adjacent((i, j), field)) == 1:
                    tmp[i][j] = '#'
                if field[i][j] == '.' and 1 <= sum(adjacent((i, j), field)) <= 2:
                    tmp[i][j] = '#'
        
        field = tmp


def part_two(field):
    levels = 100
    
    connections = defaultdict(list)
    cells = {}
    for i in range(len(field)):
        for j in range(len(field[0])):
            if i == 2 and j == 2:
                continue
            for level in range(-levels, levels + 1):
                cells[(i, j, level)] = False
                if level == 0 and field[i][j] == '#':
                    cells[(i, j, level)] = True
                for x, y in adj((i, j)):
                    if 0 <= x < len(field) and 0 <= y < len(field[0]) and (x, y) != (2, 2):
                        connections[(i, j, level)].append((x, y, level))
                if i == 0 and level - 1 >= -levels:
                    connections[(i, j, level)].append((1, 2, level - 1))
                if j == 0 and level - 1 >= -levels:
                    connections[(i, j, level)].append((2, 1, level - 1))
                if j == len(field[0]) - 1 and level - 1 >= -levels:
                    connections[(i, j, level)].append((2, 3, level - 1))
                if i == len(field) - 1 and level - 1 >= -levels:
                    connections[(i, j, level)].append((3, 2, level - 1))
                if i == 1 and j == 2 and level + 1 <= levels:
                    for y in range(5):
                        connections[(i, j, level)].append((0, y, level + 1))
                if i == 2 and j == 1 and level + 1 <= levels:
                    for x in range(5):
                        connections[(i, j, level)].append((x, 0, level + 1))
                if i == 2 and j == 3 and level + 1 <= levels:
                    for x in range(5):
                        connections[(i, j, level)].append((x, len(field[0]) - 1, level + 1))
                if i == 3 and j == 2 and level + 1 <= levels:
                    for y in range(5):
                        connections[(i, j, level)].append((len(field) - 1, y, level + 1))
    
    for _ in range(200):
        tmp = {}
        for k, v in cells.items():
            alive = 0
            for y in connections[k]:
                if cells[y]:
                    alive += 1
            if (cells[k] and alive != 1) or (not cells[k] and alive not in [1, 2]):
                tmp[k] = False
            else:
                tmp[k] = True
        cells = tmp

    return sum(cells.values())


def adjacent(pos, field):
    x, y = pos
    a = field[x][y + 1] if y + 1 < len(field[0]) else '.'
    yield 1 if a == '#' else 0
    a = field[x][y - 1] if 0 < y else '.'
    yield 1 if a == '#' else 0
    a = field[x + 1][y] if x + 1 < len(field) else '.'
    yield 1 if a == '#' else 0
    a = field[x - 1][y] if 0 < x else '.'
    yield 1 if a == '#' else 0


def adj(pos):
    yield pos[0] + 1, pos[1]
    yield pos[0] - 1, pos[1]
    yield pos[0], pos[1] + 1
    yield pos[0], pos[1] - 1


def main():
    with open('d24_input.txt') as fin:
        inp = fin.read().splitlines()
    
    field = [list(i) for i in inp]
    
    # print(part_one(field))
    print(part_two(field))


if __name__ == '__main__':
    main()
