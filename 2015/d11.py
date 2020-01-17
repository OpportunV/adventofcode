import re


def part_one(inp):
    return ''.join(get_new_password(list(inp)))


def part_two(inp):
    return ''.join(get_new_password(list(part_one(list(inp)))))


def has_straight(password):
    return any(ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2
               for i in range(0, len(password)-2))


def has_double_letter(password):
    return bool(re.match(r'^.*(.)\1.*(.)\2.*$', "".join(password)))


def has_no_bad_letters(password):
    return not any(bad_letter in password for bad_letter in ['i', 'o', 'l'])


def is_good_password(password):
    return has_straight(password) and has_double_letter(password) and has_no_bad_letters(password)


def increment_password(password):
    password[-1] = 'a' if ord(password[-1]) + 1 > ord('z') else chr(ord(password[-1]) + 1)
    return password if password[-1] != 'a' else increment_password(password[:-1]) + ['a']


def get_new_password(old_password):
    new_password = increment_password(old_password)
    while not is_good_password(new_password):
        new_password = increment_password(new_password)
    return new_password


def main():
    inp = 'cqjxjnds'
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
