import string
from collections import deque


def part_one(inp):
    stack = deque()
    for let in inp:
        if stack and let == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(let)
            
    return len(stack)


def part_two(inp):
    return min([part_one(inp.replace(low, '').replace(up, ''))
                for low, up in zip(string.ascii_lowercase, string.ascii_uppercase)])


def main():
    with open(r'input\day5.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp[0]))
    print(part_two(inp[0]))
    
    
if __name__ == '__main__':
    main()
