from collections import defaultdict, Counter
from copy import deepcopy


def adjacent(pos, data):
    x, y = pos
    n = len(data)
    m = len(data[0])
    for dx in range(-1, 2):
        if x + dx < 0 or x + dx >= n:
            continue
        for dy in range(-1, 2):
            if y + dy < 0 or y + dy >= m:
                continue
                
            if dx == 0 and dy == 0:
                continue
            
            yield data[x + dx][y + dy]


def simulate(data):
    n = len(data)
    m = len(data[0])
    new_data = deepcopy(data)
    for x in range(n):
        for y in range(m):
            counter = defaultdict(int)
            for val in adjacent((x, y), data):
                counter[val] += 1
            
            if data[x][y] == '.':
                new_data[x][y] = '|' if counter['|'] >= 3 else '.'
            elif data[x][y] == '|':
                new_data[x][y] = '#' if counter['#'] >= 3 else '|'
            else:
                new_data[x][y] = '#' if (counter['#'] >= 1 and counter['|'] >= 1) else '.'
    
    return new_data


def part_one(inp):
    data = deepcopy(inp)
    for _ in range(10):
        data = simulate(data)
        
    counter = Counter(''.join([''.join(line) for line in data]))
    return counter['|'] * counter['#']


def part_two(inp):
    n = 1_000_000_000
    data = deepcopy(inp)
    cache = {}
    minute = 1
    while True:
        data = simulate(data)
        data_hash = ''.join([''.join(line) for line in data])
        if data_hash in cache.values():
            break
        cache[minute] = data_hash
        minute += 1
        
    last_time = list(filter(lambda item: item[1] == data_hash, cache.items()))[0][0]
    period = minute - last_time
    
    while last_time % period != n % period:
        last_time += 1
        
    counter = Counter(cache[last_time])
    return counter['|'] * counter['#']


def main():
    with open(r'input\day18.txt') as fin:
        inp = fin.read().splitlines()
    
    inp = [list(line) for line in inp]
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
