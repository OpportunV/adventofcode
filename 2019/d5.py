from intcode_computer import IntcodeComputer


def part_one():
    with open('d5_input.txt') as fin:
        intcode = [int(i) for i in fin.readline().split(',')]
        
    comp = IntcodeComputer(0, intcode)
    print(comp.cor.send(1))
    for i in comp.cor:
        print(i)


def part_two():
    with open('d5_input.txt') as fin:
        intcode = [int(i) for i in fin.readline().split(',')]
        
    comp = IntcodeComputer(0, intcode)
    print(comp.cor.send(5))
    for i in comp.cor:
        print(i)


part_one()
part_two()
