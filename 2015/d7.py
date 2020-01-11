def part_one(inp):
    connections = {}
    solved = {}
    for line in inp:
        if 'NOT' in line:
            _, cur, _, tar = line.split()
            connections[tar] = ['~', cur]
        elif 'AND' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['&', cur1, cur2]
        elif 'OR' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['|', cur1, cur2]
        elif 'LSHIFT' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['<<', cur1, cur2]
        elif 'RSHIFT' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['>>', cur1, cur2]
        else:
            cur, _, tar = line.split()
            if cur.isdigit():
                solved[tar] = int(cur)
            else:
                connections[tar] = [cur]
    
    def find(target):
        if target in solved:
            return
        if target.isdigit():
            solved[target] = int(target)
            return
        if len(connections[target]) == 1:
            find(connections[target][0])
            solved[target] = solved[connections[target][0]]
            return
        op, *args = connections[target]
        find(args[0])
        if op == '~':
            solved[target] = ~solved[args[0]]
            return
        find(args[1])
        solved[target] = eval(f'{solved[args[0]]}{op}{solved[args[1]]}')
    
    find('a')
    return solved['a']
        

def part_two(inp):
    connections = {}
    solved = {}
    for line in inp:
        if 'NOT' in line:
            _, cur, _, tar = line.split()
            connections[tar] = ['~', cur]
        elif 'AND' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['&', cur1, cur2]
        elif 'OR' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['|', cur1, cur2]
        elif 'LSHIFT' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['<<', cur1, cur2]
        elif 'RSHIFT' in line:
            cur1, _, cur2, _, tar = line.split()
            connections[tar] = ['>>', cur1, cur2]
        else:
            cur, _, tar = line.split()
            if cur.isdigit():
                solved[tar] = int(cur)
            else:
                connections[tar] = [cur]
    
    def find(target):
        if target in solved:
            return
        if target.isdigit():
            solved[target] = int(target)
            return
        if len(connections[target]) == 1:
            find(connections[target][0])
            solved[target] = solved[connections[target][0]]
            return
        op, *args = connections[target]
        find(args[0])
        if op == '~':
            solved[target] = ~solved[args[0]]
            return
        find(args[1])
        solved[target] = eval(f'{solved[args[0]]}{op}{solved[args[1]]}')
    
    tmp = solved.copy()
    find('a')
    tmp['b'] = solved['a']
    solved = tmp
    find('a')
    return solved['a']


def main():
    with open('d7_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
