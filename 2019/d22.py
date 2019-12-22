from collections import deque


def part_one(commands):
    n_cards = 10007
    cards = deque(list(range(n_cards)))
    for command in commands:
        if 'cut' in command:
            n_cut = int(command.split()[-1])
            cards.rotate(-n_cut)
        elif 'increment' in command:
            n_inc = int(command.split()[-1])
            tmp = [0] * n_cards
            for i, card in enumerate(cards):
                tmp[(i * n_inc) % n_cards] = card
            cards = deque(tmp)
        elif 'new' in command:
            cards.reverse()
    
    return cards.index(2019)


def part_two(commands):
    n_repeats = 101741582076661
    n_cards = 119315717514047
    pos = 2020
    start, dif = 0, 1
    
    for command in commands:
        if 'cut' in command:
            n_cut = int(command.split()[-1])
            start += dif * n_cut
        elif 'increment' in command:
            n_inc = int(command.split()[-1])
            dif = pow(n_inc, n_cards - 2, n_cards) * dif
        elif 'new' in command:
            dif = -dif
            start += dif
    
    return (start % n_cards * (1 - pow(dif, n_repeats, n_cards)) * pow(1 - dif, n_cards - 2, n_cards)
            + pow(dif, n_repeats, n_cards) * pos) % n_cards


def main():
    with open('d22_input.txt') as fin:
        commands = fin.read().splitlines()
    
    print(part_one(commands))
    print(part_two(commands))


if __name__ == '__main__':
    main()
