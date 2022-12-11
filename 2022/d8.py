def get_field(inp):
    return [list(map(int, line)) for line in inp]


def is_visible(value, sub_list):
    return all([value > item for item in sub_list])


def count_visible(value, sub_list):
    for i in range(len(sub_list)):
        if value <= sub_list[i]:
            return i + 1
    
    return len(sub_list)


def part_one(inp):
    n = len(inp)
    m = len(inp[0])
    total = 2 * (n + m - 2)
    for i in range(1, n - 1, 1):
        for j in range(1, m - 1, 1):
            cur = inp[i][j]
            if is_visible(cur, inp[i][j + 1:]) \
                    or is_visible(cur, inp[i][:j]) \
                    or is_visible(cur, [inp[k][j] for k in range(i)]) \
                    or is_visible(cur, [inp[k][j] for k in range(i + 1, n, 1)]):
                total += 1
    
    return total


def part_two(inp):
    n = len(inp)
    m = len(inp[0])
    score = 0
    for i in range(1, n - 1, 1):
        for j in range(1, m - 1, 1):
            cur = inp[i][j]
            if is_visible(cur, inp[i][j + 1:]) \
                    or is_visible(cur, inp[i][:j]) \
                    or is_visible(cur, [inp[k][j] for k in range(i)]) \
                    or is_visible(cur, [inp[k][j] for k in range(i + 1, n, 1)]):
                sub_score = count_visible(cur, inp[i][j + 1:]) * \
                            count_visible(cur, list(reversed(inp[i][:j]))) * \
                            count_visible(cur, list(reversed([inp[k][j] for k in range(i)]))) * \
                            count_visible(cur, [inp[k][j] for k in range(i + 1, n, 1)])
                score = max(score, sub_score)
    
    return score


def main():
    with open(r'd8_input.txt') as fin:
        inp = fin.read().splitlines()
    
    field = get_field(inp)
    print(part_one(field))
    print(part_two(field))


if __name__ == '__main__':
    main()
