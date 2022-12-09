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

            minn = -1

            ss = 0
            for dx in range(x+1, len_row):
                curr = rows[y][dx]
                if curr < val:
                    ss += 1
                else:
                    ss += 1
                    break
            xr = ss

            ss = 0
            for dx in range(x - 1, -1, -1):
                curr = rows[y][dx]
                if curr < val:
                    ss += 1
                else:
                    ss += 1
                    break
            xl = ss

            ss = 0
            for dy in range(y+1, len(rows)):
                curr = rows[dy][x]
                if curr < val:
                    ss += 1
                else:
                    ss += 1
                    break
            yd = ss

            ss = 0
            for dy in range(y -1, -1, -1):
                curr = rows[dy][x]
                if curr < val:
                    ss += 1
                else:
                    ss += 1
                    break
            yu = ss

            drs = xr * xl * yd * yu
            print(x, y, xr, xl, yd, yu)
            if drs > solution:
                solution = drs


    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
