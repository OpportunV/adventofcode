FIRST = 20151125


def part_one(inp):
    i, j = inp
    s = sum(range(j + 1))
    for a in range(i - 1):
        s += j + a
    
    ans = FIRST
    for a in range(1, s):
        ans = ans * 252533 % 33554393

    return ans


def part_two(inp):
    return inp


def main():
    with open('d25_input.txt') as fin:
        inp = [int(i) for i in fin.readline().replace(',', '').replace('.', '').split() if i.isdigit()]
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
