def part_one(inp, scan):
    results = {}
    for line in scan:
        tmp = line.split(':')
        results[tmp[0]] = lambda x, y=int(tmp[1]): x == y
    for line in inp:
        tmp = line.split()
        if all((results[tmp[i][:-1]](int(tmp[i + 1].strip(','))) for i in range(2, 7, 2))):
            return tmp[1][:-1]


def part_two(inp, scan):
    results = {}
    for line in scan:
        tmp = line.split(':')
        if tmp[0] in {'cats', 'trees'}:
            results[tmp[0]] = lambda x, y=int(tmp[1]): x > y
        elif tmp[0] in {'pomeranians', 'goldfish'}:
            results[tmp[0]] = lambda x, y=int(tmp[1]): x < y
        else:
            results[tmp[0]] = lambda x, y=int(tmp[1]): x == y
    for line in inp:
        tmp = line.split()
        if all((results[tmp[i][:-1]](int(tmp[i + 1].strip(','))) for i in range(2, 7, 2))):
            return tmp[1][:-1]


def main():
    with open('d16_input.txt') as fin, open('d16_scan.txt') as fscan:
        inp = fin.read().splitlines()
        scan = fscan.read().splitlines()
    
    print(part_one(inp, scan))
    print(part_two(inp, scan))
    
    
if __name__ == '__main__':
    main()
