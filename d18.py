def part_one(maze):
    keys = {}
    doors = {}
    walls = set()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            cur = maze[i][j]
            if cur == '@':
                maze[i][j] = '.'
                keys[cur] = (i, j)
            elif cur.isalpha():
                if cur.islower():
                    keys[cur] = (i, j)
                else:
                    doors[cur] = (i, j)
            elif cur == '#':
                walls.add((i, j))

    key_map = {}
    for key in keys:
        key_pos = keys[key]
        to_check = set()
        to_check.add(key_pos)
        moves = {}
        blocked = set(walls)
        key_map[key] = {}
        
        while to_check:
            cur_check = to_check
            to_check = set()
            blocked = blocked.union(cur_check)
            for pos in cur_check:
                next_moves = {i for i in adjacent(pos)} - blocked
                to_check = to_check.union(next_moves)
                    
                for ps in next_moves:
                    moves[ps] = pos
        
        for k in keys:
            if k == '@':
                continue
            keys_by_way = set()
            doors_by_way = set()
            pos = keys[k]
            dist = 0
            while pos in moves:
                tmp = maze[pos[0]][pos[1]]
                if tmp in keys:
                    if tmp == '@':
                        continue
                    keys_by_way.add(tmp)
                elif tmp in doors:
                    doors_by_way.add(tmp.lower())
                pos = moves[pos]
                dist += 1

            key_map[key][k] = (k, dist, keys_by_way, doors_by_way)
            
    cache = {}
    
    def search(cur, collected=None, steps=0):
        if collected is None:
            collected = set()

        if collected == set(keys.keys()) - {'@'}:
            return steps
        state = tuple(sorted(collected) + [cur])

        if state in cache:
            return cache[state] + steps
        
        tmp_steps = float('inf')
        for key in keys:
            if key in collected or key == '@':
                continue
            k, dist, keys_by_way, doors_by_way = key_map[cur][key]
            if not doors_by_way.issubset(collected):
                continue
            tmp_steps = min(tmp_steps, search(k, collected.union(keys_by_way), dist))
        cache[state] = tmp_steps
        return tmp_steps + steps
    
    return search('@')
        

def adjacent(pos):
    x, y = pos
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def part_two(maze):
    keys = {}
    doors = {}
    walls = set()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            cur = maze[i][j]
            if cur.isdigit():
                maze[i][j] = '.'
                keys[cur] = (i, j)
            elif cur.isalpha():
                if cur.islower():
                    keys[cur] = (i, j)
                else:
                    doors[cur] = (i, j)
            elif cur == '#':
                walls.add((i, j))
    
    key_map = {}
    robots = list('1234')
    for key in keys:
        key_pos = keys[key]
        to_check = set()
        to_check.add(key_pos)
        moves = {}
        blocked = set(walls)
        key_map[key] = {}
        
        while to_check:
            cur_check = to_check
            to_check = set()
            blocked = blocked.union(cur_check)
            for pos in cur_check:
                next_moves = {i for i in adjacent(pos)} - blocked
                to_check = to_check.union(next_moves)
                
                for ps in next_moves:
                    moves[ps] = pos
        
        for k in keys:
            if k in robots:
                continue
            keys_by_way = set()
            doors_by_way = set()
            pos = keys[k]
            dist = 0
            while pos in moves:
                tmp = maze[pos[0]][pos[1]]
                if tmp in keys:
                    if tmp in robots:
                        continue
                    keys_by_way.add(tmp)
                elif tmp in doors:
                    doors_by_way.add(tmp.lower())
                pos = moves[pos]
                dist += 1
            
            key_map[key][k] = (k, dist, keys_by_way, doors_by_way)
    print(key_map)
    cache = {}
    
    def search(rbts, collected=None, steps=0):
        if collected is None:
            collected = set()
        
        if collected == set(keys.keys()).difference(set(robots)):
            return steps
        state = tuple(sorted(collected) + rbts)
        
        if state in cache:
            return cache[state] + steps
        
        tmp_steps = float('inf')

        for robot in rbts:
            for key in (set(keys) - collected - set(robots)):
                k, dist, keys_by_way, doors_by_way = key_map[robot][key]
                if (doors_by_way - collected) or not dist:
                    continue
                new_rbts = [k if robot == rbt else rbt for rbt in rbts]
                tmp_search = search(new_rbts, collected | keys_by_way, dist)
                print(tmp_search)
                tmp_steps = min(tmp_steps, tmp_search)
        
        cache[state] = tmp_steps
        return tmp_steps + steps
    
    return search(robots)


def main():
    with open('d18_input.txt') as fin:
        maze = fin.read().splitlines()

    maze = [list(i) for i in maze]

    # print(part_one(maze))
    
    with open('d18_2_input.txt') as fin:
        maze = fin.read().splitlines()

    maze = [list(i) for i in maze]

    print(part_two(maze))


if __name__ == '__main__':
    main()
