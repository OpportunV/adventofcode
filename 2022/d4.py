def part_one(inp):
    total_overlap = 0
    for line in inp:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if a1 <= b1 and a2 >= b2 or a1 >= b1 and a2 <= b2:
            total_overlap += 1
    
    return total_overlap


def part_two(inp):
    total_overlap = 0
    for line in inp:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2:
            total_overlap += 1
    
    return total_overlap


def main():
    with open(r'd4_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
