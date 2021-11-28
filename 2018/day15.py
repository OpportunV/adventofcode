from typing import NamedTuple
from dataclasses import dataclass
import itertools
import collections


class Pt(NamedTuple('Pt', [('x', int), ('y', int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def adjacent(self):
        return [self + d for d in [Pt(0, 1), Pt(1, 0), Pt(0, -1), Pt(-1, 0)]]


@dataclass
class Unit:
    is_elf: bool
    position: Pt
    hp: int = 200
    alive: bool = hp > 0
    attack: int = 3


class Grid(dict):
    def __init__(self, lines, attack=3):
        super().__init__()

        self.units = []

        for i, line in enumerate(lines):
            for j, el in enumerate(line):
                self[Pt(i, j)] = el == '#'

                if el in 'EG':
                    self.units.append(Unit(
                        is_elf=True if el == 'E' else False,
                        position=Pt(i, j),
                        attack=attack if el == 'E' else 3,
                    ))

    def play(self, elf_death=False):
        rounds = 0
        while True:
            if self.round(elf_death=elf_death):
                break
            rounds += 1
        return rounds * sum(unit.hp for unit in self.units if unit.alive)

    def round(self, elf_death=False):
        for unit in sorted(self.units, key=lambda item: item.position):
            if unit.alive:
                if self.move(unit, elf_death=elf_death):
                    return True

    def move(self, unit, elf_death=False):
        targets = [target for target in self.units if unit.is_elf != target.is_elf and target.alive]
        occupied = set(u2.position for u2 in self.units if u2.alive and unit != u2)

        if not targets:
            return True

        in_range = {pt for target in targets for pt in target.position.adjacent if not self[pt] and pt not in occupied}

        if unit.position not in in_range:
            move = self.find_move(unit.position, in_range)

            if move:
                unit.position = move

        opponents = [target for target in targets if target.position in unit.position.adjacent]

        if opponents:
            target = min(opponents, key=lambda item: (item.hp, item.position))

            target.hp -= unit.attack

            if target.hp <= 0:
                target.alive = False
                if elf_death and target.is_elf:
                    raise StopIteration

    def find_move(self, position, targets):
        visiting = collections.deque([(position, 0)])
        meta = {position: (0, None)}
        seen = set()
        occupied = {unit.position for unit in self.units if unit.alive}

        while visiting:
            pos, dist = visiting.popleft()
            for nb in pos.adjacent:
                if self[nb] or nb in occupied:
                    continue
                if nb not in meta or meta[nb] > (dist + 1, pos):
                    meta[nb] = (dist + 1, pos)
                if nb in seen:
                    continue
                if not any(nb == visit[0] for visit in visiting):
                    visiting.append((nb, dist + 1))
            seen.add(pos)

        try:
            min_dist, closest = min((dist, pos) for pos, (dist, parent) in meta.items() if pos in targets)
        except ValueError:
            return

        while meta[closest][0] > 1:
            closest = meta[closest][1]

        return closest


def part_one(inp):
    grid = Grid(inp)
    return grid.play()


def part_two(inp):
    for attack in itertools.count(4):
        try:
            outcome = Grid(inp, attack).play(elf_death=True)
        except StopIteration:
            continue
        else:
            return outcome
            

def main():
    with open(r'input\day15.txt') as fin:
        inp = fin.read().splitlines()
        
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
