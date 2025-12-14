def part_one(inp):
    cur = 0
    while True:
        regs = {'a': cur, 'b': 0, 'c': 0, 'd': 0}
        gen = simulate(regs, inp[:])

        for i in range(100):
            val = next(gen)
            if i % 2 != val:
                break
        else:
            return cur

        cur += 1


def part_two(inp):
    return '*'


def simulate(regs, inp):
    cur = 0
    while cur < len(inp):
        line = inp[cur]
        split = line.split()
        if 'cpy' in line:
            if split[2] in regs:
                regs[split[2]] = get_val(split[1], regs)

        if 'inc' in line:
            if split[1] in regs:
                regs[split[1]] += 1

        if 'dec' in line:
            if split[1] in regs:
                regs[split[1]] -= 1

        if 'tgl' in line:
            target = get_val(split[1], regs) + cur
            if target < len(inp):
                ins = inp[target]
                split_ = ins.split()
                if len(split_) == 2:
                    if 'inc' in ins:
                        inp[target] = f'dec {split_[1]}'
                    else:
                        inp[target] = f'inc {split_[1]}'

                if len(split_) == 3:
                    if 'jnz' in ins:
                        inp[target] = f'cpy {split_[1]} {split_[2]}'
                    else:
                        inp[target] = f'jnz {split_[1]} {split_[2]}'

        if 'out' in line:
            yield get_val(split[1], regs)

        if 'jnz' in line:
            if get_val(split[1], regs) != 0:
                cur += get_val(split[2], regs)
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
    with open('input/day25.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
