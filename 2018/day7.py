from collections import defaultdict, deque


def part_one(inp):
    steps = defaultdict(list)
    counter = defaultdict(int)
    for line in inp:
        splt = line.split()
        steps[splt[1]].append(splt[-3])
        counter[splt[-3]] += 1
    
    queue = deque()
    for step in steps:
        if counter[step] == 0:
            queue.append(step)
            
    queue = deque(sorted(queue))
    
    ans = ""
    while queue:
        cur = queue.popleft()
        ans += cur
        for dependence in steps[cur]:
            counter[dependence] -= 1
            if counter[dependence] == 0:
                queue.append(dependence)

        queue = deque(sorted(queue))
    
    return ans


def part_two(inp):
    steps = defaultdict(list)
    counter = defaultdict(int)
    for line in inp:
        splt = line.split()
        steps[splt[1]].append(splt[-3])
        counter[splt[-3]] += 1
    
    queue = deque()
    for step in steps:
        if counter[step] == 0:
            queue.append(step)
    
    queue = deque(sorted(queue))
    workers_amount = 5
    workers = [(0, None) for _ in range(workers_amount)]
    
    time = 0
    while True:
        for i in range(workers_amount):
            if workers[i][1] is None and queue:
                cur = queue.popleft()
                workers[i] = (time + ord(cur) - 4, cur)
                
            queue = deque(sorted(queue))

        time += 1
        for i in range(workers_amount):
            if workers[i][0] == time and workers[i][1] is not None:
                cur = workers[i][1]
                workers[i] = (time, None)
                for dependence in steps[cur]:
                    counter[dependence] -= 1
                    if counter[dependence] == 0:
                        queue.append(dependence)
        
        if not queue and not any(map(lambda item: item[1], workers)):
            return time


def main():
    with open(r'input\day7.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
