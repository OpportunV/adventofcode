import math
import sys
from functools import lru_cache
from heapq import heappop, heappush

sys.setrecursionlimit(10000)


@lru_cache(None)
def get_erosion_level(x, y, target, depth):
    if x == y == 0:
        return 0
    
    if x == target[0] and y == target[1]:
        return 0
    
    if y == 0:
        return x * 16807 % 20183
    elif x == 0:
        return y * 48271 % 20183
    else:
        return ((depth + get_erosion_level(x - 1, y, target, depth))
                * (depth + get_erosion_level(x, y - 1, target, depth)) % 20183)


def get_region(x, y, target, depth):
    ans = (get_erosion_level(x, y, target, depth) + depth) % 20183 % 3
    return ans


def adjacent(x, y, item, target, depth):
    for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
        if x + dx >= 0 and y + dy >= 0:
            region = get_region(x, y, target, depth)
            for new_item in range(3):
                if region != new_item and region != item:
                    yield x + dx, y + dy, new_item, 8 if item != new_item else 1


def part_one(depth, target):
    return sum(get_region(x, y, target, depth) for x in range(target[0] + 1) for y in range(target[1] + 1))


def part_two(depth, target):
    queue = [(0, 0, 0, 1)]
    distances = {(0, 0, 1): 0}
    t_x = target[0]
    t_y = target[1]
    
    while queue:
        dist, x, y, item = heappop(queue)
        if (x, y, item) == (t_x, t_y, 1):
            return dist
        
        if x > 3 * t_x or y > 3 * t_y or distances.get((x, y, item)) < dist:
            continue
        
        for adj_x, adj_y, adj_item, adj_dist in adjacent(x, y, item, target, depth):
            if dist + adj_dist < distances.get((adj_x, adj_y, adj_item), math.inf):
                distances[(adj_x, adj_y, adj_item)] = dist + adj_dist
                heappush(queue, (dist + adj_dist, adj_x, adj_y, adj_item))


def main():
    with open(r'input\day22.txt') as fin:
        inp = fin.read().splitlines()
    
    depth = int(inp[0].split(': ')[1])
    target = tuple(int(i) for i in inp[1].split(': ')[1].split(','))
    
    print(part_one(depth, target))
    print(part_two(depth, target))


if __name__ == '__main__':
    main()
