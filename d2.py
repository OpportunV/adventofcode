def part_one(intcode):

    pos = 0
    opcode = intcode[pos]
    while opcode != 99:
        if opcode == 1:
            tmp = intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
            intcode[intcode[pos + 3]] = tmp
        elif opcode == 2:
            tmp = intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
            intcode[intcode[pos + 3]] = tmp
        
        pos += 4
        opcode = intcode[pos]

    return intcode[0]


def part_two(target=19_690_720):
    for noun in range(100):
        for verb in range(100):
            with open('d2_input.txt') as fin:
                intcode = [int(i) for i in fin.readline().split(',')]
    
            intcode[1] = noun
            intcode[2] = verb
            print(part_one(intcode))
    
            if part_one(intcode) == target:
                return 100 * noun + verb
        
# print(part_two())
