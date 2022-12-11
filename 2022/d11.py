import operator
from collections import deque
from functools import reduce


class Monkey:
    monkeys = []
    common_divider = 1
    worry_level_divider = 1
    
    def __init__(self, items, sign, operation_arg, test, test_results):
        self.index = len(Monkey.monkeys)
        self.items = deque(items)
        self.operator = sign
        self.operation_arg = operation_arg
        self.test = test
        self.test_results = test_results
        self.inspected = 0
        Monkey.monkeys.append(self)
    
    def __add__(self, other):
        self.items.append(other % Monkey.common_divider)
        return self
    
    def __repr__(self):
        return f'< Monkey {self.index}: items {self.items}, inspected {self.inspected} >'
    
    def inspect(self):
        for i in range(len(self.items)):
            self.inspected += 1
            cur = self.items.popleft()
            
            arg = cur
            if self.operation_arg is not None:
                arg = self.operation_arg
            
            if self.operator == '*':
                cur *= arg
            else:
                cur += arg
            
            cur //= Monkey.worry_level_divider
            Monkey.monkeys[self.test_results[cur % self.test == 0]] += cur
    
    @classmethod
    def round(cls):
        for monkey in cls.monkeys:
            monkey.inspect()
    
    @classmethod
    def calc_dividers(cls, value=1):
        cls.worry_level_divider = value
        cls.common_divider = reduce(operator.mul, map(lambda monkey: monkey.test, cls.monkeys))
    
    @staticmethod
    def parse(inp):
        Monkey.monkeys.clear()
        cur_ind = 0
        while cur_ind < len(inp):
            items = map(int, inp[cur_ind + 1].split(':')[1].strip().split(','))
            expression = inp[cur_ind + 2].split('=')[1].strip().split()
            assert expression[0] == 'old'
            sign = expression[1]
            operation_arg = int(expression[2]) if expression[2].isnumeric() else None
            
            test = int(inp[cur_ind + 3].split()[-1])
            test_results = {
                True: int(inp[cur_ind + 4].split()[-1]),
                False: int(inp[cur_ind + 5].split()[-1])
            }
            
            Monkey(items, sign, operation_arg, test, test_results)
            cur_ind += 7


def part_one(inp):
    Monkey.parse(inp)
    Monkey.calc_dividers(3)
    for i in range(20):
        Monkey.round()
    
    inspected = list(sorted(map(lambda monkey: monkey.inspected, Monkey.monkeys), reverse=True))
    return inspected[0] * inspected[1]


def part_two(inp):
    Monkey.parse(inp)
    Monkey.calc_dividers()
    for i in range(10000):
        Monkey.round()
    
    inspected = list(sorted(map(lambda monkey: monkey.inspected, Monkey.monkeys), reverse=True))
    return inspected[0] * inspected[1]


def main():
    with open(r'd11_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
