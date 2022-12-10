import math
from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def dist(t1, t2):
    return int(max(math.fabs(t1[0] - t2[0]), math.fabs(t1[1] - t2[1])))

def get_solution(lines: List[Line]) -> str:
    solution = 0
    st = (0, 0)
    tail = (0, 0)
    visited = set()
    visited.add(tail)
    for line in lines:
        dx, dy = 0, 0
        dirr, amount = line.raw_line.split(' ')
        amount = int(amount)

        if dirr == 'R':
            dx = 1
            dy = 0
        elif dirr == 'L':
            dx = -1
            dy = 0
        elif dirr == 'U':
            dx = 0
            dy = 1
        elif dirr == 'D':
            dx = 0
            dy = -1

        for i in range(amount):
            prev = st
            st = (st[0] + dx, st[1] + dy)
            if dist(st, tail) > 1:
                tail = prev
                visited.add(tail)

    solution = len(visited)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
