from collections import Counter


def part_one(inp):
    counters = [Counter(i) for i in zip(*inp)]

    return ''.join(item.most_common()[0][0] for item in counters)


def part_two(inp):
    counters = [Counter(i) for i in zip(*inp)]

    return ''.join(item.most_common()[-1][0] for item in counters)


def main():
    with open('input/day6.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
