from collections import Counter


def part_one(inp):
    double = triple = 0
    for line in inp:
        counter = Counter(line)
        if 2 in counter.values():
            double += 1
        if 3 in counter.values():
            triple += 1
        
    return double * triple


def part_two(inp):
    length = len(inp)
    for i in range(length):
        first = inp[i]
        for j in range(i + 1, length):
            second = inp[j]
            if sum([1 for ind, let in enumerate(first) if let != second[ind]]) == 1:
                return ''.join([let for ind, let in enumerate(first) if let == second[ind]])
            
    return inp


def main():
    with open(r'input\day2.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
