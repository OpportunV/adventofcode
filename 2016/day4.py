from collections import Counter

KEY = 'northpole'


def part_one(inp):
    counter = 0
    for line in inp:
        data, checksum = line[:-1].split('[')
        *name, room_id = data.split('-')
        room_id = int(room_id)
        name_counter = Counter(''.join(name))
        name_letters = sorted(name_counter.keys())
        name_letters = set(sorted(name_letters, key=lambda letter: name_counter[letter], reverse=True)[:5])
        if not name_letters.difference(checksum):
            counter += room_id
    
    return counter


def part_two(inp):
    for line in inp:
        data, checksum = line[:-1].split('[')
        *name, room_id = data.split('-')
        room_id = int(room_id)
        name = ''.join(name)
        name_counter = Counter(name)
        name_letters = sorted(name_counter.keys())
        name_letters = set(sorted(name_letters, key=lambda letter: name_counter[letter], reverse=True)[:5])
        if not name_letters.difference(checksum):
            decrypted = decrypt(name, room_id)
            if KEY in decrypted:
                return room_id
    
    return 'Not found'


def decrypt(name, rotations):
    a = ord('a')
    return ''.join([chr((ord(letter) - a + rotations) % 26 + a) for letter in name])


def main():
    with open('input/day4.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))


if __name__ == '__main__':
    main()
