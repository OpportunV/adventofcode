def part_one(inp):
    n = 1000
    data = [[False for _ in range(n)] for _ in range(n)]
    for line in inp:
        if 'off' in line:
            c0, r0 = [int(i) for i in line.split()[2].split(',')]
            c1, r1 = [int(i) for i in line.split()[4].split(',')]
            for i in range(r0, r1 + 1):
                data[i][c0:c1 + 1] = [False for _ in data[i][c0:c1 + 1]]
        elif 'on' in line:
            c0, r0 = [int(i) for i in line.split()[2].split(',')]
            c1, r1 = [int(i) for i in line.split()[4].split(',')]
            for i in range(r0, r1 + 1):
                data[i][c0:c1 + 1] = [True for _ in data[i][c0:c1 + 1]]
        else:
            c0, r0 = [int(i) for i in line.split()[1].split(',')]
            c1, r1 = [int(i) for i in line.split()[3].split(',')]
            for i in range(r0, r1 + 1):
                data[i][c0:c1 + 1] = [not val for val in data[i][c0:c1 + 1]]
    
    return sum([sum(line) for line in data])


def part_two(inp):
    n = 1000
    data = [[0 for _ in range(n)] for _ in range(n)]
    for line in inp:
        if 'off' in line:
            c0, r0 = [int(i) for i in line.split()[2].split(',')]
            c1, r1 = [int(i) for i in line.split()[4].split(',')]
            for i in range(r0, r1 + 1):
                for j in range(c0, c1 + 1):
                    data[i][j] = max(data[i][j] - 1, 0)
                    
        elif 'on' in line:
            c0, r0 = [int(i) for i in line.split()[2].split(',')]
            c1, r1 = [int(i) for i in line.split()[4].split(',')]
            for i in range(r0, r1 + 1):
                for j in range(c0, c1 + 1):
                    data[i][j] += 1
        else:
            c0, r0 = [int(i) for i in line.split()[1].split(',')]
            c1, r1 = [int(i) for i in line.split()[3].split(',')]
            for i in range(r0, r1 + 1):
                for j in range(c0, c1 + 1):
                    data[i][j] += 2
    
    return sum([sum(line) for line in data])


def main():
    with open('d6_input.txt') as fin:
        inp = fin.read().splitlines()
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
