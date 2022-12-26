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
    bottom = 0
    stoned = {
        (k, bottom) for k in range(9)
    }
    # for k in range(10000):
    #     stoned.add((0, k))
    #     stoned.add((8, k))

    def f(x):
        ss = [1438, 2865, 4292, 5724, 7152, 8581, 11]

    max_h = bottom
    sti = 0
    l, nl = 0, 0
    luls = {}

    ustawienia = {}
    nns = {}
    for i in range(51726):
        rock = rocks[sti]
        rock = move_up(rock, max_h + 4)
        if sti == 0 and move_i == 0:
            print('okres', rock)

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
                if p[0] == 0 or p[0] == 8:
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
                # if sti == 0 and move_i == 0:
                #     print(rock)

                # if i % (len(move) * 5) == 0:
                #     l, nl = nl, rock[0][1]
                #     print(i, rock, rock[0][1] - i, nl - l - 76886)
                #     if nl - l == 76913:
                #         print('ding dong #################')
                c1 = ''.join(['#' if x in stoned else '.' for x in [(iii, max_h) for iii in range(1, 8)]])
                c2 = ''.join(['#' if x in stoned else '.' for x in [(iii, max_h-1) for iii in range(1, 8)]])
                c3 = ''.join(['#' if x in stoned else '.' for x in [(iii, max_h-2) for iii in range(1, 8)]])
                c4 = ''.join(['#' if x in stoned else '.' for x in [(iii, max_h-3) for iii in range(1, 8)]])

                nnn = '\n'.join([c1, c2, c3, c4])
                # print(nnn)
                #
                # print()
                # if sti == 4:
                luls[i] = max_h
                ustawienia[i] = nnn
                if nnn in nns:
                    tab = nns[nnn]
                    nns[nnn].append(i)
                    # print(i, [tab[i+1] - tab[i] for i in range(len(tab) - 1)], tab)
                else:
                    nns[nnn] = [i]

                break
        sti = (sti + 1) % len(rocks)

    def f(x, maxx, mod, mod_val=2630):
        modded_x = (x - maxx) % mod
        modded_val = luls[maxx + modded_x]
        okres_val = ((x - maxx) // mod) * mod_val
        return modded_val + okres_val
    # solution = max_h
    solution = f(1000000000000-1, 50000, 1725)
    return str(solution)


for filename in reversed(glob('input/*.in')):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
