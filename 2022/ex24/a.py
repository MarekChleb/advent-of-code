from copy import deepcopy
from glob import glob
from typing import List

from helpers import Line
from utils.board import Board
from utils.points import manhattan_dist
from utils.readlines import read_lines


moves = {
    '>': (1, 0),
    '^': (0, 1),
    '<': (-1, 0),
    'v': (0, -1)
}

def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))

def move_blizzard(x, y, typ, minx, maxx, miny, maxy, b):
    xx, yy = x, y
    x, y = plus((x, y), moves[typ])
    if x > maxx:
        x, y = minx, y
    if x < minx:
        x, y = maxx, y
    if y > maxy:
        x, y = x, miny
    if y < miny:
        x, y = x, maxy
    # if b.get((x, y)) != '.':
    #     return xx, yy
    return typ, x, y

def next_blizzard(b: Board, blizzards, minx, maxx, miny, maxy):
    nxt = deepcopy(b)
    nxt_blizzards = [move_blizzard(x, y, typ, minx, maxx, miny, maxy, nxt) for typ, x, y in blizzards]
    for _, x, y in blizzards:
        nxt.set((x, y), '.')
    for typ, x, y in nxt_blizzards:
        nxt.set((x, y), typ)

    return nxt, nxt_blizzards
def get_solution(lines: List[Line]) -> str:
    solution = 0

    ll = list(reversed([line.raw_line for line in lines]))
    start = 0, 0
    end = 0, 0
    blizzards = []
    for y, line in enumerate(ll):
        for x, c in enumerate(line):
            if c in moves:
                blizzards.append((c, x, y))
            if c == '.':
                if y > start[1]:
                    start = x, y
                if x > end[0]:
                    end = x, y
    b = Board(ll, default_el='#')

    print(b)
    print(blizzards)
    print(start, end)

    minx = 1
    maxx = end[0]
    miny = 1
    maxy = start[1] - 1

    t = 0
    q = [(0, start)]
    nxt_b, nxt_blizzards = next_blizzard(b, blizzards, minx, maxx, miny, maxy)

    while True:
        turn, pos = q.pop(0)

        if turn > t:
            print(t)
            t += 1
            b, blizzards = nxt_b, nxt_blizzards
            nxt_b, nxt_blizzards = next_blizzard(nxt_b, nxt_blizzards, minx, maxx, miny, maxy)
            q = sorted(list(set(q)), key=lambda z: manhattan_dist(z[1], end))[:100000]

        if pos == end:
            print(turn)
            solution = turn
            break

        nxt_moves = [pos] + nxt_b.around_non_diagonal(pos)
        for adj in nxt_moves:
            if nxt_b.get(adj) == '.':
                q.append((turn + 1, adj))



    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))