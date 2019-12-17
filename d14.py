from collections import defaultdict


def get_ore_amount_for(amount, name, target, react_dict, counter):
    counter[name] = 0
    required = defaultdict(lambda: 0)
    required[name] = amount
    while True:
        for item in counter:
            if counter[item] == 0:
                cur_amount = required[item]
                if item == target:
                    return cur_amount
                item_req_am = react_dict[item][0]
                item_needs = react_dict[item][1]
                int_mul = (cur_amount + item_req_am - 1) // item_req_am
                for needed in item_needs:
                    required[needed] += item_needs[needed] * int_mul
                    counter[needed] -= 1
                counter.pop(item)
                break


def part_one(reactions):
    react_dict = defaultdict(list)
    counter = defaultdict(lambda: 0)
    for reaction in reactions:
        requires, out = reaction.split('=>')
        requires = requires.split(',')
        out_number, out_name = out.split()
        react_dict[out_name].append(int(out_number))
        react_dict[out_name].append({})
        for req in requires:
            req_number, req_name = req.split()
            counter[req_name] += 1
            react_dict[out_name][1][req_name] = int(req_number)
    
    print(get_ore_amount_for(1, 'FUEL', 'ORE', react_dict, counter))


def part_two(reactions):
    react_dict = defaultdict(list)
    counter = defaultdict(lambda: 0)
    for reaction in reactions:
        requires, out = reaction.split('=>')
        requires = requires.split(',')
        out_number, out_name = out.split()
        react_dict[out_name].append(int(out_number))
        react_dict[out_name].append({})
        for req in requires:
            req_number, req_name = req.split()
            counter[req_name] += 1
            react_dict[out_name][1][req_name] = int(req_number)
    
    fuel = [0, 10 ** 12]
    ore = 10 ** 12
    while fuel[0] < fuel[1]:
        mid = (fuel[0] + fuel[1] + 1) // 2
        if get_ore_amount_for(mid, 'FUEL', 'ORE', react_dict.copy(), counter.copy()) <= ore:
            fuel[0] = mid
        else:
            fuel[1] = mid - 1
    
    print(fuel)


with open('d14_input.txt') as fin:
    inp = fin.read().splitlines()

# part_one(inp)
part_two(inp)
