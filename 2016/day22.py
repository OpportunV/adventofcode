from collections import deque

import aoc


def part_one(inp):
    nodes = get_nodes(inp)
    counter = 0
    for ((x1, y1), (size1, used1, avail1, use1)) in nodes.items():
        if used1 == 0:
            continue
        for ((x2, y2), (size2, used2, avail2, use2)) in nodes.items():
            if (x1, y1) == (x2, y2):
                continue

            if used1 <= avail2:
                counter += 1

    return counter


def part_two(inp):
    nodes = get_nodes(inp)
    max_x = max([key[0] for key in nodes.keys()])
    empty = (0, 0)
    to_remove = set()
    for (pos, (size1, used1, avail1, use1)) in nodes.items():
        if used1 == 0:
            empty = pos

        if size1 > 100:
            to_remove.add(pos)

    for pos in to_remove:
        del nodes[pos]

    target = (max_x, 0)
    start = (0, 0)
    data_path = get_path(start, target, nodes)[::-1]
    counter = 0
    for i in range(1, len(data_path)):
        pos = data_path[i]
        counter += len(get_path(empty, pos, nodes, ignore=target))
        empty = target
        target = pos

    return counter


def get_path(cur, end, nodes, ignore=None):
    to_visit = deque([(cur, [cur])])
    seen = {ignore}
    while to_visit:
        cur, path = to_visit.popleft()
        x, y = cur
        if cur == end:
            return path

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nxt = x + dx, y + dy
            if nxt in seen:
                continue

            seen.add(nxt)
            if nxt in nodes:
                to_visit.append((nxt, path + [nxt]))

    return None


def get_nodes(inp):
    nodes = {}
    for line in inp[2:]:
        x, y, size, used, avail, use = aoc.get_nums(line)
        nodes[(x, y)] = (size, used, avail, use)

    return nodes


def main():
    with open('input/day22.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
