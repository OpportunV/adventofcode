from collections import deque


def part_one(inp):
    start = 0, 0
    must_visit = {}
    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] == '0':
                start = r, c
            if inp[r][c].isnumeric():
                must_visit[(r, c)] = int(inp[r][c])

    target_flag = sum(1 << val for val in must_visit.values())

    to_visit = deque([(start, 0, 0)])
    seen = set()
    while to_visit:
        pos, steps, flag = to_visit.popleft()
        r, c = pos
        if pos in must_visit:
            flag |= 1 << must_visit[pos]

        if flag == target_flag:
            return steps

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc, flag) in seen:
                continue

            seen.add((nr, nc, flag))
            if 0 <= nr < len(inp) and 0 <= nc < len(inp[0]) and inp[nr][nc] != '#':
                to_visit.append(((nr, nc), steps + 1, flag))

    return 'No way..'


def part_two(inp):
    start = 0, 0
    must_visit = {}
    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] == '0':
                start = r, c
            if inp[r][c].isnumeric():
                must_visit[(r, c)] = int(inp[r][c])

    target_flag = sum(1 << val for val in must_visit.values())
    to_visit = deque([(start, 0, 1)])
    seen = set()
    end_steps = []
    while to_visit:
        pos, steps, flag = to_visit.popleft()
        r, c = pos
        if pos in must_visit:
            flag |= 1 << must_visit[pos]

        if flag == target_flag:
            end_steps.append((pos, steps))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc, flag) in seen:
                continue

            seen.add((nr, nc, flag))
            if 0 <= nr < len(inp) and 0 <= nc < len(inp[0]) and inp[nr][nc] != '#':
                to_visit.append(((nr, nc), steps + 1, flag))

    ans = int(10 ** 5)
    for end, steps in end_steps:
        to_visit = deque([(end, steps)])
        seen = set()
        while to_visit:
            pos, steps = to_visit.popleft()
            if steps >= ans:
                break
            r, c = pos
            if pos == start:
                ans = min(ans, steps)
                break

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in seen:
                    continue

                seen.add((nr, nc))
                if 0 <= nr < len(inp) and 0 <= nc < len(inp[0]) and inp[nr][nc] != '#':
                    to_visit.append(((nr, nc), steps + 1))

    return ans


def main():
    with open('input/day24.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
