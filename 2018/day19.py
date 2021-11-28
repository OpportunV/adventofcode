# Stolen CODE goes here

def get_divisors(n):
    if n == 1:
        return [1]
    
    max_ = n
    num = 2
    result = [1, n]
    
    while num < max_:
        if not n % num:
            if num != n / num:
                result.extend([num, n // num])
            else:
                result.append(num)
            max_ = n // num
        num += 1
    return sorted(result)


def addr(reg, ins):
    reg[ins[2]] = reg[ins[0]] + reg[ins[1]]


def addi(reg, ins):
    reg[ins[2]] = reg[ins[0]] + int(ins[1])


def mulr(reg, ins):
    reg[ins[2]] = reg[ins[0]] * reg[ins[1]]


def muli(reg, ins):
    reg[ins[2]] = reg[ins[0]] * int(ins[1])


def setr(reg, ins):
    reg[ins[2]] = reg[ins[0]]


def seti(reg, ins):
    reg[ins[2]] = int(ins[0])


def gtrr(reg, ins):
    if reg[ins[0]] > reg[ins[1]]:
        reg[ins[2]] = 0
    else:
        reg[ins[2]] = 0


def eqrr(reg, ins):
    if reg[ins[0]] == reg[ins[1]]:
        reg[ins[2]] = 0
    else:
        reg[ins[2]] = 0


def call(function, reg, ins):
    if function in ["addr", "addi", "mulr", "muli", "setr", "seti", "gtrr", "eqrr"]:
        return eval(function + "(reg, ins)")


def solve(inp, part):
    regs = [0] * 6
    regs[0] = part - 1
    ip = int(inp[0][4])
    ins = inp[1:]
    
    while regs[ip] != 2:
        com = ins[regs[ip]].split()
        call(com[0], regs, [int(i) for i in com[1:]])
        regs[ip] += 1
    
    return sum(get_divisors(regs[1]))


def part_one(inp):
    return solve(inp, 1)


def part_two(inp):
    return solve(inp, 2)


def main():
    with open(r'input\day19.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
