import re
from collections import defaultdict

from d15 import pos

SAND_POS = pos(500, 0)


def simulate_drop(field, start_pos, max_y):
    done = False
    cur_pos = start_pos
    while not done:
        if field[pos(cur_pos.x, cur_pos.y + 1)] == '.':
            cur_pos = pos(cur_pos.x, cur_pos.y + 1)
        elif field[pos(cur_pos.x - 1, cur_pos.y + 1)] == '.':
            cur_pos = pos(cur_pos.x - 1, cur_pos.y + 1)
        elif field[pos(cur_pos.x + 1, cur_pos.y + 1)] == '.':
            cur_pos = pos(cur_pos.x + 1, cur_pos.y + 1)
        else:
            field[cur_pos] = 'o'
            done = True
        
        if cur_pos.y > max_y + 5:
            return True
        
        if field[SAND_POS] == 'o':
            return True
    
    return False


def get_field(inp):
    field = defaultdict(lambda: '.')
    field[SAND_POS] = '+'
    
    for line in inp:
        coords = [pos(*map(int, pair.split(','))) for pair in re.findall(r"\d+,\d+", line)]
        for i in range(len(coords) - 1):
            cur = coords[i]
            nxt = coords[i + 1]
            for x in range(min(cur.x, nxt.x), max(cur.x, nxt.x) + 1):
                field[pos(x, cur.y)] = '#'
            
            for y in range(min(cur.y, nxt.y), max(cur.y, nxt.y) + 1):
                field[pos(cur.x, y)] = '#'
    
    return field


def get_sand_count(field):
    return len(list(filter(lambda space: space == 'o', field.values())))


def part_one(inp):
    field = get_field(inp)
    max_y = max(field.keys(), key=lambda pair: pair.y).y
    
    done = False
    while not done:
        done = simulate_drop(field, SAND_POS, max_y)
    
    return get_sand_count(field)


def part_two(inp):
    field = get_field(inp)
    max_y = max(field.keys(), key=lambda pair: pair.y).y
    
    floor_level = max_y + 2
    for x in range(-floor_level, floor_level + 1):
        field[pos(SAND_POS.x + x, floor_level)] = '#'
    
    done = False
    while not done:
        done = simulate_drop(field, SAND_POS, max_y)
    
    return get_sand_count(field)


def main():
    with open(r'd14_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
