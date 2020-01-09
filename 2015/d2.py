def part_one(data):
    total = 0
    for x, y, z in data:
        total += 3 * x * y
        total += 2 * x * z
        total += 2 * y * z
    
    return total


def part_two(data):
    total = 0
    for x, y, z in data:
        total += 2 * x + 2 * y
        total += x * y * z
    
    return total


def main():
    with open('d2_input.txt') as fin:
        data = [sorted([int(i) for i in line.split('x')]) for line in fin.readlines()]
    
    print(part_one(data))
    print(part_two(data))
    

if __name__ == '__main__':
    main()
