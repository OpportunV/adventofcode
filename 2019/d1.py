def part_one():
    total = 0
    with open('d1_input.txt') as fin:
        for line in fin:
            module = int(line)
            fuel = module // 3 - 2
            extra = part_two(fuel)
            total += fuel
            total += extra
    
    return total


def part_two(fuel):
    total = 0
    extra_fuel = fuel // 3 - 2
    while extra_fuel > 0:
        total += extra_fuel
        extra_fuel = extra_fuel // 3 - 2
    
    return total


total_fuel = part_one()

print(total_fuel)
