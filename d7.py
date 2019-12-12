from itertools import permutations
from intcode_computer import IntcodeComputer


def part_one():
    maximum = float('-inf')
    for phases in permutations([0, 1, 2, 3, 4]):
        
        amps = []
        for i in range(5):
            amp = IntcodeComputer(i)
            amps.append(amp)
            amp.cor.send(phases[i])
        
        out1 = amps[0].cor.send(0)
        out5 = amps[4].cor.send(amps[3].cor.send(amps[2].cor.send(amps[1].cor.send(out1))))
        
        if out5 > maximum:
            maximum = out5
    
    return maximum


def part_two():
    maximum = float('-inf')
    # phases = [9,8,7,6,5]
    # phases = [9,7,8,5,6]
    
    for phases in permutations([5, 6, 7, 8, 9]):
        amps = []
        outs = [0] * 5
        for i in range(5):
            amp = IntcodeComputer(i)
            amps.append(amp)
            amp.cor.send(phases[i])
    
        for i in range(5):
            outs[i] = amps[i].cor.send(outs[(i - 1) % 5])
            next(amps[i].cor)
    
        def inner():
            flag = True
            for i in range(5):
                try:
                    outs[i] = amps[i].cor.send(outs[(i - 1) % 5])
                    next(amps[i].cor)
                except StopIteration:
                    flag = False
                    continue
            return flag
    
        while inner():
            pass
        
        maximum = max(maximum, outs[-1])
           
    return maximum


# print(part_one())
print(part_two())
