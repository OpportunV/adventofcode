from itertools import combinations


def part_one(inp, amount=150):
    ans = 0
    for i in range(len(inp)):
        for cups in combinations(inp, i):
            if sum(cups) == amount:
                ans += 1
    return ans


def part_two(inp, amount=150):
    ans = 0
    for i in range(len(inp)):
        for cups in combinations(inp, i):
            if sum(cups) == amount:
                ans += 1
        if ans:
            break
    return ans


def main():
    with open('d17_input.txt') as fin:
        inp = [int(x) for x in fin.read().splitlines()]
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
