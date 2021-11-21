def part_one(inp):
    return read_valued_node(0, inp)[0]


def part_two(inp):
    return read_valued_node(0, inp, True)[0]


def read_valued_node(cur, data, valued=False):
    nodes = []
    nodes_amount = data[cur]
    cur += 1
    metadata_amount = data[cur]
    cur += 1
    for _ in range(nodes_amount):
        md, node, cur = read_valued_node(cur, data, valued)
        nodes.append(md)
    my_data = data[cur: cur + metadata_amount]
    value = 0
    cur += metadata_amount
    if not valued:
        return sum(my_data) + sum(nodes), nodes, cur
    
    if nodes_amount == 0:
        value = sum(my_data)
    else:
        for item in my_data:
            try:
                value += nodes[item - 1]
            except IndexError:
                pass
        
    return value, nodes, cur


def main():
    with open(r'input\day8.txt') as fin:
        inp = fin.read()
        
    inp = list(map(int, inp.split()))
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
