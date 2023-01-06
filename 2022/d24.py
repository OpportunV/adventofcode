from copy import deepcopy
from itertools import cycle


class Field:
    __slots__ = ('raw_map', 'all_maps', 'start', 'end', 'n_cols', 'n_raws', 'blizzards', 'step')
    
    moves = {
        '>': 1,
        'v': 1j,
        '<': -1,
        '^': -1j,
        '0': 0
    }
    
    surroundings = [-1 - 1j, -1j, 1 - 1j, -1 + 1j, 1j, 1 + 1j, 1, -1]
    
    def __init__(self, inp):
        self.raw_map = {}
        self.blizzards = set()
        self.step = 0
        self.n_cols = len(inp[0])
        self.n_raws = len(inp)
        self._from_inp(inp)
        self.start = complex(inp[0].index('.'), 0)
        self.end = complex(inp[-1].index('.'), self.n_raws - 1)
        self.all_maps = self.get_all_maps()
    
    def reach_goal(self, start, end):
        can_visit = {start: 0}
        while end not in can_visit:
            next_to_visit = {}
            self.step += 1
            cur_map = next(self.all_maps)
            for k, v in can_visit.items():
                for direction in self.moves.values():
                    pos = k + direction
                    if (self.n_cols > pos.real >= 0 and self.n_raws > pos.imag >= 0
                            and cur_map[pos] == "."):
                        next_to_visit[pos] = v + 1
            can_visit = next_to_visit
    
    def get_all_maps(self):
        all_maps = []
        new_map = self.get_next_map()
        while new_map not in all_maps:
            all_maps.append(new_map)
            new_map = self.get_next_map()
        
        return cycle(all_maps)
    
    def get_next_map(self):
        new_map = deepcopy(self.raw_map)
        new_blizzards = set()
        for pos, direction in self.blizzards:
            new_pos = pos + self.moves[direction]
            if new_pos.real < 1:
                new_pos = complex(self.n_cols - 2, new_pos.imag)
            if new_pos.real >= self.n_cols - 1:
                new_pos = complex(1, new_pos.imag)
            if new_pos.imag < 1:
                new_pos = complex(new_pos.real, self.n_raws - 2)
            if new_pos.imag >= self.n_raws - 1:
                new_pos = complex(new_pos.real, 1)
            
            new_map[new_pos] = direction
            new_blizzards.add((new_pos, direction))
        
        self.blizzards = new_blizzards
        return new_map
    
    def _from_inp(self, inp):
        for i in range(self.n_raws):
            for j in range(self.n_cols):
                cur = inp[i][j]
                self.raw_map[complex(j, i)] = cur if cur == '#' else '.'
                if cur in self.moves.keys():
                    self.blizzards.add((complex(j, i), cur))


def part_one(inp):
    field = Field(inp)
    field.reach_goal(field.start, field.end)
    return field.step


def part_two(inp):
    field = Field(inp)
    field.reach_goal(field.start, field.end)
    field.reach_goal(field.end, field.start)
    field.reach_goal(field.start, field.end)
    return field.step


def main():
    with open(r'd24_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
