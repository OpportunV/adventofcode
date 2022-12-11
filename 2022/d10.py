class Cpu:
    def __init__(self, x=1, cycle=0):
        self.total = 0
        self.x = x
        self.cycle = cycle
        self.drawing = ''
    
    def step(self):
        self.cycle += 1
        self.draw()
        if (self.cycle - 20) % 40 == 0:
            self.total += self.cycle * self.x
    
    def draw(self):
        self.drawing += '#' if abs(self.cycle % 40 - 1 - self.x) <= 1 else '.'
        if self.cycle % 40 == 0:
            self.drawing += '\n'
    
    def add(self, value):
        self.x += value


def run(inp, cpus=[]):
    if cpus:
        return cpus[0]
    
    cpu = Cpu()
    cpus.append(cpu)
    for line in inp:
        if line == 'noop':
            cpu.step()
        if 'addx' in line:
            cpu.step()
            cpu.step()
            cpu.add(int(line.split()[1]))
    
    return cpu


def part_one(inp):
    cpu = run(inp)
    return cpu.total


def part_two(inp):
    cpu = run(inp)
    return cpu.drawing


def main():
    with open(r'd10_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
