from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0

    oks = set()
    while len(oks) < len(lines):
        for i, line in enumerate(lines):
            if i not in oks:
                try:
                    exec(line.raw_line.replace(':', '='))
                    oks.add(i)
                except NameError:
                    pass

    solution = 1
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
