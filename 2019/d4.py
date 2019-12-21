def part_one(l_b=357_253, r_b=892_942):
    total_correct = 0
    for i in range(l_b, r_b + 1):
        passwd = str(i)

        if ''.join(sorted(passwd)) != passwd:
            continue
        
        if not has_doublets(passwd):
            continue
        
        total_correct += 1
    
    print(total_correct)
        
        
def has_doublets(string: str):
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            if not has_triplets(string, string[i]):
                return True
    return False


def has_triplets(string: str, value):
    for i in range(1, len(string) - 1):
        if string[i - 1] == string[i] == string[i + 1] == value:
            return True
    
    return False


part_one()  # accidentally rewrited part_one for part_two
