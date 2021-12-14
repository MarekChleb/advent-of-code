from typing import List

from helpers import Line, Octopuses
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    solution = 0
    rows = []
    for line in lines:
        row = [int(v) for v in line.raw_line]
        rows.append(row)

    board = Octopuses(rows)
    flashed = 0

    while flashed != len(board):
        solution += 1
        flashed = board.flash()
    return str(solution)


print(get_solution(input_lines))