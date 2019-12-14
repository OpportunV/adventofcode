from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        
    @property
    def pot_en(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    
    @property
    def kin_en(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)
    
    @property
    def total_en(self):
        return self.kin_en * self.pot_en
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        
    def change_velocities(self, other):
        if self.x != other.x:
            self.vx += 1 if other.x > self.x else -1
        
        if self.y != other.y:
            self.vy += 1 if other.y > self.y else -1
        
        if self.z != other.z:
            self.vz += 1 if other.z > self.z else -1
            
    def __repr__(self):
        return f'pos = <{self.x}, {self.y}, {self.z}> ' \
               f'vel = <{self.vx}, {self.vy}, {self.vz}> ' \
               f'total = {self.total_en}\n'


def get_axes_velocities(moons):
    tmp = [''] * 3
    for moon in moons:
        tmp[0] += f'{moon.vx}'
        tmp[1] += f'{moon.vy}'
        tmp[2] += f'{moon.vz}'
    
    return tmp


def lcm(a, b):
    return (a * b) // gcd(a, b)


def part_both(data):
    moons = []
    for line in data:
        x, y, z = line.replace('<', '').replace('>', '').split(',')
        moons.append(Moon(int(x.split('=')[-1]), int(y.split('=')[-1]), int(z.split('=')[-1])))
    counter = 0
    
    cycled = [0, 0, 0]
    periods = [0]*3
    states = get_axes_velocities(moons)
    while True:
        for moon in moons:
            for other in moons:
                moon.change_velocities(other)
    
        for moon in moons:
            moon.move()
    
        counter += 1
        for i, state in enumerate(states):
            if get_axes_velocities(moons)[i] == states[i] and cycled[i] != 1:
                periods[i] = counter
                cycled[i] = 1
        
        # if counter == 1000:
        #     print(sum([i.total_en for i in moons]))
        #     break
        
        if sum(cycled) == 3:
            break
    
    return lcm(lcm(periods[0], periods[1]), periods[2]) * 2
    
    
with open('d12_input.txt') as fin:
    inp = fin.read().splitlines()

print(part_both(inp))
