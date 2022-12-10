import collections
from collections import defaultdict
from copy import deepcopy

from typing import Dict


def part_one(inp):
    stacks: Dict[int, collections.deque] = get_stacks(inp)
    for line in inp:
        data = line.split()
        n, a, b = map(int, [data[1], data[3], data[5]])
        for i in range(n):
            item = stacks[a].pop()
            stacks[b].append(item)
    
    return ''.join([stack.pop() for stack in stacks.values()])


def part_two(inp):
    stacks: Dict[int, collections.deque] = get_stacks(inp)
    for line in inp:
        data = line.split()
        n, a, b = map(int, [data[1], data[3], data[5]])
        tmp = collections.deque()
        for i in range(n):
            tmp.appendleft(stacks[a].pop())
        
        stacks[b].extend(tmp)
    
    return ''.join([stack.pop() for stack in stacks.values()])


def get_stacks(inp, stacks=defaultdict(collections.deque)):
    if stacks:
        return deepcopy(stacks)
    
    n = 0
    total_height = 0
    for i, line in enumerate(inp):
        if '[' in line:
            continue
        
        n = int(line.split()[-1])
        total_height = i
        break
    
    for i in range(total_height - 1, -1, -1):
        line = inp[i]
        for j in range(1, n + 1):
            cur = 1 + 4 * (j - 1)
            if len(line) <= cur:
                continue
            
            mark = line[cur]
            if mark != ' ':
                stacks[j].append(mark)
    
    while not inp[0].startswith('move'):
        inp.__delitem__(0)
    
    return deepcopy(stacks)


def main():
    with open(r'd5_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
