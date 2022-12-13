from glob import glob
from typing import List

from helpers import Line
from utils.board import Board
from utils.readlines import read_lines

def get_num(c: str):
    if c == 'S':
        return 27
    if c == 'E':
        return 0
    return 27 - (ord(c) - 96 if c.islower() else ord(c.lower()) - 70)

def get_solution(lines: List[Line]) -> str:
    solution = 0
    rows = []
    for line in lines:
        rows.append(line.raw_line)

    b = Board[str](rows, default_el='.')
    # print(b)

    start = None
    for x in range(137):
        for y in range(41):
            if b.get((x, y)) == 'E':
                start = (x, y)

    q = [start]
    fromm = {start: start}
    stop = (0, 0)

    while len(q) > 0:
        # print(q)
        el = q.pop(0)
        x, y = el
        if b.get(el) == 'a':
            stop = el
            break
        neigs = b.around_non_diagonal((x, y))
        curr_val = b.get(el)
        curr_val = get_num(curr_val)

        for ne in neigs:
            if ne not in fromm:
                ne_val = get_num(b.get(ne))
                if curr_val + 1 >= ne_val:
                    fromm[ne] = el
                    if ne is not None:
                        q.append(ne)

    ell = stop
    while fromm.get(ell) is not None:
        if ell == fromm.get(ell):
            break
        solution += 1
        ell = fromm.get(ell)
        # print(ell)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
