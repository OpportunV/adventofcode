from collections import defaultdict


def part_one(inp):
    x_max, x_min, y_max, y_min = get_boundaries(inp)
    
    counter = defaultdict(int)
    
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            p = min(inp, key=lambda item: abs(item[0] - i) + abs(item[1] - j))
            counter[p] += 1
    
    return max(counter.values())


def part_two(inp):
    x_max, x_min, y_max, y_min = get_boundaries(inp)
    
    ans = 0
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            p = sum(map(lambda item: abs(item[0] - i) + abs(item[1] - j), inp))
            ans += 1 if p < 10_000 else 0
    
    return ans


def get_boundaries(inp):
    x_min = min(inp, key=lambda item: item[0])[0]
    x_max = max(inp, key=lambda item: item[0])[0]
    y_min = min(inp, key=lambda item: item[1])[1]
    y_max = max(inp, key=lambda item: item[1])[1]
    return x_max, x_min, y_max, y_min


def main():
    with open(r'input\day6.txt') as fin:
        inp = fin.read().splitlines()
    inp = [tuple(map(int, line.split(','))) for line in inp]
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
