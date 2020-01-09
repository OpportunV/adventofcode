import hashlib
from concurrent import futures
from datetime import datetime


def search(inp, start, step, pattern, res=None):
    i = start
    while not hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest().startswith(pattern):
        i += step
        if res:
            return
    
    if res is not None:
        res.append(i)
    return i


def part_one(inp):
    return search(inp, 0, 1, '00000')


def part_two(inp):
    workers = 4
    fs = []
    res = []
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(workers):
            f = executor.submit(search, inp, i, workers, '000000', res)
            fs.append(f)
        
    return res[0]
        
        
def main():
    inp = 'iwrupvqb'
    
    print(part_one(inp))
    a = datetime.now()
    print(part_two(inp))
    print(datetime.now() - a)
    
    
if __name__ == '__main__':
    main()
