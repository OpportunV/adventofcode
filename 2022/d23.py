from collections import deque


class Field:
    __slots__ = ('elves', 'forbidden_moves', 'round', 'moves_priority')
    
    spots = {
        -1j: [-1 - 1j, -1j, 1 - 1j],
        1j: [-1 + 1j, 1j, 1 + 1j],
        1: [1 - 1j, 1, 1 + 1j],
        -1: [-1 - 1j, -1, -1 + 1j]
    }
    
    surroundings = [-1 - 1j, -1j, 1 - 1j, -1 + 1j, 1j, 1 + 1j, 1, -1]
    
    def __init__(self, inp):
        self.moves_priority = deque([-1j, 1j, -1, 1])
        self.elves = {}
        self.forbidden_moves = set()
        self._from_inp(inp)
        self.round = 0
    
    @property
    def empty_ground(self):
        keys = self.elves.keys()
        min_x = int(min(keys, key=lambda key: key.real).real)
        max_x = int(max(keys, key=lambda key: key.real).real)
        min_y = int(min(keys, key=lambda key: key.imag).imag)
        max_y = int(max(keys, key=lambda key: key.imag).imag)
        total = 0
        for j in range(min_y, max_y + 1):
            for i in range(min_x, max_x + 1):
                if complex(i, j) not in keys:
                    total += 1
        
        return total
    
    def can_move(self, direction, pos):
        return all((pos + sub_dir) not in self.elves.keys() for sub_dir in self.spots[direction])
    
    def other_elf_close(self, pos):
        return any((pos + sub_dir) in self.elves.keys() for sub_dir in self.surroundings)
    
    def plan(self):
        for elf in self.elves.keys():
            if not self.other_elf_close(elf):
                continue
            
            for direction in self.moves_priority:
                if self.can_move(direction, elf):
                    target = elf + direction
                    if target in self.elves.values():
                        self.forbidden_moves.add(target)
                    
                    self.elves[elf] = target
                    break
        
        return not any(self.elves.values())
    
    def move(self):
        new_elves = {}
        for elf, target in self.elves.items():
            if target is not None and target not in self.forbidden_moves:
                new_elves[target] = None
            else:
                new_elves[elf] = None
        
        self.elves = new_elves
        self.moves_priority.rotate(-1)
        self.forbidden_moves.clear()
        self.round += 1
    
    def _from_inp(self, inp):
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                if inp[i][j] == '#':
                    self.elves[complex(j, i)] = None


def part_one(inp):
    field = Field(inp)
    for _ in range(10):
        field.plan()
        field.move()
    
    return field.empty_ground


def part_two(inp):
    field = Field(inp)
    done = False
    while not done:
        done = field.plan()
        field.move()
    
    return field.round


def main():
    with open(r'd23_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
