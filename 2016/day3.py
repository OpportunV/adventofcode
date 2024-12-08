def part_one(inp):
    counter = 0
    for triangle in inp:
        if is_triangle(*triangle):
            counter += 1
    
    return counter


def part_two(inp):
    counter = 0
    for i in range(0, len(inp), 3):
        for triangle in zip(*inp[i: i + 3]):
            if is_triangle(*triangle):
                counter += 1
    
    return counter


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def main():
    with open('input/day3.txt') as fin:
        inp = fin.read().splitlines()
    
    inp = [[int(item) for item in line.split()] for line in inp]
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
