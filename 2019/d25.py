from collections import deque

from intcode_computer import IntcodeComputer


def part_one(intcode):
    comp = IntcodeComputer(0, intcode)
    
    print(chr(comp.first_val), end='', sep='')
    commands = deque(['south', 'south', 'south', 'take fixed point', 'south', 'take festive hat',
                      'west', 'west', 'take jam', 'south', 'take easter egg', 'north',
                      'east', 'east', 'north', 'west', 'take asterisk', 'east', 'north',
                      'west', 'north', 'north', 'take tambourine', 'south', 'south', 'east',
                      'north', 'west', 'west', 'west', 'take space heater', 'west', 'drop asterisk',
                      'drop jam', 'drop festive hat'])
    while True:
        text = []
        try:
            while repl := next(comp.cor):
                text.append(chr(repl))
        except StopIteration:
            pass
        print(''.join(text))
        
        cmd = commands.popleft() if commands else input()
        for i in cmd:
            repl = comp.cor.send(ord(i))
            if repl:
                print(chr(repl), end='')
        
        comp.cor.send(10)
    

def part_two():
    return 'Weee!'


def main():
    with open('d25_input.txt') as fin:
        intc = [int(i) for i in fin.readline().split(',')]
    
    print(part_one(intc))
    print(part_two())


if __name__ == '__main__':
    main()
