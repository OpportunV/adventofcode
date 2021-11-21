import re


def part_both(inp):
    return simulate(set(inp))


def simulate(data):
    time = 0
    while True:
        new = set()
        time += 1
        for x, y, vx, vy in data:
            new.add((x + vx, y + vy, vx, vy))
        
        y_min = min(new, key=lambda item: item[1])[1]
        y_max = max(new, key=lambda item: item[1])[1]
        if y_max - y_min < 11:
            pos = set(map(lambda item: (item[0], item[1]), new))
            x_min = min(new, key=lambda item: item[0])[0]
            x_max = max(new, key=lambda item: item[0])[0]
            for y in range(y_min, y_max + 1):
                for x in range(x_min - 1, x_max + 2):
                    if (x, y) in pos:
                        print('#', end='')
                    else:
                        print(' ', end='')
                        
                print()
                
            return time
        
        data = new


def main():
    with open(r'input\day10.txt') as fin:
        inp = fin.read().splitlines()
        
    inp = [tuple(map(int, re.findall(r'-?\d+', line))) for line in inp]
    
    print(part_both(inp))
    
    
if __name__ == '__main__':
    main()
