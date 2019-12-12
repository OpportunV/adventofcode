class Wire:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.path = []
    
    @property
    def pos(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        return f'position x: {self.x}, y: {self.y}'
    
    def r(self, value):
        stop = self.x + value
        while self.x < stop:
            self.x += 1
            self.path.append(self.pos)
        
        return self

    def l(self, value):
        stop = self.x - value
        while self.x > stop:
            self.x -= 1
            self.path.append(self.pos)
            
        return self

    def u(self, value):
        stop = self.y + value
        while self.y < stop:
            self.y += 1
            self.path.append(self.pos)
            
        return self

    def d(self, value):
        stop = self.y - value
        while self.y > stop:
            self.y -= 1
            self.path.append(self.pos)
        return self
        
    def move(self, path):
        for string in path:
            direction = string[0].lower()
            value = int(string[1:])
            eval(f'self.{direction}({value})')
        return self
    
    def m_dist(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)


def part_one(p1, p2):
    w1 = Wire(0, 0)
    w2 = Wire(0, 0)
    
    w1.move(p1)
    w2.move(p2)
    
    intersections = set(w1.path) & set(w2.path)
    
    dist = min([Wire(*i).m_dist(Wire()) for i in intersections])
    print(f'{dist=}')

    shortest_time = float('inf')
    for i in intersections:
        ind1 = w1.path.index(i)
        ind2 = w2.path.index(i)
        shortest_time = min(shortest_time,
                            len(w1.path[:ind1 + 1]) + len(w2.path[:ind2 + 1]))
            
    print(f'{shortest_time=}')
    
    return intersections
    

with open('d3_input.txt') as fin:
    w1_path = fin.readline().split(',')
    
    w2_path = fin.readline().split(',')

    
part_one(w1_path, w2_path)
