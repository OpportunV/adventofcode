import hashlib


def part_one(inp):
    salt = inp[0]
    return get_index(salt, False)


def part_two(inp):
    salt = inp[0]
    return get_index(salt, True)


def get_index(salt, stretch):
    keys = []
    candidates = {}

    cur = 0
    while len(keys) < 64:
        md5 = get_hash(f'{salt}{cur}', stretch)

        to_delete = set()
        for ind, char in candidates.items():
            if cur - ind >= 1000:
                to_delete.add(ind)
                continue

            if char * 5 in md5:
                keys.append(ind)
                to_delete.add(ind)

        for ind in to_delete:
            candidates.pop(ind)

        char = get_triplet_char(md5)
        if char:
            candidates[cur] = char

        cur += 1

    return keys[63]


def get_hash(key, stretch):
    md5 = hashlib.md5(key.encode()).hexdigest()
    if stretch:
        for i in range(2016):
            md5 = hashlib.md5(md5.encode()).hexdigest()

    return md5


def get_triplet_char(line):
    for i in range(len(line) - 2):
        if line[i] == line[i + 1] == line[i + 2]:
            return line[i]

    return None


def main():
    with open('input/day14.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
