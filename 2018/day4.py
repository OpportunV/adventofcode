import re
from collections import defaultdict, Counter
from functools import reduce


def part_one(inp):
    guards = defaultdict(list)
    guards_time = defaultdict(int)
    cur_id = 0
    start_sleep = 0
    for line in inp:
        if "falls" in line:
            start_sleep = int(re.findall(r':\d+', line)[0][1:])
        if "wakes" in line:
            cur = int(re.findall(r':\d+', line)[0][1:])
            guards[cur_id].append({i for i in range(start_sleep, cur)})
            guards_time[cur_id] += (cur - start_sleep)
        if "begins" in line:
            cur_id = int(re.findall(r'#\d+', line)[0][1:])
    
    top = 0
    cur = None
    for k, v in guards_time.items():
        if v > top:
            top = v
            cur = k

    counted = reduce(lambda x, y: Counter(x) + Counter(y), guards[cur], Counter())
    return counted.most_common(1)[0][0] * cur


def part_two(inp):
    guards = defaultdict(int)
    cur_id = 0
    start_sleep = 0
    for line in inp:
        if "falls" in line:
            start_sleep = int(re.findall(r':\d+', line)[0][1:])
        if "wakes" in line:
            cur = int(re.findall(r':\d+', line)[0][1:])
            for i in range(start_sleep, cur):
                guards[(cur_id, i)] += 1
        if "begins" in line:
            cur_id = int(re.findall(r'#\d+', line)[0][1:])
    
    guard, minute, *_ = max([(k[0], k[1], c) for k, c in guards.items()], key=lambda item: item[2])
    
    return guard * minute


def main():
    with open(r'input\day4.txt') as fin:
        inp = fin.read().splitlines()
    
    inp = sorted(inp)
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
