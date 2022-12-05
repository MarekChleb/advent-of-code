from typing import List

from line import Line, BracketChecker
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        checker = BracketChecker(line.raw_line)
        solution += checker.check()
    return str(solution)


print(get_solution(input_lines))