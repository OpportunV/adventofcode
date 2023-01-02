from d14 import get_field, SAND_POS, pos, part_one as pt_one

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


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
    
    return cur_pos


def part_one(inp):
    field = get_field(inp)
    min_x = min(field.keys(), key=lambda pair: pair.x).x
    max_x = max(field.keys(), key=lambda pair: pair.x).x
    min_y = min(field.keys(), key=lambda pair: pair.y).y
    max_y = max(field.keys(), key=lambda pair: pair.y).y
    print(min_x, max_x, min_y, max_y)
    
    dx = max_x - min_x + 30
    matrix = np.zeros((max_y - min_y + 5, dx), dtype=int)
    
    def get_x_pos(xx):
        return (xx - SAND_POS.x - 25) % dx
    
    def fill():
        for (xx, yy) in field.keys():
            if field[(xx, yy)] == '#':
                matrix[yy, get_x_pos(xx)] = 4
            if field[(xx, yy)] == 'o':
                matrix[yy, get_x_pos(xx)] = 2
            if field[(xx, yy)] == '+':
                matrix[yy, get_x_pos(xx)] = 1
    
    fill()
    matplotlib.use('TkAgg')
    fig = plt.figure(1, (6, 3), dpi=400)
    img = plt.imshow(matrix, interpolation='none')
    plt.axis(False)
    
    def animate(cur):
        cur_pos = simulate_drop(field, SAND_POS, max_y)
        print(cur)
        if isinstance(cur_pos, bool):
            print(cur)
            return
        
        matrix[cur_pos.y, get_x_pos(cur_pos.x)] = 2
        img.set_data(matrix)
        return img,
    
    ani = animation.FuncAnimation(fig, animate, interval=1, frames=pt_one(inp), repeat=False)
    # writer = animation.FFMpegFileWriter(fps=60)
    # ani.save('d14_visual.mp4', writer=writer)
    plt.show()


def main():
    with open(r'd14_input.txt') as fin:
        inp = fin.read().splitlines()
    
    part_one(inp)


if __name__ == '__main__':
    main()
