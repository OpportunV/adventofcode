import matplotlib

from d9 import Head, Tail, MOVES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def part_two(inp):
    head = Head(0, 0)
    tails = [Tail(0, 0, head)]
    for i in range(1, 9):
        tails.append(Tail(0, 0, tails[i - 1]))
    
    def step(cur):
        direction, amount = inp[cur].split()
        for _ in range(int(amount)):
            head.move(MOVES[direction])
            for tail in tails:
                tail.move()
    
    n, m = 430, 200
    field = np.zeros((n, m), dtype=int)
    matplotlib.use('TkAgg')
    fig = plt.figure(1, (1, 2), dpi=600)
    field[0, 0] = 1
    field[0, 0] = 2
    field[0, 0] = 3
    img = plt.imshow(field, interpolation='none')
    plt.axis(False)
    
    head = Head(15, m // 2)
    tails = [Tail(15, m // 2, head)]
    for i in range(1, 9):
        tails.append(Tail(15, m // 2, tails[i - 1]))
    
    def animate(cur):
        step(cur)
        field.fill(0)
        field[head.x % n, head.y % m] = 1
        for tail in tails:
            field[tail.x % n, tail.y % m] = 2
        
        for coords in tails[-1].visited:
            field[coords] = 3
        
        img.set_data(field)
        return img,
    
    ani = animation.FuncAnimation(fig, animate, interval=0.1, frames=2000)
    writer = animation.FFMpegFileWriter(fps=30)
    ani.save('d9_visual.mp4', writer=writer)
    plt.show()


def main():
    with open(r'd9_input.txt') as fin:
        inp = fin.read().splitlines()
    
    part_two(inp)
    pass


if __name__ == '__main__':
    main()
