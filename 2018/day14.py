def part_one(inp):
    recipes = [3, 7]
    first = 0
    second = 1
    while len(recipes) < inp + 10:
        first, second = simulate(first, recipes, second)
        
    return ''.join([str(item) for item in recipes[inp:inp + 10]])


def part_two(inp):
    recipes = [3, 7]
    target = list(map(int, str(inp)))
    first = 0
    second = 1
    while target != recipes[-len(target):] and target != recipes[-len(target) - 1: -1]:
        first, second = simulate(first, recipes, second)
        
    return len(recipes) - len(target) if target == recipes[-len(target):] else len(recipes) - len(target) - 1


def simulate(first, recipes, second):
    new_recipes = recipes[first] + recipes[second]
    if new_recipes >= 10:
        recipes.extend(divmod(new_recipes, 10))
    else:
        recipes.append(new_recipes)
        
    first = (first + 1 + recipes[first]) % len(recipes)
    second = (second + 1 + recipes[second]) % len(recipes)
    return first, second


def main():
    with open(r'input\day14.txt') as fin:
        inp = int(fin.read())
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
