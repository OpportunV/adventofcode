def part_one(inp):
    regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    simulate(regs, inp)
    return regs['a']


def part_two(inp):
    regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    simulate(regs, inp)
    return regs['a']


def simulate(regs, inp):
    cur = 0
    while cur < len(inp):
        line = inp[cur]
        split = line.split()
        if 'cpy' in line:
            regs[split[2]] = get_val(split[1], regs)

        if 'inc' in line:
            regs[split[1]] += 1

        if 'dec' in line:
            regs[split[1]] -= 1

        if 'jnz' in line:
            if get_val(split[1], regs) != 0:
                cur += int(split[2])
            else:
                cur += 1
        else:
            cur += 1


def get_val(val, regs):
    if val in regs:
        return regs[val]
    else:
        return int(val)


def main():
    with open('input/day12.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
