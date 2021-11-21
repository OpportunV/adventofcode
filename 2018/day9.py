import re
from collections import defaultdict, deque


def part_one(inp):
    players = play_game(*inp)
    return max(players.values())


def part_two(inp):
    players = play_game(inp[0], inp[1] * 100)
    return max(players.values())


def play_game(n_players, n_marbles):
    players = defaultdict(int)
    marbles = deque([0])
    
    for marble in range(1, n_marbles + 1):
        if marble % 23 == 0:
            marbles.rotate(7)
            players[marble % n_players] += marble + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)
    
    return players


class Marble:
    def __init__(self, value, nxt=None, prev=None):
        if nxt is None:
            self.nxt = self
        else:
            self.nxt = nxt

        if prev is None:
            self.prev = self
        else:
            self.prev = prev

        self.value = value

    def __repr__(self):
        return f"<{self.prev.value} {self.value} {self.nxt.value}>"


# super long running in python but on c#/java runs faster than deque solution on python =\
def play_game_linked(n_players, n_marbles):
    players = defaultdict(int)
    cur_marble = Marble(0)
    cur_player = 1
    new_val = 1

    while new_val != n_marbles:
        if new_val % 23 == 0:
            players[cur_player] += new_val
            marble_to_remove = cur_marble
            for _ in range(7):
                marble_to_remove = marble_to_remove.prev
            players[cur_player] += marble_to_remove.value
            prev = marble_to_remove.prev
            nxt = marble_to_remove.nxt
            prev.nxt = nxt
            nxt.prev = prev
            cur_marble = nxt
        else:
            new_marble = Marble(new_val, prev=cur_marble.nxt, nxt=cur_marble.nxt.nxt)
            cur_marble.nxt.nxt.prev = new_marble
            cur_marble.nxt.nxt = new_marble
            cur_marble = new_marble

        cur_player = (cur_player + 1) % n_players
        new_val += 1
    return players


def main():
    with open(r'input\day9.txt') as fin:
        inp = fin.read()
    
    inp = list(map(int, re.findall(r'\d+', inp)))
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
