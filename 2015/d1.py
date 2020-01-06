def part_one(inp):
    ans = 0
    for i, char in enumerate(inp):
        if char == '(':
            ans += 1
        else:
            ans -= 1
    
    print(ans)


def part_two(inp):
    ans = 0
    for i, char in enumerate(inp):
        if char == '(':
            ans += 1
        else:
            ans -= 1
        if ans == -1:
            print(i + 1)
            break


def main():
    with open('d1_input.txt') as fin:
        inp = fin.readline()
    
    part_one(inp)
    part_two(inp)


if __name__ == '__main__':
    main()

