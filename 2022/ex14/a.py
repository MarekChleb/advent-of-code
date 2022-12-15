import math
from glob import glob
from typing import List

from helpers import Line
from utils.board import Board
from utils.readlines import read_lines

def get_xy(x):
    return x // 10, x % 10

def down(x):
    return x[0], x[1]+1

def left_down(x):
    return x[0] - 1, x[1]+1

def right_down(x):
    return x[0] + 1, x[1] + 1

def get_y_wall(x1, x2):
    return list(range(x1, x2+ 11, 10))

def get_x_wall(x1, x2):
    return list(range(x1, x2 + 1))

def is_x_wall(x1, x2):
    xx1, _ = get_xy(x1)
    xx2, _ = get_xy(x2)
    return xx1 == xx2
def get_solution(lines: List[Line]) -> str:
    walls = set()
    solution = 0
    min_y = 0
    for line in lines:
        wall_d = [x.split(',') for x in line.raw_line.split(' -> ')]
        wall_d = [(int(x[0]), int(x[1])) for x in wall_d]
        for i in range(len(wall_d) - 1):
            w1, w2 = sorted([wall_d[i], wall_d[i + 1]])
            x1, y1 = w1
            x2, y2 = w2
            if x1 == x2:
                print('add x wall', w1, w2)
                y1, y2 = sorted([y1, y2])
                for w in [(x1, y) for y in range(y1, y2+1)]:
                    walls.add(w)
            else:
                print('add y wall', w1, w2)
                x1, x2 = sorted([x1, x2])
                for w in [(x, y1) for x in range(x1, x2+1)]:
                    walls.add(w)

            if min_y < max(y1, y2):
                min_y = max(y1, y2)

    print(len(walls), walls)
    sands = set()
    while True:
        s = (500, 0)
        while s[1] < min_y:
            d = down(s)
            if d in walls or d in sands:
                d = left_down(s)
                if d in walls or d in sands:
                    d = right_down(s)
                    if d in walls or d in sands:
                        sands.add(s)
                        break
                    else:
                        s = d
                else:
                    s = d
            else:
                s = d
        solution += 1
        if s[1] == min_y:
            break
    print(len(sands), sands)

    # b = Board(['..........'] * 10, default_el='.', key_func=lambda x: (x[0]+494, x[1]))
    # b.set_key_func(lambda x: (x[0], x[1]))
    # for w in walls:
    #     b.set(get_xy(w), '#')
    # for s in walls:
    #     b.set(get_xy(s), 'o')

    # print(b)
    solution = len(sands)

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
