import aoc


def part_one(inp):
    return decompress(inp[0], False)


def part_two(inp):
    return decompress(inp[0], True)


def main():
    with open('input/day9.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


def decompress(line: str, full):
    if '(' not in line:
        return len(line)
    res = 0
    while '(' in line:
        start = line.find('(')
        res += start
        line = line[start:]
        end = line.find(')')
        length, amount = aoc.get_nums(line[1:end])
        line = line[end + 1:]
        if full:
            res += decompress(line[:length], full) * amount
        else:
            res += len(line[:length]) * amount
        line = line[length:]
    res += len(line)
    return res


if __name__ == '__main__':
    main()
