def part_one(inp):
    return sum(len(line) - len(eval(line)) for line in inp)


def part_two(inp):
    return sum(2 + line.count('\\')+line.count('"') for line in inp)


def main():
    with open('d8_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
