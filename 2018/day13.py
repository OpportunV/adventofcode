from collections import defaultdict


DIRECTIONS = {
    "<": -1,
    "v": +1j,
    ">": +1,
    "^": -1j,
}

PARTS = {
    "<": "-",
    "v": "|",
    ">": "-",
    "^": "|",
}


def part_one(inp):
    tracks, carts = setup(inp)
    while True:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            cart.position += cart.direction
            if any(c2.position == cart.position for c2i, c2 in enumerate(carts) if c2i != ci):
                return f"{cart.position.real:.0f},{cart.position.imag:.0f}"
            
            part = tracks[cart.position]
            turn(cart, part)


def part_two(inp):
    tracks, carts = setup(inp)
    while len(carts) > 1:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            if cart.dead:
                continue
            cart.position += cart.direction
            for ci2, cart2 in enumerate(carts):
                if ci != ci2 and cart.position == cart2.position and not cart2.dead:
                    cart.dead = True
                    cart2.dead = True
                    break
            if cart.dead:
                continue
            part = tracks[cart.position]
            turn(cart, part)
        carts = [c for c in carts if not c.dead]
    cart = carts[0]
    return f"{cart.position.real:.0f},{cart.position.imag:.0f}"


class Cart:
    def __init__(self, pos, di):
        self.position = pos
        self.direction = di
        self.turn = 0
        self.dead = False


def setup(inp):
    tracks = defaultdict(lambda: "")
    carts = []
    for y, line in enumerate(inp):
        for x, char in enumerate(line):
            if char in "<v>^":
                direction = DIRECTIONS[char]
                carts.append(Cart(x + y * 1j, direction))
                part = PARTS[char]
            else:
                part = char
            if part in "\\/+":
                tracks[(x + y * 1j)] = part
    return tracks, carts


def turn(cart, part):
    if not part:
        return
    if part == "\\":
        if cart.direction.real == 0:
            cart.direction *= -1j
        else:
            cart.direction *= +1j
    if part == "/":
        if cart.direction.real == 0:
            cart.direction *= +1j
        else:
            cart.direction *= -1j
    if part == "+":
        cart.direction *= -1j * 1j ** cart.turn
        cart.turn = (cart.turn + 1) % 3


def main():
    with open(r'input\day13.txt') as fin:
        inp = fin.read().splitlines()
        
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
