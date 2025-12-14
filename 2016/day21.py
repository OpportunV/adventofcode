from collections import deque
from itertools import permutations

import aoc


def part_one(inp):
    return do_scramble(inp, 'abcdefgh')


def part_two(inp):
    target = 'fbgdceah'

    for val in permutations('abcdefgh', 8):
        if do_scramble(inp, val) == target:
            return ''.join(val)

    return 'no way..'


def do_scramble(inp, val):
    pw = deque(list(val))
    for line in inp:
        nums = aoc.get_nums(line)
        if 'swap position' in line:
            l, r = nums
            pw[l], pw[r] = pw[r], pw[l]

        if 'swap letter' in line:
            split = line.split()
            a, b = split[2], split[-1]
            ai = pw.index(a)
            bi = pw.index(b)
            pw[ai], pw[bi] = b, a

        if 'rotate left' in line or 'rotate right' in line:
            pw.rotate(-nums[0] if 'left' in line else nums[0])

        if 'rotate based' in line:
            letter = line.split()[-1]
            ind = pw.index(letter)
            pw.rotate(1 + ind)
            if ind >= 4:
                pw.rotate()

        if 'reverse positions' in line:
            l, r = nums
            pw = list(pw)
            pw = pw[:l] + pw[l:r + 1][::-1] + pw[r + 1:]
            pw = deque(pw)

        if 'move position' in line:
            x, y = nums
            val = pw[x]
            pw.remove(val)
            pw.insert(y, val)

    return ''.join(pw)


def main():
    with open('input/day21.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
