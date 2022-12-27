from glob import glob
from typing import List

from helpers import Line
from utils.board import Board
from utils.readlines import read_lines

def get_north_adj(b: Board, p):
    return [x for x in b.around(p) if x[1] > p[1]]

def get_south_adj(b: Board, p):
    return [x for x in b.around(p) if x[1] < p[1]]

def get_west_adj(b: Board, p):
    return [x for x in b.around(p) if x[0] < p[0]]

def get_east_adj(b: Board, p):
    return [x for x in b.around(p) if x[0] > p[0]]
def get_solution(lines: List[Line]) -> str:
    solution = 0
    bb = []
    elves = {}
    for y, line in enumerate(reversed(lines)):
        bb.append(line.raw_line)
        for x, c in enumerate(line.raw_line):
            if c == '#':
                elves[(x, y)] = ([
                    (get_north_adj, (0, 1)),
                    (get_south_adj, (0, -1)),
                    (get_west_adj, (-1, 0)),
                    (get_east_adj, (1, 0))
                ])

    b = Board(bb, default_el='.')
    print(b)
    for i in range(10):
        want_to_move = {}
        occupy_spot_count = {}
        for elf in elves:
            all_adj = b.around(elf)
            props = [b.get(x) for x in all_adj if b.get(x) != '.']
            if len(props) == 0:
                want_to_move[elf] = elf
                occupy_spot_count[elf] = occupy_spot_count.get(elf, 0) + 1
            else:
                new_elf = elf
                for fun, dp in elves[elf]:
                    props = [b.get(x) for x in fun(b, elf) if b.get(x) != '.']

                    if len(props) == 0:
                        new_elf = tuple(e1 + e2 for e1, e2 in zip(elf, dp))
                        break

                want_to_move[elf] = new_elf
                occupy_spot_count[new_elf]  = occupy_spot_count.get(new_elf, 0) + 1

        new_elves = {}
        for elf in elves:
            new_pos = want_to_move[elf]
            movements = elves[elf]
            new_movements = movements[1:] + [movements[0]]
            if new_pos == elf:
                new_elves[elf] = new_movements
            elif occupy_spot_count[new_pos] == 1:
                b.move(elf, new_pos)
                new_elves[new_pos] = new_movements
            else:
                new_elves[elf] = new_movements

        print(len(new_elves), len(elves))
        elves = new_elves

        # print(b)


    print(b)
    minx, maxx = 1000000, -1000000
    miny, maxy = 1000000, -1000000
    for elf in elves:
        x, y = elf
        if minx > x:
            minx = x
        if maxx < x:
            maxx = x
        if miny > y:
            miny = y
        if maxy < y:
            maxy = y


    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if b.get((x, y)) == '.':
                solution += 1
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
