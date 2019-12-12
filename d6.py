def part_one(orbit_map):
    dict_map = {}

    for line in orbit_map:
        center, body = line.split(')')
        dict_map[body] = center
    
    total = 0
    for body in dict_map:
        while dict_map.get(body):
            total += 1
            body = dict_map[body]
    
    return total


def part_two(orbit_map):
    dict_map = {}
    
    for line in orbit_map:
        center, body = line.split(')')
        dict_map[body] = center
        
    my_body = dict_map.get('YOU')
    my_path = [my_body]
    while dict_map.get(my_body):
        my_body = dict_map[my_body]
        my_path.append(my_body)
    
    target_body = dict_map.get('SAN')
    target_path = [target_body]
    while dict_map.get(target_body) not in my_path:
        target_body = dict_map[target_body]
        target_path.append(target_body)
    else:
        target_body = dict_map[target_body]
        target_path.append(target_body)
        total = len(target_path) + len(my_path[:my_path.index(target_body)]) - 1
    
    return total
    

with open('d6_input.txt') as fin:
    data = fin.read().splitlines()

print(part_two(data))
