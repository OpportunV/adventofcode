import re


def get_nums(line):
    return list(map(int, re.findall(r'-?\d+', line)))