from typing import List

from line import Line, BracketChecker
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    solution = 0
    solutions = []
    for line in lines:
        checker = BracketChecker(line.raw_line)
        if checker.check() == 0:
            solutions += [checker.closing_value()]

    solutions = sorted(solutions)
    solution = solutions[len(solutions)//2]

    return str(solution)


print(get_solution(input_lines))