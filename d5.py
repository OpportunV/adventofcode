from intcode_computer import IntcodeComputer

def part_one():
    with open('d5_input.txt') as fin:
        intcode = [int(i) for i in fin.readline().split(',')]
    
    comp = IntcodeComputer(intcode)
    comp.run()


part_one()
