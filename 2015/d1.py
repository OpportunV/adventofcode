with open('d1_input.txt') as fin:
    inp = fin.readline()
    
ans = 0
for i, char in enumerate(inp):
    if char == '(':
        ans += 1
    else:
        ans -= 1
    if ans == -1:
        print(i + 1)
        break

print(ans)
