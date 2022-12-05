from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

def get_num(c: str):
    return ord(c) - 96 if c.islower() else ord(c.lower()) - 70


def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        p1, p2 = line.raw_line[:len(line.raw_line)//2], line.raw_line[len(line.raw_line)//2:]
        s1 = set(p1)
        s2 = set(p2)
        c = next(iter(s1 & s2))
        # print(c, get_num(c), p1, p2, s1, s2)
        solution += get_num(c)

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
