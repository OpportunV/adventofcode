from collections import defaultdict


def part_one(inp):
    moves = {
        '^': lambda ps: (ps[0], ps[1] + 1),
        '>': lambda ps: (ps[0] + 1, ps[1]),
        'v': lambda ps: (ps[0], ps[1] - 1),
        '<': lambda ps: (ps[0] - 1, ps[1]),
    }
    
    pos = 0, 0
    houses = {pos}
    for move in inp:
        pos = moves[move](pos)
        houses.add(pos)
    
    return houses
    

def part_two(inp):
    return part_one(inp[::2]) | part_one(inp[1::2])


def main():
    with open('d3_input.txt') as fin:
        inp = fin.read()
    
    print(len(part_one(inp)))
    print(len(part_two(inp)))
    
    
if __name__ == '__main__':
    main()
