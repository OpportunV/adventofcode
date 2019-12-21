from collections import defaultdict, deque


def part_one(maze):
    portals = defaultdict(list)
    paths = defaultdict(set)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j].isupper():
                coords = port_name = None
                for x, y in adjacent((i, j)):
                    try:
                        cur = maze[x][y]
                    except IndexError:
                        continue
                    if cur.isupper():
                        port_name = ''.join(sorted(maze[i][j] + cur))
                        for a, b in adjacent((x, y)):
                            try:
                                if maze[a][b] == '.':
                                    coords = a, b
                            except IndexError:
                                continue
                        
                    if cur == '.':
                        coords = x, y
                portals[port_name].append(coords)
            
            if maze[i][j] == '.':
                for x, y in adjacent((i, j)):
                    if maze[x][y] == '.':
                        paths[(i, j)].add((x, y))
                        paths[(x, y)].add((i, j))
       
    for port in portals:
        portals[port] = list(set(portals[port]))
        if port == 'AA' or port == 'ZZ' or len(portals[port]) != 2:
            continue
        pos1, pos2 = portals[port]
        paths[pos1].add(pos2)
        paths[pos2].add(pos1)
        
    visited = set()
    to_check = deque()
    to_check.append((portals['AA'][0], 0))
    
    while to_check:
        pos, d = to_check.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        if pos == portals['ZZ'][0]:
            return d
        
        for path in paths[pos]:
            to_check.append((path, d+1))


def part_two(maze):
    portals = defaultdict(dict)
    port_names = {}
    paths = defaultdict(set)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j].isupper():
                coords = port_name = outer = None
                for x, y in adjacent((i, j)):
                    if x < 0 or y < 0:
                        continue
                    try:
                        cur = maze[x][y]
                    except IndexError:
                        continue
                    if cur.isupper():
                        port_name = ''.join(sorted(maze[i][j] + cur))
                        outer = (x <= 3 or y <= 3 or x >= len(maze) - 3 or y >= len(maze[x]) - 3)
                        for a, b in adjacent((x, y)):
                            if a < 0 or b < 0:
                                continue
                            try:
                                if maze[a][b] == '.':
                                    coords = a, b
                            except IndexError:
                                continue
                    
                    if cur == '.':
                        coords = x, y
                portals[port_name][outer] = coords
                port_names[coords] = (port_name, outer)
            
            if maze[i][j] == '.':
                for x, y in adjacent((i, j)):
                    if maze[x][y] == '.':
                        paths[(i, j)].add((x, y))
                        paths[(x, y)].add((i, j))
            
    def get_paths(state):
        pos, lvl = state
        ans = []
        for path in paths[pos]:
            ans.append((path, lvl))
        
        if pos in port_names:
            port_name, outer = port_names[pos]
            if port_name == 'AA' or port_name == "ZZ":
                pass
            elif outer and lvl > 0:
                ans.append((portals[port_name][not outer], lvl - 1))
            elif not outer:
                ans.append((portals[port_name][not outer], lvl + 1))
        return ans
    
    visited = set()
    to_check = deque()
    to_check.append((portals['AA'][1], 0, 0))
    
    while to_check:
        pos, d, lvl = to_check.popleft()
        if (pos, lvl) in visited:
            continue
        visited.add((pos, lvl))
        
        if pos == portals['ZZ'][1] and lvl == 0:
            return d
        
        for nxt_pos, nxt_lvl in get_paths((pos, lvl)):
            to_check.append((nxt_pos, d + 1, nxt_lvl))
    return False
    
    
def adjacent(pos):
    x, y = pos
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    

def main():
    with open('d20_input.txt') as fin:
        maze = []
        for line in fin.read().splitlines():
            maze.append(list(line))
            
    print(part_one(maze))
    print(part_two(maze))


if __name__ == '__main__':
    main()
