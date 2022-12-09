from glob import glob
from typing import List

from helpers import Line
from utils.board import Board
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    rows = []
    len_row = 0
    for line in lines:
        rows.append([int(x) for x in line.raw_line])
        len_row = len(line.raw_line)

    b = Board[int](rows, default_el=0)
    print(b, b.get((0, 0)))

    solution = len([])
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
