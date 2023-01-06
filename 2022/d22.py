import re
from collections import defaultdict

DIRECTIONS = {
    0: 1,
    1: 1j,
    2: -1,
    3: -1j,
}


class Field(defaultdict):
    __slots__ = ('n_cols', 'n_raws', 'face_size')
    
    def __init__(self, n_cols, n_raws, raw_field, default=' '):
        self.n_cols = n_cols
        self.n_raws = n_raws
        self.face_size = n_cols // 3
        self._from_raw(raw_field)
        super().__init__(lambda: default)
    
    @property
    def start_pos(self):
        for i in range(self.n_raws):
            for j in range(self.n_cols):
                if super().__getitem__(complex(j, i)) == '.':
                    return complex(j, i)
    
    def _from_raw(self, raw_field):
        for i in range(self.n_raws):
            for j in range(self.n_cols):
                try:
                    super().__setitem__(complex(j, i), raw_field[i][j])
                except IndexError:
                    pass
    
    def display(self):
        for i in range(self.n_raws):
            for j in range(self.n_cols):
                print(super().__getitem__(complex(j, i)), end='')
            
            print()
    
    def normalize_pos_on_plane(self, pos: complex):
        return complex((pos.real + self.n_cols) % self.n_cols, (pos.imag + self.n_raws) % self.n_raws)
    
    def normalize_pos_on_cube(self, pos: complex, direction):
        """
        faces: \n
        o 1 2 \n
        o 3 o \n
        4 5 o \n
        6 o o
        
        :param pos: desired position on flat map
        :param direction: desired direction on flat map
        :return: desired position and direction on flat map using cube wrapping
        """
        # stepping left from face 1 must land on face 4
        if pos.real == self.face_size - 1 and pos.imag < self.face_size:
            assert direction == 2
            dy = pos.imag
            pos = complex(0, 3 * self.face_size - dy - 1)
            direction = 0
            return pos, direction
        # stepping left from face 4 must land on face 1
        elif pos.real == -1 and 2 * self.face_size <= pos.imag < 3 * self.face_size:
            assert direction == 2
            dy = 3 * self.face_size - pos.imag - 1
            pos = complex(self.face_size, dy)
            direction = 0
            return pos, direction
        # stepping up from face 1 must land on face 6
        elif pos.imag == -1 and pos.real < 2 * self.face_size:
            assert direction == 3
            dx = 2 * self.face_size - pos.real
            pos = complex(0, self.n_raws - dx)
            direction = 0
            return pos, direction
        # stepping left from face 6 must land on face 1
        elif pos.real == -1 and pos.imag >= 3 * self.face_size:
            assert direction == 2
            dy = self.n_raws - pos.imag
            pos = complex(2 * self.face_size - dy, 0)
            direction = 1
            return pos, direction
        # stepping up from face 2 must land on face 6
        elif pos.imag == -1 and pos.real >= 2 * self.face_size:
            assert direction == 3
            dx = pos.real - 2 * self.face_size
            pos = complex(dx, self.n_raws - 1)
            return pos, direction
        # stepping down from face 6 must land on face 2
        elif pos.imag == 4 * self.face_size:
            assert direction == 1
            dx = pos.real
            pos = complex(2 * self.face_size + dx, 0)
            return pos, direction
        # stepping right from face 2 must land on face 5
        elif pos.real == self.n_cols:
            assert direction == 0
            dy = pos.imag
            pos = complex(2 * self.face_size - 1, 3 * self.face_size - dy - 1)
            direction = 2
            return pos, direction
        # stepping right from face 5 must land on face 2
        elif pos.real == 2 * self.face_size and 2 * self.face_size <= pos.imag < 3 * self.face_size:
            assert direction == 0
            dy = 3 * self.face_size - pos.imag - 1
            pos = complex(self.n_cols - 1, dy)
            direction = 2
            return pos, direction
        # stepping down from face 2 must land on face 3
        elif pos.imag == self.face_size and pos.real >= 2 * self.face_size:
            assert direction == 1
            dx = self.n_cols - pos.real
            pos = complex(2 * self.face_size - 1, 2 * self.face_size - dx)
            direction = 2
            return pos, direction
        # stepping right from face 3 must land on face 2
        elif pos.real == 2 * self.face_size and self.face_size <= pos.imag < 2 * self.face_size:
            assert direction == 0
            dy = 2 * self.face_size - pos.imag
            pos = complex(self.n_cols - dy, self.face_size - 1)
            direction = 3
            return pos, direction
        # stepping left from face 3 must land on face 4
        elif pos.real == self.face_size - 1 and self.face_size <= pos.imag < 2 * self.face_size and direction == 2:
            dy = pos.imag - self.face_size
            pos = complex(dy, 2 * self.face_size)
            direction = 1
            return pos, direction
        # stepping up from face 4 must land on face 3
        elif pos.imag == 2 * self.face_size - 1 and pos.real < self.face_size and direction == 3:
            dx = pos.real
            pos = complex(self.face_size, self.face_size + dx)
            direction = 0
            return pos, direction
        # stepping down from face 5 must land on face 6
        elif pos.imag == 3 * self.face_size and pos.real >= self.face_size:
            assert direction == 1
            dx = 2 * self.face_size - pos.real
            pos = complex(self.face_size - 1, self.n_raws - dx)
            direction = 2
            return pos, direction
        # stepping right from face 6 must land on face 5
        elif pos.real == self.face_size and pos.imag >= 3 * self.face_size:
            assert direction == 0
            dy = self.n_raws - pos.imag
            pos = complex(2 * self.face_size - dy, 3 * self.face_size - 1)
            direction = 3
            return pos, direction
        
        return pos, direction


def get_field(inp):
    raw_field = inp[0].split('\n')
    n_cols = max(map(lambda item: len(item), raw_field))
    n_raws = len(raw_field)
    field = Field(n_cols, n_raws, raw_field)
    return field


def part_one(inp):
    field = get_field(inp)
    position = field.start_pos
    direction = 0
    for instruction in re.findall(r'\d+|[RL]', inp[1]):
        if instruction == 'R':
            direction = (direction + 1) % 4
        elif instruction == 'L':
            direction = (direction - 1) % 4
        else:
            for _ in range(int(instruction)):
                next_pos = field.normalize_pos_on_plane(position + DIRECTIONS[direction])
                while field[next_pos] == ' ':
                    next_pos = field.normalize_pos_on_plane(next_pos + DIRECTIONS[direction])
                
                if field[next_pos] == '.':
                    position = next_pos
                elif field[next_pos] == '#':
                    break
    
    position += (1 + 1j)
    return int(1000 * position.imag + 4 * position.real + direction)


def part_two(inp):
    field = get_field(inp)
    position = field.start_pos
    direction = 0
    for instruction in re.findall(r'\d+|[RL]', inp[1]):
        if instruction == 'R':
            direction = (direction + 1) % 4
        elif instruction == 'L':
            direction = (direction - 1) % 4
        else:
            for _ in range(int(instruction)):
                next_pos, next_dir = field.normalize_pos_on_cube(position + DIRECTIONS[direction], direction)
                if field[next_pos] == ' ':
                    next_pos, next_dir = field.normalize_pos_on_cube(next_pos + DIRECTIONS[direction], next_dir)
                
                if field[next_pos] == '.':
                    position, direction = next_pos, next_dir
                elif field[next_pos] == '#':
                    break
    
    position += (1 + 1j)
    return int(1000 * position.imag + 4 * position.real + direction)


def main():
    with open(r'd22_input.txt') as fin:
        inp = fin.read().split('\n\n')
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
