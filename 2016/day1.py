def part_one(inp):
    pos = 0 + 0j
    direction = 1j
    for command in inp:
        rotate = command[0]
        value = int(command[1:])
        if rotate == "R":
            direction *= -1j
        elif rotate == "L":
            direction *= 1j
        
        pos += direction * value
    
    return int(abs(pos.real) + abs(pos.imag))
    

def part_two(inp):
    pos = 0 + 0j
    direction = 1j
    visited = {pos}
    for command in inp:
        rotate = command[0]
        value = int(command[1:])
        if rotate == "R":
            direction *= -1j
        elif rotate == "L":
            direction *= 1j
        
        for i in range(value):
            pos += direction
            if pos in visited:
                return int(abs(pos.real) + abs(pos.imag))
            
            visited.add(pos)
    
    return -1


def main():
    with open(r'input\day1.txt') as fin:
        inp = fin.read().split(', ')
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
