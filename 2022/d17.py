from collections import defaultdict, namedtuple
from itertools import cycle

import numpy as np

Shape = namedtuple('shape', ['pattern', 'width', 'height'])

SHAPES = [
    Shape([['#', '#', '#', '#']], 4, 1),
    
    Shape([['.', '#', '.'],
           ['#', '#', '#'],
           ['.', '#', '.']], 3, 3),
    
    Shape([['.', '.', '#'],
           ['.', '.', '#'],
           ['#', '#', '#']], 3, 3),
    
    Shape([['#'],
           ['#'],
           ['#'],
           ['#']], 1, 4),
    
    Shape([['#', '#'],
           ['#', '#']], 2, 2)
]


def add_current(x, y, shape, field, char=None):
    for i in range(shape.width):
        for j in range(shape.height):
            if shape.pattern[j][i] == '#':
                field[x + i, y - j] = shape.pattern[j][i] if char is None else char


def check_move(x, y, shape, field):
    for i in range(shape.width):
        for j in range(shape.height):
            if field[x + i, y - j] == '#' and shape.pattern[j][i] == '#':
                return False
    
    return True


def part_one(inp):
    n_iter = 2022
    moves = cycle(inp[0])
    shapes = cycle(SHAPES)
    field = defaultdict(lambda: '.')
    field_width = 7
    cur_field_height = 0
    
    for i in range(field_width):
        field[i, -1] = '#'
    
    def step(n):
        shape = next(shapes)
        nonlocal cur_field_height
        x, y = 2, cur_field_height + 2 + shape.height
        can_fall = True
        while can_fall:
            move = 1 if next(moves) == '>' else -1
            if x + shape.width + move <= field_width and x + move >= 0 and check_move(x + move, y, shape, field):
                x += move
            
            can_fall = check_move(x, y - 1, shape, field)
            
            if not can_fall:
                cur_field_height = max(y + 1, cur_field_height)
                add_current(x, y, shape, field)
            else:
                y -= 1
    
    for i in range(n_iter):
        step(i)
    
    return cur_field_height


def part_two(inp):
    target_iter = 1_000_000_000_000
    n_iter = 1_000_000
    moves = cycle(inp[0])
    shapes = cycle(SHAPES)
    field = defaultdict(lambda: '.')
    heights = []
    field_width = 7
    cur_field_height = 0
    
    for i in range(field_width):
        field[i, -1] = '#'
    
    def step(n):
        shape = next(shapes)
        nonlocal cur_field_height
        x, y = 2, cur_field_height + 2 + shape.height
        can_fall = True
        while can_fall:
            move = 1 if next(moves) == '>' else -1
            if x + shape.width + move <= field_width and x + move >= 0 and check_move(x + move, y, shape, field):
                x += move
            
            can_fall = check_move(x, y - 1, shape, field)
            
            if not can_fall:
                cur_field_height = max(y + 1, cur_field_height)
                add_current(x, y, shape, field)
                heights.append(cur_field_height)
            else:
                y -= 1
            
            for h in range(cur_field_height, cur_field_height + 4):
                line = True
                for i in range(field_width):
                    if field[i, cur_field_height + h] == '.':
                        line = False
                        
                if line:
                    print(n, shape.pattern, move)
                    
    for i in range(n_iter):
        step(i)
    
    a, b, *_ = np.polyfit(np.arange(len(heights)), heights, 1)
    
    heights = np.array(heights)
    calc_heights = np.array([a * x + b for x in range(len(heights))])
    diff = heights - calc_heights
    diff = np.round(diff, 3)
    first = np.argmax(diff)
    period = np.argmax(diff[first + 1:]) + 1
    a, b, *_ = np.polyfit(np.arange(len(heights))[first: 10*first:period], heights[first: 10*first:period], 1)

    return ((target_iter - first) // period) \
        * (heights[first + period] - heights[first]) + heights[first + (target_iter - first) % period] - 1


def main():
    with open(r'd17_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
