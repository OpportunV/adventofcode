import numba


def part_one(signal: list, phases):
    n = len(signal)
    
    for j in range(phases):
        ans = [-1 for _ in range(n)]
        sums = [sum(signal[:i]) for i in range(n + 1)]
        for i in range(n):
            cur_digit = 0
            for one_start in range(i, n, 4 * (i + 1)):
                cur_digit += sums[min(one_start + i + 1, n)] - sums[one_start]
            for neg_one_start in range(3 * i + 2, n, 4 * (i + 1)):
                cur_digit -= sums[min(neg_one_start + i + 1, n)] - sums[neg_one_start]
            
            ans[i] = abs(cur_digit) % 10
        signal = ans[:]
        
    return signal


@numba.jit
def part_two(signal, phases):
    n = len(signal)
    
    for j in range(phases):
        for i in range(n - 2, -1, -1):
            signal[i] += signal[i + 1]
            signal[i] %= 10
    return signal


def main():
    with open('d16_input.txt') as fin:
        data = fin.readline()
        offset = int(data[:7])
        signal = [int(i) for i in data]
    
    a = signal[:]
    b = signal[:] * 10000
    b = b[offset:]
    
    print(offset, len(b), len(b) // 2)

    a = part_one(a, 100)
    b = part_two(b, 100)

    print(*a[:8], sep='')
    print(*b[:8], sep='')


if __name__ == '__main__':
    main()
