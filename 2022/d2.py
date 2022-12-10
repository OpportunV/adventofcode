from copy import deepcopy


def part_one(inp):
    total = 0
    tmp = deepcopy(inp)
    for line in tmp:
        a, b = line.split()
        a_ord = ord(a) - ord('A')
        b_ord = ord(b) - ord('X')
        if b_ord - a_ord == 0:
            total += 3
        
        if (b_ord - a_ord) % 3 == 1:
            total += 6
        
        total += b_ord + 1
    
    return total


def part_two(inp):
    total = 0
    tmp = deepcopy(inp)
    for line in tmp:
        a, b = line.split()
        a_ord = ord(a) - ord('A')
        if b == 'X':
            total += (a_ord - 1) % 3 + 1
        
        if b == 'Y':
            total += 3
            total += a_ord + 1
        
        if b == 'Z':
            total += 6
            total += (a_ord + 1) % 3 + 1
    
    return total


def main():
    with open(r'd2_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
