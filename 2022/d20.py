def prepare_input(inp):
    nums_to_mix = {}
    zero = None
    for i, num in enumerate(inp):
        nums_to_mix[f"{num}_{i}"] = num
        if num == 0:
            zero = f"{num}_{i}"
    
    return nums_to_mix, zero


def mix_file(data, nums_to_mix):
    length = len(data) - 1
    for num in nums_to_mix.keys():
        pos = data.index(num)
        val = nums_to_mix[num]
        new_pos = (pos + val + length) % length
        data.remove(num)
        data.insert(new_pos, num)


def part_one(inp):
    nums_to_mix, zero = prepare_input(inp)
    
    data = list(nums_to_mix.keys())
    mix_file(data, nums_to_mix)
    
    pos = data.index(zero)
    return sum([nums_to_mix[data[(pos + i) % len(data)]] for i in [1000, 2000, 3000]])


def part_two(inp):
    decryption_key = 811589153
    inp = [i * decryption_key for i in inp]
    
    nums_to_mix, zero = prepare_input(inp)
    data = list(nums_to_mix.keys())
    for i in range(10):
        mix_file(data, nums_to_mix)
    
    pos = data.index(zero)
    return sum([nums_to_mix[data[(pos + i) % len(data)]] for i in [1000, 2000, 3000]])


def main():
    with open(r'd20_input.txt') as fin:
        inp = list(map(int, fin.read().splitlines()))
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
