import numpy as np

from intcode_computer import IntcodeComputer


def robot():
    pos = np.array([0, 0])
    painted = {(0, 0):1}
    directions = ['u', 'l', 'd', 'r']
    movement = {'u': np.array([0, 1]),
                'l': np.array([-1, 0]),
                'd': np.array([0, -1]),
                'r': np.array([1, 0])}
    direction = directions[0]
    while True:
        cur_col = painted.get((pos[0], pos[1]), 0)
        yield cur_col
        
        color = yield
        if color == 2:

            yield painted
            return
        painted[(pos[0], pos[1])] = color
        turn = yield
        if turn == 0:
            direction = directions[(directions.index(direction) + 1) % 4]
        if turn == 1:
            direction = directions[(directions.index(direction) - 1) % 4]
        pos += movement[direction]
        
        
def part_both(intcode):
    comp = IntcodeComputer(0, intcode=intcode)
    rob = robot()
    cur_col = next(rob)
    next(rob)
    while True:
        try:
            color = comp.cor.send(cur_col)
            turn = next(comp.cor)
            next(comp.cor)
            rob.send(color)
            cur_col = rob.send(turn)
            next(rob)
        except StopIteration:
            painted = rob.send(2)
            break

    keys = sorted(painted, key=lambda x: -x[1])

    line = ['\u25AF' for i in range(100)]
    ans = []

    cur_row = 0
    for coords in keys:
        if cur_row != coords[1]:
            ans.extend(line)
            ans.append('\n')
            cur_row = coords[1]
        line[coords[0]] = '\u25AE' if painted[coords] == 1 else '\u25AF'
    else:
        ans.extend(line)
    
    print(''.join(ans))

    
with open('d11_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]
    
part_both(intc)
