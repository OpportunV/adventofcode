def part_one(inp):
    connections, solved = parse_inp(inp)
    find('a', solved, connections)
    return solved['a']
        

def part_two(inp):
    connections, solved = parse_inp(inp)
    
    tmp = solved.copy()
    find('a', solved, connections)
    tmp['b'] = solved['a']
    solved = tmp
    find('a', solved, connections)
    return solved['a']


def parse_inp(inp):
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
                
    return connections, solved


def find(target, solved, connections):
    if target in solved:
        return
    if target.isdigit():
        solved[target] = int(target)
        return
    if len(connections[target]) == 1:
        find(connections[target][0], solved, connections)
        solved[target] = solved[connections[target][0]]
        return
    op, *args = connections[target]
    find(args[0], solved, connections)
    if op == '~':
        solved[target] = ~solved[args[0]]
        return
    find(args[1], solved, connections)
    solved[target] = eval(f'{solved[args[0]]}{op}{solved[args[1]]}')


def main():
    with open('d7_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
