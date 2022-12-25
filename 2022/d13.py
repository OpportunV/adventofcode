from itertools import zip_longest


def compare(first, second):
    for a, b in zip_longest(first, second, fillvalue=-1):
        if a == -1:
            return 1
        
        if b == -1:
            return 0
        
        if isinstance(a, int) and isinstance(b, int):
            if a > b:
                return 0
            
            if b > a:
                return 1
        else:
            if isinstance(a, int):
                a = [a]
            
            if isinstance(b, int):
                b = [b]
            
            res = compare(a, b)
            if isinstance(res, int):
                return res


def part_one(inp):
    pairs = [(eval(inp[i]), eval(inp[i + 1])) for i in range(0, len(inp), 3)]
    total = 0
    for i in range(len(pairs)):
        total += i + 1 if compare(*pairs[i]) else 0
    
    return total


def part_two(inp):
    target1 = [[2]]
    target2 = [[6]]
    pairs = [eval(line) for line in inp if line != '']
    pairs.extend([target1, target2])
    done = False
    while not done:
        done = True
        for i in range(1, len(pairs)):
            if not compare(pairs[i - 1], pairs[i]):
                pairs[i - 1], pairs[i] = pairs[i], pairs[i - 1]
                done = False
    
    return (pairs.index(target1) + 1) * (pairs.index(target2) + 1)


def main():
    with open(r'd13_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
