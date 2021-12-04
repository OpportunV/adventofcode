from collections import defaultdict, deque

DIRECTIONS = {
    "N": -1j,
    "E": 1,
    "S": 1j,
    "W": -1,
}


def part_one(inp):
    distances = get_distances(inp)
    return max(distances.values())


def part_two(inp):
    distances = get_distances(inp)
    return len(list(filter(lambda item: item >= 1000, distances.values())))


def get_distances(inp):
    distances = defaultdict(int)
    positions = deque()
    pos = new_pos = 0 + 0j
    for char in inp[1:-1]:
        if char == '(':
            positions.append(new_pos)
        elif char == ')':
            new_pos = positions.pop()
        elif char == '|':
            new_pos = positions[-1]
        else:
            new_pos = pos + DIRECTIONS[char]
            if distances[new_pos] != 0:
                distances[new_pos] = min(distances[new_pos], distances[pos] + 1)
            else:
                distances[new_pos] = distances[pos] + 1
        
        pos = new_pos
    return distances


def main():
    with open(r'input\day20.txt') as fin:
        inp = fin.read()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
