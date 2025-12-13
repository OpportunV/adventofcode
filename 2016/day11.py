def part_one(inp):
    floors = []
    for line in inp:
        floors.append(len(line.split(' a ')) - 1)

    return calculate_moves(floors)


def part_two(inp):
    floors = []
    for line in inp:
        floors.append(len(line.split(' a ')) - 1)

    floors[0] += 4
    return calculate_moves(floors)


def main():
    with open('input/day11.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


def calculate_moves(floors):
    res = 0
    for i, amount in enumerate(floors):
        if i == len(floors) - 1:
            break
        res += 2 * (amount - 1 if amount > 1 else 1) - 1
        floors[i] = 0
        floors[i + 1] += amount

    return res


if __name__ == '__main__':
    main()
