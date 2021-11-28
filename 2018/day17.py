import sys
from collections import defaultdict

sys.setrecursionlimit(10000)
SETTLED = set()
FLOWING = set()


def get_clay(inp):
    clay = defaultdict(bool)
    
    for line in inp:
        left, right = line.split(',')
        first = int(left.split('=')[1])
        second1, second2 = map(int, right.split('=')[1].split('..'))
        if left[0] == 'x':
            for y in range(second1, second2 + 1):
                clay[(first, y)] = True
        else:
            for x in range(second1, second2 + 1):
                clay[(x, first)] = True

    y_min, y_max = min(clay, key=lambda p: p[1])[1], max(clay, key=lambda p: p[1])[1]
    return clay, y_min, y_max


def simulate(pt, clay, y_min, y_max, direction=(0, 1)):
    FLOWING.add(pt)
    below = (pt[0], pt[1] + 1)

    if not clay[below] and below not in FLOWING and 1 <= below[1] <= y_max:
        simulate(below, clay, y_min, y_max)

    if not clay[below] and below not in SETTLED:
        return False

    left = (pt[0] - 1, pt[1])
    right = (pt[0] + 1, pt[1])

    left_filled = clay[left] or left not in FLOWING and simulate(left, clay, y_min, y_max, direction=(-1, 0))
    right_filled = clay[right] or right not in FLOWING and simulate(right, clay, y_min, y_max, direction=(1, 0))

    if direction == (0, 1) and left_filled and right_filled:
        SETTLED.add(pt)

        while left in FLOWING:
            SETTLED.add(left)
            left = (left[0] - 1, left[1])

        while right in FLOWING:
            SETTLED.add(right)
            right = (right[0] + 1, right[1])

    return direction == (-1, 0) and (left_filled or clay[left]) or direction == (1, 0) and (right_filled or clay[right])


def part_one(inp):
    clay, y_min, y_max = get_clay(inp)
    simulate((500, 0), clay, y_min, y_max)
    return len([pt for pt in FLOWING if y_min <= pt[1] <= y_max])


def part_two(inp):
    clay, y_min, y_max = get_clay(inp)
    simulate((500, 0), clay, y_min, y_max)
    return len([pt for pt in SETTLED if y_min <= pt[1] <= y_max])


def main():
    with open(r'input\day17.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
