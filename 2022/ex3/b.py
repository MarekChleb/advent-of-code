from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

def get_num(c: str):
    return ord(c) - 96 if c.islower() else ord(c.lower()) - 70


def get_solution(lines: List[Line]) -> str:
    solution = 0
    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i:i+3]
        p1, p2, p3 = l1.raw_line, l2.raw_line, l3.raw_line
        s1 = set(p1)
        s2 = set(p2)
        s3 = set(p3)
        c = next(iter(s1 & s2 & s3))
        # print(c, get_num(c), p1, p2, s1, s2)
        solution += get_num(c)

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
