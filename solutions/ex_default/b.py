from typing import List

from line import Line
from utils.readlines import read_lines

lines = read_lines(Line)


def get_solution(_lines: List[Line]) -> str:
    print(_lines[0])
    solution = 0
    return str(solution)


print(get_solution(lines))