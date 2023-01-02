from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

def around_point(p):
    x, y = p
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

def turn_left(dd):
    dx, dy = dd
    return -dy, dx

def turn_right(dd):
    dx, dy = dd
    return dy, -dx

def join(dic, A: list, dir_a, B: list, dir_b, reverse: bool):
    ll = reversed(A) if reverse else A
    for p_a, p_b in zip(ll, B):
        if p_a not in dic:
            dic[p_a] = {}
        if p_b not in dic:
            dic[p_b] = {}

        dx, dy = dir_b
        dic[p_a][dir_a] = (p_b, (-dx, -dy))

        dx, dy = dir_a
        dic[p_b][dir_b] = (p_a, (-dx, -dy))

A_t = [(149, y) for y in range(150, 200)]
A_b = [(99, y) for y in range(50, 100)]

B_t = [(x, 199) for x in range(100, 150)]
B_b = [(x, 0) for x in range(0, 50)]

C_t = [(x, 199) for x in range(50, 100)]
C_b = [(0, y) for y in range(0, 50)]

D_t = [(50, y) for y in range(150, 200)]
D_b = [(0, y) for y in range(50, 100)]

E_t = [(50, y) for y in range(100, 150)]
E_b = [(x, 99) for x in range(0, 50)]

F_t = [(x, 50) for x in range(50, 100)]
F_b = [(49, y) for y in range(0, 50)]

G_t = [(x, 150) for x in range(100, 150)]
G_b = [(99, y) for y in range(100, 150)]
def get_neighbours(b):
    neighbours = {}

    for p in b:
        nn = {}
        around = around_point(p)
        x, y = p
        for neigh in around:
            nx, ny = neigh
            dx, dy = x - nx, y - ny
            ddx, ddy = -dx, -dy
            tx, ty = x, y
            if neigh in b:
                nn[ddx, ddy] = (neigh, (ddx, ddy))

        neighbours[p] = nn


    join(neighbours, A_t, (1, 0), A_b, (1, 0), True)
    join(neighbours, B_t, (0, 1), B_b, (0, -1), False)
    join(neighbours, C_t, (0, 1), C_b, (-1, 0), True)
    join(neighbours, D_t, (-1, 0), D_b, (-1, 0), True)
    join(neighbours, E_t, (-1, 0), E_b, (0, 1), True)
    join(neighbours, F_t, (0, -1), F_b, (1, 0), True)
    join(neighbours, G_t, (0, -1), G_b, (1, 0), True)

    return neighbours

def get_solution(lines: List[Line]) -> str:
    solution = 0
    board = {}
    sx, sy = 10000, 0
    for y, line in enumerate(reversed(lines[:-2])):
        for x, c in enumerate(line.raw_line):
            if c != ' ':
                board[x, y] = c
                if y > sy:
                    sx, sy = x, y
    start = sx, sy
    adjacent = get_neighbours(board)
    # print(adjacent)

    moves = lines[-1].raw_line
    moves = sum(['#R#'.join(chunk.split('R')).split('#') + ['L'] for chunk in moves.split('L')], [])
    moves = moves[:-1]
    print(moves)

    dd = (1, 0)
    pos = start
    print(pos, dd)
    for move in moves:
        if move == 'R':
            dd = turn_right(dd)
        elif move == 'L':
            dd = turn_left(dd)
        else:
            num = int(move)
            for _ in range(num):
                dx, dy = dd
                x, y = pos
                pp, dd_temp = adjacent[x, y][dx, dy]
                if board[pp] != '#':
                    pos = pp
                    dd = dd_temp

        # print(pos, dd)

    print(pos, dd)
    row = len(lines) - pos[1] - 2
    column = pos[0] + 1
    facings = {(1, 0): 0, (0, -1): 1, (-1, 0): 2, (0, 1): 3}
    facing = facings[dd]
    print(row, column, facing)

    solution = 1000 * row + 4 * column + facing
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
