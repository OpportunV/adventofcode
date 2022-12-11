MOVES = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
}


class Knot:
    @staticmethod
    def one():
        return Knot(1, 1)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Knot(self.x - other.x, self.y - other.y)
    
    def __abs__(self):
        return Knot(abs(self.x), abs(self.y))
    
    def __gt__(self, other):
        return self.x > other.x or self.y > other.y
    
    @property
    def position(self):
        return self.x, self.y
    
    @property
    def norm(self):
        return Knot(int(self.x / abs(self.x)) if self.x != 0 else 0, int(self.y / abs(self.y)) if self.y != 0 else 0)
    
    def move(self, direction):
        x, y = direction
        self.x += x
        self.y += y


class Head(Knot):
    pass


class Tail(Knot):
    def __init__(self, x, y, parent):
        super().__init__(x, y)
        self.visited = set()
        self.visited.add(self.position)
        self.parent = parent
    
    def move(self, direction=None):
        dk = self.parent - self
        if abs(dk) > Knot.one():
            dx = dk.norm.x
            dy = dk.norm.y
            super(Tail, self).move((dx, dy))
        self.visited.add(self.position)


def part_one(inp):
    head = Head(0, 0)
    tail = Tail(0, 0, head)
    for line in inp:
        direction, amount = line.split()
        for i in range(int(amount)):
            head.move(MOVES[direction])
            tail.move()
    
    return len(tail.visited)


def part_two(inp):
    head = Head(0, 0)
    tails = [Tail(0, 0, head)]
    for i in range(1, 9):
        tails.append(Tail(0, 0, tails[i - 1]))
    
    for line in inp:
        direction, amount = line.split()
        for i in range(int(amount)):
            head.move(MOVES[direction])
            for tail in tails:
                tail.move()
    
    return len(tails[-1].visited)


def main():
    with open(r'd9_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
