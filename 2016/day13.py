from collections import deque
from functools import cache


def part_one(inp):
    num = int(inp[0])
    start = (1, 1)
    target = (31, 39)
    to_visit = deque([(start, 0)])
    seen = set()
    while to_visit:
        (cur, steps) = to_visit.popleft()
        x, y = cur
        if cur == target:
            return steps

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_y < 0 or (next_x, next_y) in seen:
                continue

            seen.add((next_x, next_y))

            if not is_open(next_x, next_y, num):
                continue

            to_visit.append(((next_x, next_y), steps + 1))

    return inp


def part_two(inp):
    num = int(inp[0])
    start = (1, 1)
    to_visit = deque([(start, 0)])
    seen = set()
    while to_visit:
        (cur, steps) = to_visit.popleft()
        x, y = cur
        if steps == 50:
            continue

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_y < 0 or (next_x, next_y) in seen:
                continue

            if not is_open(next_x, next_y, num):
                continue

            seen.add((next_x, next_y))
            to_visit.append(((next_x, next_y), steps + 1))

    return len(seen)


@cache
def is_open(x, y, num):
    res = x * x + 3 * x + 2 * x * y + y + y * y
    res += num
    return bin(res)[2:].count('1') % 2 == 0


def main():
    with open('input/day13.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
