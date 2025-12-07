def part_one(inp):
    return sum([check_ip_tls(line) for line in inp])


def part_two(inp):
    return sum([check_ip_ssl(line) for line in inp])


def check_ip_tls(ip: str) -> bool:
    inside = False
    found = False
    length = 4
    for i in range(len(ip) - length + 1):
        if ip[i] == "[":
            inside = True
            continue

        if ip[i] == "]":
            inside = False
            continue

        left = ip[i: i + length // 2]
        right = ip[i + length // 2: i + length]
        if left == right[::-1] and len(set(left)) == len(left):
            if inside:
                return False

            found = True

    return found


def check_ip_ssl(ip: str) -> bool:
    inside = False
    insides = set()
    outsides = set()
    for i in range(len(ip) - 3 + 1):
        if ip[i] == "[":
            inside = True
            continue

        if ip[i] == "]":
            inside = False
            continue

        if ip[i] == ip[i + 2]:
            string = f"{ip[i + 1]}{ip[i]}{ip[i + 1]}"
            if inside:
                if string in outsides:
                    return True
                insides.add(ip[i:i + 3])
            else:
                if string in insides:
                    return True
                outsides.add(ip[i:i + 3])

    return False


def main():
    with open('input/day7.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
