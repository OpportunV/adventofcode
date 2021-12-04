def part_one(inp):
    c = 0
    while True:
        a = c | 65536
        c = inp
        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215
            if 256 > a:
                return c
            else:
                a //= 256


def part_two(inp):
    seen = set()
    c = 0
    last_c = -1
    while True:
        a = c | 65536
        c = inp
        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215
            if 256 > a:
                if c not in seen:
                    seen.add(c)
                    last_c = c
                    break
                else:
                    return last_c
            else:
                a //= 256


def main():
    with open(r'input/day21.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(int(inp[8].split()[1])))
    print(part_two(int(inp[8].split()[1])))
    
    
if __name__ == '__main__':
    main()
