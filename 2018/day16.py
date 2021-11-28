def addr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + result[b]
    return result


def addi(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + b
    return result


def mulr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * result[b]
    return result


def muli(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * b
    return result


def banr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & result[b]
    return result


def bani(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & b
    return result


def borr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | result[b]
    return result


def bori(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | b
    return result


def setr(registers, a, _, c):
    result = registers[::]
    result[c] = result[a]
    return result


def seti(registers, a, _, c):
    result = registers[::]
    result[c] = a
    return result


def gtir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a > result[b])
    return result


def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > b)
    return result


def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > result[b])
    return result


def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a == result[b])
    return result


def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == b)
    return result


def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == result[b])
    return result


OPERATIONS = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


def possible_operations(instruction, before, after):
    result = set()
    for operation in OPERATIONS:
        op_result = operation(before, *instruction[1:])
        if op_result == after:
            result.add(operation)
    return result


def get_experiments(inp):
    i = 0
    experiments = []
    while inp[i].strip():
        before, instruction, after = inp[i:i + 3]
        i += 4
        experiments.append((
            list(map(int, instruction.split(' '))),
            eval(before[8:]),
            eval(after[8:])
        ))
    
    return experiments, i


def part_one(inp):
    experiments, _ = get_experiments(inp)
    return len([experiment for experiment in experiments if len(possible_operations(*experiment)) >= 3])


def part_two(inp):
    experiments, i = get_experiments(inp)
    
    operations = {opcode: set(OPERATIONS) for opcode in range(16)}
    for experiment in experiments:
        opcode = experiment[0][0]
        operations[opcode].intersection_update(possible_operations(*experiment))
    
    while True:
        unique_ops = {}
        for op, ops in operations.items():
            if len(ops) == 1:
                unique_ops[op] = ops
        for op_, ops_ in unique_ops.items():
            for op, ops in operations.items():
                if op != op_:
                    ops.difference_update(ops_)
        if len(unique_ops) == len(operations):
            break
    
    for op in operations:
        operations[op] = operations[op].pop()
    registers = [0, 0, 0, 0]
    for line in inp[i:]:
        if not line.strip():
            continue
        opcode, a, b, c = list(map(int, line.split(' ')))
        registers = operations[opcode](registers, a, b, c)
    return registers[0]


def main():
    with open(r'input\day16.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
