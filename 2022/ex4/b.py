from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        li1, li2 = line.raw_line.split(',')
        l1, r1 = (int(x) for x in li1.split('-'))
        l2, r2 = (int(x) for x in li2.split('-'))
        if (l1 <= r2) and l2 <= r1:
            solution += 1

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
