DIRECTIONS = {
    "U": 1j,
    "R": 1,
    "D": -1j,
    "L": -1
}


def part_one(inp):
    code = []
    pos = 0 + 0j
    for line in inp:
        for char in line:
            new_pos = pos + DIRECTIONS[char]
            if abs(new_pos.real) < 2 and abs(new_pos.imag) < 2:
                pos = new_pos
        
        code.append(5 + int(pos.real - 3 * pos.imag))
    
    return ''.join([str(i) for i in code])


def part_two(inp):
    code = []
    pos = 0 + 0j
    for line in inp:
        for char in line:
            new_pos = pos + DIRECTIONS[char]
            if abs(new_pos.real) + abs(new_pos.imag) < 3:
                pos = new_pos
        
        code.append(hex(7 + int(pos.real - 2 * pos.imag - 2 * min(pos.imag, 1)))[2:])
        
    return ''.join(code)


def main():
    with open(r'input\day2.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
