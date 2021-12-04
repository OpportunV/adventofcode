import re
from z3 import *


def part_one(inp):
    cur_x, cur_y, cur_z, r = max(inp, key=lambda item: item[3])
    ans = 0
    for x, y, z, _ in inp:
        if abs(cur_x - x) + abs(cur_y - y) + abs(cur_z - z) <= r:
            ans += 1
    
    return ans


def part_two(inp):
    def zabs(t):
        return If(t >= 0, t, -t)
    
    (x, y, z) = (Int('x'), Int('y'), Int('z'))
    in_ranges = [
        Int('in_range_' + str(i)) for i in range(len(inp))
    ]
    range_count = Int('sum')
    o = Optimize()
    for i in range(len(inp)):
        nx, ny, nz, nrng = inp[i]
        o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= nrng, 1, 0))
    o.add(range_count == sum(in_ranges))
    dist_from_zero = Int('dist')
    o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))
    o.maximize(range_count)
    h2 = o.minimize(dist_from_zero)
    
    return o.lower(h2)


def main():
    with open(r'input\day23.txt') as fin:
        inp = fin.read().splitlines()
        
    inp = [tuple(int(i) for i in re.findall(r'-?\d+', line)) for line in inp]
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
