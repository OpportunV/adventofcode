def part_one(inp):
    register = {'a': 0, 'b': 0}

    run_programm(inp, register)

    return register['b']


def run_programm(inp, register):
    program_counter = -1
    eop = len(inp)
    while program_counter < eop - 1:
        program_counter += 1
        instruction = inp[program_counter]
        if instruction[0] == "hlf":
            register[instruction[1]] /= 2
        elif instruction[0] == "tpl":
            register[instruction[1]] *= 3
        elif instruction[0] == "inc":
            register[instruction[1]] += 1
        elif instruction[0] == "jmp":
            program_counter += int(instruction[1]) - 1
        elif instruction[0] == "jie":
            if register[instruction[1]] % 2 == 0:
                program_counter += int(instruction[2]) - 1
        elif instruction[0] == "jio":
            if register[instruction[1]] == 1:
                program_counter += int(instruction[2]) - 1


def part_two(inp):
    register = {'a': 1, 'b': 0}
    
    run_programm(inp, register)
    
    return register['b']


def main():
    with open('d23_input.txt') as fin:
        inp = [line.strip().replace(',', '').split() for line in fin.read().splitlines()]
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
