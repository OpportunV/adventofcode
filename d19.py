from intcode_computer import IntcodeComputer


def part_one(intcode):
    ans = []
    total = 0
    for i in range(50):
        line = []
        for j in range(50):
            comp = IntcodeComputer(0, intcode.copy())
            comp.cor.send(i)
            reply = comp.cor.send(j)
            total += reply
            line.append(reply)
        ans.append(line)
    
    for line in ans:
        print(''.join(str(i) for i in line))
    
    return total


def get_reply(x, y, intcode):
    comp = IntcodeComputer(0, intcode)
    comp.cor.send(x)
    return comp.cor.send(y)


def part_two(intcode):
    side = 100 - 1
    x = 0
    y = side
    
    while True:
        
        while get_reply(x, y, intcode) == 0:
            x += 1
        
        if get_reply(x + side, y - side, intcode) == 1:
            return 10000 * x + y - side
        
        y += 1


def main():
    with open('d19_input.txt') as fin:
        intc = [int(i) for i in fin.readline().split(',')]
    
    # print(part_one(intc))
    print(part_two(intc))


if __name__ == '__main__':
    main()
