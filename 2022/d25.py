FROM_SNAFU = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}

TO_SNAFU = {v: k for k, v in FROM_SNAFU.items()}


def part_one(inp):
    max_cols = max(len(num) for num in inp)
    result_in_snafu = []
    extra = 0
    for col in range(max_cols):
        sum_col = extra
        for num in inp:
            if col < len(num):
                sum_col += FROM_SNAFU[num[len(num) - 1 - col]]

        extra = 0
        while sum_col > 2:
            extra += 1
            sum_col -= 5

        while sum_col < -2:
            extra -= 1
            sum_col += 5

        result_in_snafu.append(TO_SNAFU[sum_col])

    return ''.join(reversed(result_in_snafu))


def main():
    with open(r'd25_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))


if __name__ == '__main__':
    main()
