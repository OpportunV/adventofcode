import aoc


def part_one(inp):
    merged = get_merged(inp)
    return merged[0][1] + 1


def part_two(inp):
    merged = get_merged(inp) + [(2 ** 32, 2 ** 33)]

    counter = 0
    for i in range(len(merged) - 1):
        counter += merged[i + 1][0] - merged[i][1] - 1

    return counter


def get_merged(inp):
    ranges = sorted([tuple(sorted(map(abs, aoc.get_nums(line)))) for line in inp])

    merged = [ranges[0]]
    for r in ranges[1:]:
        if r[0] - 1 <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(r[1], merged[-1][1]))
        else:
            merged.append(r)

    return merged


def main():
    with open('input/day20.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
