def part_one(inp):
    max_cal = 0
    subtotal = 0
    for line in inp:
        if line == '':
            max_cal = max(max_cal, subtotal)
            subtotal = 0
            continue
        
        subtotal += int(line)
    
    max_cal = max(max_cal, subtotal)
    
    return max_cal


def part_two(inp):
    totals = []
    subtotal = 0
    for line in inp:
        if line == '':
            totals.append(subtotal)
            subtotal = 0
            continue
        
        subtotal += int(line)
    
    totals.append(subtotal)
    totals.sort(reverse=True)
    
    return sum(totals[:3])


def main():
    with open(r'd1_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
