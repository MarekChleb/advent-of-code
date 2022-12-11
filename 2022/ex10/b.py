from glob import glob
from typing import List

import parse

from helpers import Line
from utils.board import Board
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    cycles = [1]
    for i in range(len(lines)):
        line = lines[i]
        if line.raw_line.startswith('noop'):
            i += 1
            cycles.append(cycles[-1])
            continue
        addx = parse.parse('addx {}', line.raw_line)
        addx = int(addx[0])
        cycles.append(cycles[-1])
        cycles.append(cycles[-1] + addx)
        i+=1

    ll = []
    for y in range(6):
        ll.append([])
        for x in range(40):
            ll[y].append('#' if x - 1<=cycles[y*40 + x] <=x+1 else '.')
        print(''.join(ll[y]))

    print()
    b = Board(ll, default_el='.')
    print(b)

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
