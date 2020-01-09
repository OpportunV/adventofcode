def part_one(inp):
    def check_line(line):
        vowels = 'aeiou'
        forbidden = ['ab', 'cd', 'pq', 'xy']
        for i in forbidden:
            if i in line:
                return 0
        
        if sum([line.count(i) for i in vowels]) < 3:
            return 0
        
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                return 1
        
        return 0
    
    return sum([check_line(line) for line in inp])


def part_two(inp):
    def check_line(line):
        doubles = False
        for i in range(len(line) - 1):
            if doubles:
                break
            cur = line[i] + line[i + 1]
            for j in range(i + 2, len(line) - 1):
                if line[j] + line[j + 1] == cur:
                    doubles = True
        if not doubles:
            return 0
    
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                return 1
        return 0
    
    return sum([check_line(line) for line in inp])


def main():
    with open('d5_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
