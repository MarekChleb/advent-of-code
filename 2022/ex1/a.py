from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    mm, ss = 0, 0
    for line in lines:
        if line.raw_line == "":
            mm = ss if ss > mm else mm
            ss = 0
            continue
        ss += int(line.raw_line)
    return str(mm)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
