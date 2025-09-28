import hashlib


def part_one(inp):
    index = 0
    result = ''

    while len(result) != 8:
        hex_hash = hashlib.md5(f'{inp}{index}'.encode()).hexdigest()
        if hex_hash.startswith('00000'):
            result += hex_hash[5]

        index += 1

    return result


def part_two(inp):
    index = 0
    result = [None] * 8

    while None in result:
        hex_hash = hashlib.md5(f'{inp}{index}'.encode()).hexdigest()
        if hex_hash.startswith('00000'):
            pos = int(hex_hash[5], 16)
            if pos <= 7 and result[pos] is None:
                result[pos] = hex_hash[6]

        index += 1

    return ''.join(result)


def main():
    with open('input/day5.txt') as fin:
        inp = fin.read().splitlines()[0]

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
