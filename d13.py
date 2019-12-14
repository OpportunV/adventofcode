from intcode_computer import IntcodeComputer
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class Arcade:
    def __init__(self, intcode):
        self.tiles = tiles = {0: '\u25AF',  # empty
                              1: '\u23F8',  # wall
                              2: '\u25AE',  # block
                              3: '\u2501',  # paddle
                              4: '\u23FA'}  # ball
        self.field = [[tiles[0] for _ in range(36)] for _ in range(21)]
        self.comp = IntcodeComputer(0, intcode=intcode)
        self.ball_x = 0
        self.paddle_x = 0
        self.score = 0
        self.fig, self.ax = plt.subplots()
        self.get_field()
        self.img = plt.imshow(self.draw_field())
        self.animation = FuncAnimation(self.fig, self.update)
        plt.show()
        
    def update(self, frame):
        self.update_field()
        data = self.draw_field()
        self.img.set_data(data)
        return self.img
    
    def get_field(self):
        x = self.comp.first_val
        y = next(self.comp.cor)
        _id = next(self.comp.cor)
        self.field[y][x] = self.tiles[_id]
        for i in range(752):
            x = next(self.comp.cor)
            y = next(self.comp.cor)
            _id = next(self.comp.cor)
            if _id == 4:
                self.ball_x = x
            if _id == 3:
                self.paddle_x = x
            self.field[y][x] = self.tiles[_id]

    def update_field(self):
        try:
            x = self.send_input()
            y = self.send_input()
            if x == -1 and y == 0:
                self.score = self.send_input()
                print(self.score)
            else:
                _id = self.send_input()
                if _id == 4:
                    self.ball_x = x
                if _id == 3:
                    self.paddle_x = x
                self.field[y][x] = self.tiles[_id]
        except StopIteration:
            return
    
    def send_input(self):
        if self.ball_x < self.paddle_x:
            move = -1
        elif self.ball_x > self.paddle_x:
            move = 1
        else:
            move = 0
        a = self.comp.cor.send(move)
        if a is None:
            a = self.send_input()
        return a
    
    def draw_field(self):
        board = '\n'.join([''.join(line) for line in self.field])

        tmp = board.replace(self.tiles[0], '0') \
            .replace(self.tiles[1], '1') \
            .replace(self.tiles[2], '2') \
            .replace(self.tiles[3], '3') \
            .replace(self.tiles[4], '4')
        return [[int(j) for j in i] for i in tmp.split()]
        


def write_tile(x, y, _id, last_y=[0]):
    tiles = {0: '\u25AF',  # empty
             1: '\u23F8',  # wall
             2: '\u25AE',  # block
             3: '\u2501',  # paddle
             4: '\u23FA'}  # ball
    
    if last_y[0] != y:
        print()
        last_y[0] = y
    print(tiles[_id], sep='', end='')


def part_one(intcode):
    comp = IntcodeComputer(0, intcode=intcode)
    x = comp.first_val
    y = next(comp.cor)
    _id = next(comp.cor)
    write_tile(x, y, _id)
    
    while True:
        try:
            x = next(comp.cor)
            y = next(comp.cor)
            _id = next(comp.cor)
            # tiles.append((x, y, _id))
            write_tile(x, y, _id)
        except StopIteration:
            break


def par_two(intcode):
    Arcade(intcode)


with open('d13_input.txt') as fin:
    intc = [int(i) for i in fin.readline().split(',')]

# part_one(intc)
par_two(intc)
