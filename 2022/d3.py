def part_one(inp):
    total_priority = 0
    for line in inp:
        n = len(line)
        a, b = line[:n // 2], line[n // 2:]
        same = set(a).intersection(set(b))
        assert len(same) == 1
        item: str = same.pop()
        total_priority += 1 if item.islower() else 27
        total_priority += ord(item.lower()) - ord('a')
        
    return total_priority


def part_two(inp):
    total_priority = 0
    for i in range(0, len(inp), 3):
        a, b, c = inp[i], inp[i + 1], inp[i + 2]
        badge = set(a).intersection(set(b)).intersection(set(c))
        assert len(badge) == 1
        item: str = badge.pop()
        total_priority += 1 if item.islower() else 27
        total_priority += ord(item.lower()) - ord('a')
    
    return total_priority


def main():
    with open(r'd3_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
