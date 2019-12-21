from intcode_computer import IntcodeComputer


def part_one(intcode):
    comp = IntcodeComputer(0, intcode)
    
    spring_script = [
        'NOT A J\n',
        'NOT B T\n',
        'OR T J\n',
        'NOT C T\n',
        'OR T J\n',
        'AND D J\n',
        'WALK\n'
    ]
    
    print(chr(comp.first_val), end='', sep='')
    while repl := next(comp.cor):
        print(chr(repl), end='', sep='')
    print()
    
    for line in spring_script:
        for letter in line:
            repl = comp.cor.send(ord(letter))
            print(letter, end='')
            if repl:
                print(chr(repl))
    try:
        while repl := next(comp.cor):
            if repl and repl < 256:
                print(chr(repl), end='')
            else:
                print(repl)
    except StopIteration:
        return repl


def part_two(intcode):
    comp = IntcodeComputer(0, intcode)
    
    spring_script = [
        'NOT A J\n',
        'AND D J\n',
        'NOT B T\n',
        'AND D T\n',
        'OR T J\n',
        'NOT C T\n',
        'AND D T\n',
        'AND H T\n',
        'OR T J\n',
        'RUN\n'
    ]
    
    print(chr(comp.first_val), end='', sep='')
    while repl := next(comp.cor):
        print(chr(repl), end='', sep='')
    print()
    
    for line in spring_script:
        for letter in line:
            repl = comp.cor.send(ord(letter))
            print(letter, end='')
            if repl:
                print(chr(repl))

    try:
        while repl := next(comp.cor):
            if repl and repl < 256:
                print(chr(repl), end='')
            else:
                print(repl)
    except StopIteration:
        return repl


def main():
    with open('d21_input.txt') as fin:
        intc = [int(i) for i in fin.readline().split(',')]
    
    print(part_one(intc))
    print(part_two(intc))


if __name__ == '__main__':
    main()