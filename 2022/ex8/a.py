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

    visible = set()
    for x in range(len_row):
        min_row = -1
        for y in range(len(rows)):
            val = rows[y][x]
            if val > min_row:
                visible.add((x, y))
                min_row = val

    for x in range(len_row):
        min_row = -1
        for y in range(len(rows)-1, -1, -1):
            val = rows[y][x]
            if val > min_row:
                visible.add((x, y))
                min_row = val

    for y in range(len(rows)):
        min_row = -1
        for x in range(len_row):
            val = rows[y][x]
            if val > min_row:
                visible.add((x, y))
                min_row = val

    for y in range(len(rows)):
        min_row = -1
        for x in range(len_row-1, -1, -1):
            val = rows[y][x]
            if val > min_row:
                visible.add((x, y))
                min_row = val

    solution = len(visible)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
