from collections import defaultdict, deque

from intcode_computer import IntcodeComputer


def part_one(intcode):
    comps = []
    to_send = defaultdict(deque)
    for i in range(50):
        comp = IntcodeComputer(i, intcode)
        comp.cor.send(i)
        comps.append(comp)
    
    while True:
        for comp in comps:
            msg = to_send[comp.ind].popleft() if to_send[comp.ind] else -1
            repl = comp.cor.send(msg)
            if repl:
                tmp = next(comp.cor)
                to_send[repl].append(tmp)
                tmp = next(comp.cor)
                if repl == 255:
                    return tmp
                to_send[repl].append(tmp)
    
        
def part_two(intcode):
    comps = []
    to_send = defaultdict(deque)
    for i in range(50):
        comp = IntcodeComputer(i, intcode)
        comp.cor.send(i)
        comps.append(comp)
    
    nat = None
    prev_y = None
    i = 0
    last_repl = 0
    while True:
        if i - last_repl > 500:
            x, y = nat
            if y == prev_y:
                return y
            to_send[0].append(x)
            to_send[0].append(y)
            prev_y = y
            last_repl = i
            
        for comp in comps:
            msg = to_send[comp.ind][0] if to_send[comp.ind] else -1
            if comp.last_inp == msg:
                msg = to_send[comp.ind].popleft() if to_send[comp.ind] else -1
                msg = to_send[comp.ind][0] if to_send[comp.ind] else -1
            repl = comp.cor.send(msg)
            if repl is None:
                continue
            last_repl = i
            x = comp.cor.send(msg)
            y = comp.cor.send(msg)
            if repl == 255:
                nat = x, y
            else:
                to_send[repl].append(x)
                to_send[repl].append(y)
        i += 1
            


def main():
    with open('d23_input.txt') as fin:
        intc = [int(i) for i in fin.readline().split(',')]
    print(part_one(intc.copy()))
    print(part_two(intc.copy()))


if __name__ == '__main__':
    main()

