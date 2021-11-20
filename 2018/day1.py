from itertools import cycle


def part_one(inp):
    return sum(map(int, inp))


def part_two(inp):
    cache = set()
    ans = 0
    for i in cycle(map(int, inp)):
        ans += i
        if ans in cache:
            return ans
        cache.add(ans)
    return inp


def main():
    with open(r'input\day1.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
