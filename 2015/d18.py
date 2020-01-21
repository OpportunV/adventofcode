def part_one(inp):
    lights = [[i == '#' for i in line] for line in inp]
    for _ in range(100):
        tmp = [[0] * len(lights[0]) for _ in range(len(lights))]
        for i in range(len(lights[0])):
            for j in range(len(lights)):
                tmp[i][j] = (lights[i][j] and 2 <= sum(adjacent((i, j), lights)) <= 3) \
                    or (not lights[i][j] and sum(adjacent((i, j), lights)) == 3)
        lights = tmp
    return sum(sum(i) for i in lights)


def part_two(inp):
    lights = [[i == '#' for i in line] for line in inp]
    lights[0][0] = lights[-1][0] = lights[0][-1] = lights[-1][-1] = True
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots()
    img = plt.imshow(lights)
    plt.axis('off')
    plt.ion()
    plt.show()
    for _ in range(100):
        tmp = [[0] * len(lights[0]) for _ in range(len(lights))]
        for i in range(len(lights[0])):
            for j in range(len(lights)):
                tmp[i][j] = (lights[i][j] and 2 <= sum(adjacent((i, j), lights)) <= 3) \
                            or (not lights[i][j] and sum(adjacent((i, j), lights)) == 3)
        lights = tmp
        lights[0][0] = lights[-1][0] = lights[0][-1] = lights[-1][-1] = True
        img.set_data(lights)
        plt.pause(.001)
    return sum(sum(i) for i in lights)


def adjacent(pos, grid):
    x, y = pos
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            yield grid[x + i][y + j] if 0 <= x + i < len(grid[0]) and 0 <= y + j < len(grid) else False


def main():
    with open('d18_input.txt') as fin:
        inp = fin.read().splitlines()
    
    # print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
