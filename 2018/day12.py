INIT_LEN = 0


def part_one(state, morphs):
    for _ in range(20):
        state = f'...{state}...'
        state = simulate(state, morphs)
        
    return calc_plants(state)


def part_two(state, morphs):
    n = 50000000000
    for gen in range(n):
        state = f'...{state}...'
        new_state = simulate(state, morphs)
        if new_state in state:
            diff = calc_plants(new_state) - calc_plants(state)
            break
        
        state = new_state

    ans = (n - gen) * diff + calc_plants(state)
    return ans


def simulate(state, morphs):
    new_state = ""
    for i in range(2, len(state) - 2):
        cur = state[i - 2:i + 3]
        new_state += morphs.get(cur, state[i])
    
    return new_state


def calc_plants(state):
    ans = 0
    dif = (len(state) - INIT_LEN) // 2
    for i, val in enumerate(state):
        if val == '#':
            ans += i - dif
            
    return ans


def main():
    with open(r'input\day12.txt') as fin:
        inp = fin.read()
    
    splt = inp.split('\n\n')
    init_state = splt[0].split(': ')[1].strip()
    global INIT_LEN
    INIT_LEN = len(init_state)
    morphs = {item.split(' => ')[0]: item.split(' => ')[1] for item in splt[1].split('\n')}
    
    print(part_one(init_state, morphs))
    print(part_two(init_state, morphs))
    
    
if __name__ == '__main__':
    main()
