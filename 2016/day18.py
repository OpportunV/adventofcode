TRAP = '^'
SAFE = '.'


def part_one(inp):
    return calculate(40, inp[0])


def part_two(inp):
    return calculate(400000, inp[0])


def calculate(target_count, cur):
    counter = 1
    ans = sum(item == SAFE for item in cur)
    while counter < target_count:
        new = ['1'] * len(cur)
        new[0] = get_tile(SAFE, cur[0], cur[1])
        new[-1] = get_tile(cur[-2], cur[-1], SAFE)
        for i in range(1, len(cur) - 1):
            new[i] = get_tile(cur[i - 1], cur[i], cur[i + 1])

        counter += 1
        ans += sum(item == SAFE for item in new)
        cur = new

    return ans


def get_tile(left, center, right):
    if left == center == TRAP and right != TRAP:
        return TRAP
    if center == right == TRAP and left != TRAP:
        return TRAP
    if left == TRAP and center != TRAP and right != TRAP:
        return TRAP
    if left != TRAP and center != TRAP and right == TRAP:
        return TRAP

    return SAFE


def main():
    with open('input/day18.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
