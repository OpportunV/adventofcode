from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y', 'z'])


def adjacent(x, y, z):
    yield Pos(x - 1, y, z)
    yield Pos(x + 1, y, z)
    yield Pos(x, y - 1, z)
    yield Pos(x, y + 1, z)
    yield Pos(x, y, z - 1)
    yield Pos(x, y, z + 1)


def part_one(inp, res=[]):
    if res:
        return res[0]
    
    field = {}
    for line in inp:
        pos = Pos(*map(int, line.split(',')))
        field[pos] = 6
        for neighbour in adjacent(*pos):
            if neighbour in field:
                field[pos] -= 1
                field[neighbour] -= 1
    
    res.append(sum(field.values()))
    return res[0]


def part_two(inp):
    field = set()
    for line in inp:
        x, y, z = map(int, line.split(','))
        field.add(Pos(x, y, z))
    
    min_pos = Pos(min(map(lambda cube: cube.x, field)), min(map(lambda cube: cube.y, field)),
                  min(map(lambda cube: cube.z, field)))
    max_pos = Pos(max(map(lambda cube: cube.x, field)), max(map(lambda cube: cube.y, field)),
                  max(map(lambda cube: cube.z, field)))
    
    air = set()
    q = set()
    q.add(min_pos)
    
    while q:
        cur = q.pop()
        if cur in air:
            continue
        
        air.add(cur)
        
        for pos in adjacent(*cur):
            if pos.x < min_pos.x or pos.y < min_pos.y or pos.z < min_pos.z \
                    or pos.x > max_pos.x or pos.y > max_pos.y or pos.z > max_pos.z:
                continue
            
            if pos in field:
                continue
            
            q.add(pos)
    
    total = 0
    for x in range(min_pos.x, max_pos.x + 1):
        for y in range(min_pos.y, max_pos.y + 1):
            for z in range(min_pos.z, max_pos.z + 1):
                cur = Pos(x, y, z)
                if cur in field:
                    continue
                
                if cur in air:
                    continue
                
                total += len(list(filter(lambda block: block in field, adjacent(*cur))))
    
    return part_one(inp) - total


def main():
    with open(r'd18_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
