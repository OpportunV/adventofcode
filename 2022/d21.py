OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: int(a / b),
    '*': lambda a, b: a * b,
}

TARGET_MONKEY = 'root'
HUMAN = 'humn'


def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def evaluate_root(raw_monkeys):
    monkeys = {}
    sign = 0
    while TARGET_MONKEY not in monkeys:
        to_remove = []
        for monkey, data in raw_monkeys.items():
            if is_number(data):
                monkeys[monkey] = int(data)
                to_remove.append(monkey)
            else:
                left, op, right = data.split()
                if left in monkeys and right in monkeys:
                    if monkey == TARGET_MONKEY:
                        sign = monkeys[left] - monkeys[right]
                    
                    monkeys[monkey] = OPERATIONS[op](monkeys[left], monkeys[right])
                    to_remove.append(monkey)
        
        for monkey in to_remove:
            raw_monkeys.pop(monkey)
    
    return monkeys, sign


def part_one(inp):
    raw_monkeys = {a.split(': ')[0]: a.split(': ')[1] for a in inp}
    monkeys = evaluate_root(raw_monkeys)[0]
    
    return monkeys[TARGET_MONKEY]


def part_two(inp):
    raw_monkeys = {a.split(': ')[0]: a.split(': ')[1] for a in inp}
    step = 10 ** (len(str(part_one(inp))) - 1)
    raw_monkeys[HUMAN] = f'{step * 10}'
    diff = evaluate_root(raw_monkeys.copy())[1]
    while diff != 0:
        new_diff = evaluate_root(raw_monkeys.copy())[1]
        if (diff > 0) != (new_diff > 0):
            step //= 10
        
        last_val = int(raw_monkeys[HUMAN])
        if (abs(new_diff) - abs(diff)) > 0:
            step = -step
        
        diff = new_diff
        raw_monkeys[HUMAN] = f'{last_val + step}'
    
    return raw_monkeys[HUMAN]


def main():
    with open(r'd21_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
