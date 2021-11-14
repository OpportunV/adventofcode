from functools import reduce
from itertools import combinations
from operator import mul


def part_one(inp):
    return run(inp, 3)


def part_two(inp):
    return run(inp, 4)


def run(inp, groups_num):
    group_size = sum(inp) // groups_num
    for i in range(len(inp)):
        qes = [reduce(mul, c) for c in combinations(inp, i)
               if sum(c) == group_size]
        if qes:
            return min(qes)


def main():
    with open('d24_input.txt') as fin:
        inp = [int(i) for i in fin.read().splitlines()]
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
