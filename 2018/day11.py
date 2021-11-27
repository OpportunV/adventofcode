import math


def part_one(inp):
    ans = -math.inf
    pos = None
    for i in range(298):
        for j in range(298):
            sub_sum = get_square_value(i, j, inp)
            if sub_sum > ans:
                ans = sub_sum
                pos = i, j
                
    return f"{pos[0]},{pos[1]}"


def part_two(inp):
    ans = -math.inf
    pos = None
    for size in range(1, 300):
        sub_ans = -math.inf
        sub_pos = None
        for i in range(301 - size):
            for j in range(301 - size):
                sub_sum = get_square_value(i, j, inp, size)
                if sub_sum > sub_ans:
                    sub_ans = sub_sum
                    sub_pos = i, j, size
                    
        if sub_ans > ans:
            ans = sub_ans
            pos = sub_pos
            
        if sub_ans < 0:
            return f"{pos[0]},{pos[1]},{pos[2]}"


def get_square_value(x, y, inp, size=3, cache={}):
    key = x, y, size
    if key in cache:
        return cache[key]
    
    if size == 1:
        return get_cell_value(x, y, inp)
    
    ans = get_square_value(x, y, inp, size - 1)
    for k in range(2 * size - 1):
        if k < size:
            x_c = x + k
            y_c = y + size - 1
        else:
            x_c = x + size - 1
            y_c = y + (k - size)
        
        ans += get_cell_value(x_c, y_c, inp)
        
    cache[key] = ans
    return ans


def get_cell_value(x, y, inp, cache={}):
    key = x, y, inp
    if key in cache:
        return cache[key]
    
    rack_id = x + 10
    power_level = rack_id * y
    power_level += inp
    power_level *= rack_id
    power_level = power_level % 1000 // 100
    power_level -= 5
    cache[key] = power_level
    return power_level


def main():
    with open(r'input\day11.txt') as fin:
        inp = int(fin.read())
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
