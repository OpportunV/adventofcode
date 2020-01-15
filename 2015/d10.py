def part_one(inp):
    for _ in range(40):
        inp = step(inp)
    
    return len(inp)
    

def part_two(inp):
    for _ in range(50):
        inp = step(inp)
    
    return len(inp)


def step(inp):
    ans = []
    count = 1
    for i in range(len(inp) - 1):
        if inp[i] == inp[i + 1]:
            count += 1
        else:
            ans.extend([str(count), inp[i]])
            count = 1

    ans.extend([str(count), inp[-1]])
    return ''.join(ans)


def main():
    inp = '3113322113'
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
