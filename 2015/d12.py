import json


def part_one(inp):
    def values_iterator(obj):
        if isinstance(obj, int):
            yield obj
        if isinstance(obj, dict):
            for key, value in obj.items():
                yield from values_iterator(value)
        if isinstance(obj, list):
            for value in obj:
                yield from values_iterator(value)
    return sum(values_iterator(inp))


def part_two(inp):
    def values_iterator(obj):
        if isinstance(obj, int):
            yield obj
        if isinstance(obj, dict) and ('red' not in obj.values()):
            for key, value in obj.items():
                yield from values_iterator(value)
        if isinstance(obj, list):
            for value in obj:
                yield from values_iterator(value)
    return sum(values_iterator(inp))


def main():
    with open('d12_input.txt') as fin:
        inp = json.load(fin)
        
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
