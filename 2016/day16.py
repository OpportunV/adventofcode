def part_one(inp):
    return solve(inp[0], 272)


def part_two(inp):
    return solve(inp[0], 35651584)


def solve(data, length):
    while len(data) < length:
        data = generate_next(data)

    return generate_checksum(data[:length])


def generate_next(data: str):
    b = reversed(data)
    b = ''.join(['0' if item == '1' else '1' for item in b])
    return f'{data}0{b}'


def generate_checksum(data):
    new = []
    while True:
        for i in range(0, len(data), 2):
            new.append('1' if data[i] == data[i + 1] else '0')

        if len(new) % 2 == 1:
            return ''.join(new)

        data = new[:]
        new = []


def main():
    with open('input/day16.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
