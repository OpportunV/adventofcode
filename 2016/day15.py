import aoc


def part_one(inp):
    disks = get_disks(inp)
    return simulate(disks)


def part_two(inp):
    disks = get_disks(inp)
    disks.append((len(disks) + 1, 11, 0))
    return simulate(disks)


def simulate(disks):
    t = 1
    while True:
        if all((((t + ind) % total) + start) % total == 0 for (ind, total, start) in disks):
            return t
        t += 1


def get_disks(inp):
    return [(nums[0], nums[1], nums[3]) for nums in [aoc.get_nums(line) for line in inp]]


def main():
    with open('input/day15.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
