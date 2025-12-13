import aoc


def part_both(inp):
    grid = [[False for _ in range(50)] for _ in range(6)]

    for line in inp:
        if 'rect' in line:
            cols, rows = aoc.get_nums(line)
            for i in range(rows):
                for j in range(cols):
                    grid[i][j] = True

        if 'rotate row' in line:
            row, amount = aoc.get_nums(line)
            grid[row] = grid[row][-amount:] + grid[row][:-amount]

        if 'rotate column' in line:
            col, amount = aoc.get_nums(line)
            for i in range(amount):
                tmp = grid[-1][col]
                for j in range(len(grid)):
                    (grid[j][col], tmp) = (tmp, grid[j][col])

    print('\n'.join(''.join(['#' if it else '.' for it in row]) for row in grid))
    return sum([sum(row) for row in grid])


def main():
    with open('input/day8.txt') as fin:
        inp = fin.read().splitlines()

    print(part_both(inp))


if __name__ == '__main__':
    main()
