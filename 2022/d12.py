from collections import deque


def bfs(start, end, field):
    q = deque()
    q.append((start, 0))
    seen = set()
    while q:
        coord, cost = q.popleft()
        i, j = coord
        if field[i][j] == end:
            return cost
        
        if coord in seen:
            continue
        
        seen.add(coord)
        
        for (ii, jj) in neighbours(i, j, field):
            if ord(field[ii][jj]) - ord(field[i][j]) <= 1 or field[ii][jj] == end:
                q.append(((ii, jj), cost + 1))


def neighbours(i, j, field):
    if i - 1 >= 0:
        yield i - 1, j
    
    if i + 1 < len(field):
        yield i + 1, j
    
    if j - 1 >= 0:
        yield i, j - 1
    
    if j + 1 < len(field[0]):
        yield i, j + 1


def part_one(inp):
    field = [list(line) for line in inp]
    start = 0, 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'S':
                start = i, j
                field[i][j] = 'a'
    
    return bfs(start, 'E', field)


def part_two(inp):
    field = [list(line) for line in inp]
    starts = []
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'S':
                field[i][j] = 'a'
                starts.append((i, j))
            
            if field[i][j] == 'a':
                starts.append((i, j))
    
    return min(filter(lambda x: type(x) is int, [bfs(start, 'E', field) for start in starts]))


def main():
    with open(r'd12_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
