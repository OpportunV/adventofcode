import numpy as np

from intcode_computer import IntcodeComputer


def part_one(intcode):
    comp = IntcodeComputer(0, intcode)
    field = np.zeros((39, 51), dtype=int)
    x, y = 0, 0
    field[y, x] = comp.first_val
    x += 1
    
    for i in comp.cor:
        if i == 10:
            y += 1
            x = 0
        else:
            field[y, x] = i
            x += 1
    
    xs, ys = np.where(field[1:-1, 1:-1] == 35)
    ans = 0
    for x, y in zip(xs + 1, ys + 1):
        if field[x - 1, y] == 35 \
                and field[x + 1, y] == 35 \
                and field[x, y - 1] == 35 \
                and field[x, y + 1] == 35:
            ans += x * y
    
    for line in field:
        print(''.join(chr(i) for i in line))
    
    print(ans)
    return field


def part_two(intcode, field):
    intcode[0] = 2
    comp = IntcodeComputer(0, intcode)
    
    prog = [
        'A,B,A,B,C,C,B,A,B,C\n',
        'L,6,6,L,6,L,8,R,6\n',
        'L,8,L,8,R,4,R,6,R,6\n',
        'L,6,6,R,6,L,8\n',
        'y\n',
    ]
    
    print(chr(comp.first_val), end='', sep='')
    while repl := next(comp.cor):
        print(chr(repl), end='', sep='')
    print()
    
    for pr in prog:
        for instr in pr:
            repl = comp.cor.send(ord(instr))
            print(instr, end='')
            if repl:
                print(chr(repl))
        
        if pr == prog[-1]:
            break
        while repl := next(comp.cor):
            if repl and chr(repl).isascii():
                print(chr(repl), end='')
            else:
                print(repl)
                break
    
    def update(frame):
        nonlocal frames, field
        frames += 1
        for i in range(len(field)):
            for j in range(len(field[0])):
                tmp = next(comp.cor)
                while tmp == 10:
                    tmp = next(comp.cor)
                field[i, j] = tmp

        img.set_data(field)
        return img
        
    from matplotlib import pyplot as plt
    from matplotlib.animation import FuncAnimation, FFMpegWriter
    fig, ax = plt.subplots()
    img = plt.imshow(field, interpolation='none')
    plt.axis(False)
    frames = 0
    anim = FuncAnimation(fig, update, interval=0.1, frames=343)
    writer = FFMpegWriter(fps=30)
    plt.rcParams['animation.ffmpeg_path'] = r'D:\univ\Progin\ffmpeg\bin\ffmpeg.exe'
    anim.save('d17.mp4', writer=writer)


with open('d17_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]


def main():
    field = part_one(intc.copy())
    part_two(intc, field)


if __name__ == '__main__':
    main()

