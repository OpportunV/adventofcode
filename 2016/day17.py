import hashlib
from collections import deque

DIRS = ['U', 'D', 'L', 'R']


def part_both(inp):
    data = inp[0]
    start = (0, 0)
    end = (3, 3)

    to_visit = deque([(start, '')])

    res = 0
    while to_visit:
        cur, path = to_visit.popleft()
        (x, y) = cur
        if cur == end:
            if res == 0:
                print(path)
            res = max(res, len(path))
            continue

        md5 = get_hash(f'{data}{path}')[:4]
        for i, (dx, dy) in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]):
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < 4 and 0 <= next_y < 4 and md5[i] in 'bcdef':
                to_visit.append(((next_x, next_y), path + DIRS[i]))

    return res


def main():
    with open('input/day17.txt') as fin:
        inp = fin.read().splitlines()

    print(part_both(inp))


def get_hash(key):
    return hashlib.md5(key.encode()).hexdigest()


if __name__ == '__main__':
    main()
