from collections import defaultdict, deque

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import numpy as np

from intcode_computer import IntcodeComputer


def get_full_map(intcode):
    comp = IntcodeComputer(0, intcode)
    size = 41
    field = np.zeros((size, size), dtype=int) - 1
    x, y = size // 2 + 1, size // 2 + 1
    field[x, y] = 1
    field[0, 0] = 0
    field[0, -1] = 2
    field[-1, -1] = 5
    
    def right(move):
        if move == 1:
            return 3
        if move == 2:
            return 4
        if move == 3:
            return 2
        if move == 4:
            return 1
    
    def get_move():
        last_move = 1
        while True:
            if reply == 0:
                last_move = right(right(right(last_move)))
                yield last_move
            yield right(last_move)
            if reply != 0:
                last_move = right(last_move)
                yield last_move
            else:
                yield last_move
                
    reply = 1
    done = False
    fig, ax = plt.subplots()
    img = plt.imshow(field)
    plt.ion()
    plt.axis(False)
    plt.show()
    mover = get_move()
    while not done:
        move = next(mover)
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
        
        tmp =field[x, y]
        field[x, y] = 5
        img.set_data(field)
        plt.pause(1e-10)
        field[x, y] = tmp
        
        xs, ys = np.where(field[1:-1, 1:-1] == -1)
        for _x, _y in zip(xs + 1, ys + 1):
            if not (field[_x - 1, _y] == 0
                    and field[_x + 1, _y] == 0
                    and field[_x, _y - 1] == 0
                    and field[_x, _y + 1] == 0):
                break
        else:
            field[0, 0] = -1
            field[0, -1] = -1
            field[-1, -1] = -1
            with open('d15_output.txt', 'w') as fout:
                for line in field:
                    print(' '.join([f'{i: d}' for i in line]), file=fout)
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
        if 1 not in field:
            print(time)
            input('exit\t')
            exit()
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
    # anim.save('anim.mp4', writer=writer)
    plt.show()


with open('d15_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]

get_full_map(intc)
field = np.loadtxt('d15_output.txt')

# print(part_one(field))
part_two(field)

