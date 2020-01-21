from collections import defaultdict


def part_one(inp, time=2503):
    deers = parse_inp(inp)
    dists = set()
    for deer in deers:
        v, mt, rt = deers[deer].values()
        cycles = time // (mt + rt)
        dists.add(cycles * mt * v + v * min(mt, time - cycles * (mt + rt)))
    return max(dists)


def part_two(inp, time=2503):
    deers = parse_inp(inp)
    for deer in deers:
        deers[deer]['dist'] = 0
        deers[deer]['stars'] = 0
    for i in range(1, time + 1):
        cur_max = 0
        for deer in deers:
            v, mt, rt, *_ = deers[deer].values()
            if 0 < i % (mt + rt) <= mt:
                deers[deer]['dist'] += v
            cur_max = max(cur_max, deers[deer]['dist'])
        for deer in deers:
            if deers[deer]['dist'] == cur_max:
                deers[deer]['stars'] += 1
    return max({deers[deer]['stars'] for deer in deers})


def parse_inp(inp):
    deers = defaultdict(dict)
    for line in inp:
        tmp = line.split()
        name, speed, movetime, resttime = tmp[0], int(tmp[3]), int(tmp[6]), int(tmp[-2])
        deers[name]['speed'] = speed
        deers[name]['movetime'] = movetime
        deers[name]['resttime'] = resttime
    
    return deers


def main():
    with open('d14_input.txt') as fin:
        inp = fin.read().splitlines()
        
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
