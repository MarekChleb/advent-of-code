from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

rocks = [
    [(3, 0), (4, 0), (5, 0), (6, 0)],
    [(4, 0), (3, 1), (4, 1), (5, 1), (4, 2)],
    [(3, 0), (4, 0), (5, 0), (5, 1), (5, 2)],
    [(3, 0), (3, 1), (3, 2), (3, 3)],
    [(3, 0), (4, 0), (3, 1), (4, 1)]
]

def move_up(rock, v):
    return [(x, y + v) for x, y in rock]

def move_down(rock):
    return move_up(rock, -1)

def move_x(rock, v):
    return [(x + v, y) for x, y in rock]

def move_left(rock):
    return move_x(rock, -1)

def move_right(rock):
    return move_x(rock, 1)

def get_solution(lines: List[Line]) -> str:
    solution = 0
    move = ""
    for line in lines:
        move = line.raw_line
    move_i = 0

    stoned = {
        (k, 0) for k in range(9)
    }
    for k in range(10000):
        stoned.add((0, k))
        stoned.add((8, k))

    max_h = 0
    sti = 0
    for i in range(2022):
        rock = rocks[sti]
        rock = move_up(rock, max_h + 4)
        print(i, rock)

        while True:
            mm = move[move_i]
            move_i = (move_i + 1) % len(move)

            if mm == '>':
                tmp_r = move_right(rock)
            else:
                tmp_r = move_left(rock)
            move_possible = True
            for p in tmp_r:
                if p in stoned:
                    move_possible = False
                    break
            if move_possible:
                rock = tmp_r

            tmp_r = move_down(rock)
            move_possible = True
            for p in tmp_r:
                if p in stoned:
                    move_possible = False
                    break
            if move_possible:
                rock = tmp_r
            else:
                for p in rock:
                    stoned.add(p)
                    if p[1] > max_h:
                        max_h = p[1]
                break
        sti = (sti + 1) % len(rocks)

    solution = max_h
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
