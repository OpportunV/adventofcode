from collections import defaultdict, deque
from random import randint

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import numpy as np

from intcode_computer import IntcodeComputer


def get_full_map(intcode):
    """north (1), south (2), west (3), and east (4)
    -1: fog of war
    0: The repair droid hit a wall. Its position has not changed.
    1: The repair droid has moved one step in the requested direction.
    2: The repair droid has moved one step in the requested direction;
    its new position is the location of the oxygen system.
    4: oxygen
    5: start
"""
    comp = IntcodeComputer(0, intcode)
    size = 41
    field = np.zeros((size, size), dtype=int) - 1
    x, y = size // 2 + 1, size // 2 + 1
    
    done = False
    while not done:
        move = randint(1, 4)
        reply = comp.cor.send(move)
        next(comp.cor)
        prev_pos = x, y
        if move == 1:
            y -= 1
        if move == 2:
            y += 1
        if move == 3:
            x -= 1
        if move == 4:
            x += 1
        field[x][y] = reply
        if reply == 0:
            x, y = prev_pos
        
        xs, ys = np.where(field[1:-1, 1:-1] == -1)
        for x, y in zip(xs + 1, ys + 1):
            if not (field[x - 1, y] == 0
                    and field[x + 1, y] == 0
                    and field[x, y - 1] == 0
                    and field[x, y + 1] == 0):
                break
        else:
            with open('d15_output.txt', 'w') as fout:
                for line in field:
                    print(' '.join([str(i) for i in line]), file=fout)
            return


def draw_field(field):
    plt.figure()
    plt.imshow(field, interpolation='none')
    plt.axis('off')
    plt.show()


def part_one(field):
    xs, ys = np.where(field == 2)
    target = (xs[0], ys[0])
    start = len(field) // 2 + 1, len(field) // 2 + 1
    field[start] = 3
    path = defaultdict(lambda:float('inf'))
    path[start] = 0
    to_check = deque()
    to_check.append(start)
    fig, ax = plt.subplots()
    img = plt.imshow(field)
    plt.ion()
    plt.axis(False)
    plt.plot()
    while target not in path:
        current = to_check.popleft()
        x, y = current
        if field[x - 1, y] == 1 or field[x - 1, y] == 2:
            path[(x - 1, y)] = min(path[(x - 1, y)], path[current] + 1)
            field[x - 1, y] = 3
            to_check.append((x - 1, y))
        if field[x + 1, y] == 1 or field[x + 1, y] == 2:
            path[(x + 1, y)] = min(path[(x + 1, y)], path[current] + 1)
            field[x + 1, y] = 3
            to_check.append((x + 1, y))
        if field[x, y - 1] == 1 or field[x, y - 1] == 2:
            path[(x, y - 1)] = min(path[(x, y - 1)], path[current] + 1)
            field[x, y - 1] = 3
            to_check.append((x, y - 1))
        if field[x, y + 1] == 1 or field[x, y + 1] == 2:
            path[(x, y + 1)] = min(path[(x, y + 1)], path[current] + 1)
            field[x, y + 1] = 3
            to_check.append((x, y + 1))
        
        img.set_data(field)
        plt.pause(.001)
    return path[target]


def part_two(field):
    def spread_air(last):
        cur = []
        for x, y in last:
            if field[x - 1, y] == 1:
                field[x - 1, y] = 2
                cur.append((x - 1, y))
            if field[x + 1, y] == 1:
                field[x + 1, y] = 2
                cur.append((x + 1, y))
            if field[x, y - 1] == 1:
                field[x, y - 1] = 2
                cur.append((x, y - 1))
            if field[x, y + 1] == 1:
                field[x, y + 1] = 2
                cur.append((x, y + 1))
        
        return cur
    
    def update(frame):
        nonlocal time, last_added
        last_added = spread_air(last_added)
        time += 1
        img.set_data(field)
        return img
    
    time = 0
    xs, ys = np.where(field == 2)
    last_added = [(xs[0], ys[0])]
    fig, ax = plt.subplots()
    img = plt.imshow(field, interpolation='none')
    plt.axis('off')
    anim = FuncAnimation(fig, update, interval=1, frames=382)
    writer = FFMpegWriter(fps=60)
    plt.rcParams['animation.ffmpeg_path'] = r'D:\univ\Progin\ffmpeg\bin\ffmpeg.exe'
    # anim.save('anim.mp4', writer-writer)
    plt.show()


with open('d15_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]
    
# get_full_map(intc)
field = np.loadtxt('d15_output.txt')

print(part_one(field))
# part_two(field)

