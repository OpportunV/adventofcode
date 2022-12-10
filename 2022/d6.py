def part_one(inp):
    return find_first_n_unique_pos(inp[0], 4)


def find_first_n_unique_pos(line: str, n: int):
    for i in range(n, len(line)):
        if len(set(line[i - n: i])) == n:
            return i


def part_two(inp):
    return find_first_n_unique_pos(inp[0], 14)


def main():
    with open(r'd6_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
