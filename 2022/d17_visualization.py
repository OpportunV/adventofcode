from collections import defaultdict
from itertools import cycle

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from d17 import add_current, check_move, SHAPES


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
            if x + shape.width + move <= field_width and x + move >= 0 and check_move(x, y, shape, field):
                x += move
            
            can_fall = check_move(x, y - 1, shape, field)
            
            if not can_fall:
                cur_field_height = max(y + 1, cur_field_height)
                add_current(x, y, shape, field)
                return x, y, shape
            else:
                y -= 1
    
    matplotlib.use('TkAgg')
    fig = plt.figure(1, (1, 2), dpi=600)
    matrix = np.zeros((3400, field_width), dtype=int)
    matrix[-1, -1] = 10
    img = plt.imshow(matrix, interpolation='none')
    plt.axis(False)
    colors = cycle(list(range(1, 10)))
    
    def animate(cur):
        x, y, shape = step(cur)
        color = next(colors)
        for i in range(shape.width):
            for j in range(shape.height):
                if shape.pattern[j][i] == '#':
                    matrix[y - j, x + i] = color
        
        img.set_data(np.flip(matrix, 0))
        return img,
    
    ani = animation.FuncAnimation(fig, animate, interval=1, frames=n_iter, repeat=False)
    # writer = animation.FFMpegFileWriter(fps=30)
    # ani.save('d9_visual.mp4', writer=writer)
    plt.show()


def main():
    with open(r'd17_input.txt') as fin:
        inp = fin.read().splitlines()
    part_one(inp)


if __name__ == '__main__':
    main()
