from collections import deque


def part_one(inp):
    amount = int(inp[0])

    initial = list(range(1, amount + 1))
    while len(initial) != 1:
        new = []
        for i, item in enumerate(initial):
            if i % 2 == 0:
                new.append(item)

        if len(initial) % 2 == 1:
            new.pop(0)

        initial = new

    return initial[0]


def part_two(inp):
    amount = int(inp[0])
    left = deque(range(1, amount // 2 + 1))
    right = deque(range(amount // 2 + 1, amount + 1))

    while True:
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()

        if not left or not right:
            break

        left.append(right.popleft())
        right.append(left.popleft())

    return left[0] if left else right[0]


def main():
    with open('input/day19.txt') as fin:
        inp = fin.read().splitlines()

    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
