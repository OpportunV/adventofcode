def part_one(inp):
    for target in range(inp // 100, inp, 1):
        numbers = set()
        for i in range(1, int(target ** .5)):
            if target % i == 0:
                numbers.add(i)
                numbers.add(target // i)
        if sum(numbers) * 10 >= inp:
            return target


def part_two(inp):
    for target in range(inp // 100, inp, 1):
        numbers = set()
        for i in range(1, 51):
            if target % i == 0:
                numbers.add(target // i)
        if sum(numbers) * 11 >= inp:
            return target


def main():
    inp = 29000000
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
