DIVIDER = '__'
TOTAL_DISK = 70_000_000
REQUIRED = 30_000_000


def part_one(inp):
    fs, dir_paths = build_tree(inp)
    total = 0
    for dir_path in dir_paths:
        path = dir_path.split(DIVIDER)
        size = get_size(fs, path)
        if size < 100_000:
            total += size
    
    return total


def part_two(inp):
    fs, dir_paths = build_tree(inp)
    space_taken = get_size(fs, ['/'])
    delete_candidate_size = TOTAL_DISK
    for dir_path in dir_paths:
        path = dir_path.split(DIVIDER)
        size = get_size(fs, path)
        if TOTAL_DISK - space_taken + size >= REQUIRED:
            delete_candidate_size = min(delete_candidate_size, size)
    
    return delete_candidate_size


def build_tree(inp, fs={}, dir_paths=set()):
    if fs:
        return fs, dir_paths
    
    dir_paths.add('/')
    i = 0
    cur_path = []
    while i < len(inp):
        line = inp[i]
        if 'cd' in line:
            arg = line.split()[-1]
            if arg == '/':
                cur_path = ['/']
            elif arg == '..':
                cur_path.pop()
            else:
                cur_path.append(arg)
                dir_paths.add(DIVIDER.join(cur_path))
            
            i += 1
            continue
        if 'ls' in line:
            i += 1
            line = inp[i]
            while not line.startswith('$'):
                type_, name = line.split()
                if type_ == 'dir':
                    fs = add_dir(fs, cur_path, name)
                else:
                    fs = add_file(fs, cur_path, name, type_)
                i += 1
                if i >= len(inp):
                    break
                line = inp[i]
    
    return fs, dir_paths


def add_dir(fs, path, name):
    if path[0] not in fs.keys():
        fs[path[0]] = {}
    
    if len(path) > 1:
        add_dir(fs[path[0]], path[1:], name)
    else:
        fs[path[0]][name] = {}
    
    return fs


def add_file(fs, path, name, size):
    if path[0] not in fs.keys():
        fs[path[0]] = {}
    
    if len(path) > 1:
        add_file(fs[path[0]], path[1:], name, size)
    else:
        fs[path[0]][name] = int(size)
    
    return fs


def get_size(fs, path):
    cur = fs
    for item in path:
        cur = cur[item]
    
    total = 0
    for key in cur.keys():
        if isinstance(cur[key], int):
            total += cur[key]
        else:
            total += get_size(cur[key], [])
    
    return total


def main():
    with open(r'd7_input.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
