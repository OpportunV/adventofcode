from collections import defaultdict, deque


def part_one(inp):
    constellations = defaultdict(set)
    
    for i, (x, y, z, w) in enumerate(inp):
        for j, (x1, y1, z1, w1) in enumerate(inp):
            if abs(x1 - x) + abs(y1 - y) + abs(z1 - z) + abs(w1 - w) <= 3:
                constellations[i].add(j)
    
    seen = set()
    ans = 0
    for constellation in constellations.keys():
        if constellation in seen:
            continue
        
        ans += 1
        queue = deque([constellation])
        
        while queue:
            current = queue.pop()
            if current in seen:
                continue
            
            seen.add(current)
            for nxt in constellations[current]:
                queue.append(nxt)
                
    return ans


def part_two(inp):
    return "bam"


def main():
    with open(r'input\day25.txt') as fin:
        inp = fin.read().splitlines()
    
    inp = [tuple(int(i) for i in line.split(',')) for line in inp]
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
