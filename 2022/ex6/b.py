from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        raw = line.raw_line
        for i in range(0, len(line.raw_line) - 14):
            nn = raw[i:i+14]
            if len(set(nn)) == 14:
                solution = i + 14
                break
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
