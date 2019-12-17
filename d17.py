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
    
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots()
    img = plt.imshow(field)
    plt.axis(False)
    plt.show()


def part_two(intcode):
    intcode[0] = 2
    comp = IntcodeComputer(0, intcode)
    
    prog = [
        'A,B,A,B,C,C,B,A,B,C\n',
        'L,6,6,L,6,L,8,R,6\n',
        'L,8,L,8,R,4,R,6,R,6\n',
        'L,6,6,R,6,L,8\n',
        'n\n',
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
        
        while repl := next(comp.cor):
            if repl and chr(repl).isascii():
                print(chr(repl), end='')
            else:
                print(repl)
    
    for i in range(10):
        print(next(comp.cor))


with open('d17_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]

# part_one(intc)
part_two(intc)
