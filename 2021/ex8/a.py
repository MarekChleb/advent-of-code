from typing import List

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    lens = {k: 0 for k in [2, 3, 4, 7]}
    for line in lines:
        for out in line.output:
            if len(out) in lens:
                lens[len(out)] += 1
    solution = sum(lens.values())
    return str(solution)


print(get_solution(input_lines))