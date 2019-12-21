from intcode_computer import IntcodeComputer


def part_both(intcode):
    comp = IntcodeComputer(0, intcode=intcode)
    print(comp.first_val)
    print(comp.cor.send(2))
    for i in comp.cor:
        print(i)


with open('d9_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]
    
part_both(intc)
