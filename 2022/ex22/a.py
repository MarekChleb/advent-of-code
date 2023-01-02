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
                nn[ddx, ddy] = neigh
            else:
                while (tx + dx, ty + dy) in b:
                    tx += dx
                    ty += dy

                nn[ddx, ddy] = (tx, ty)
        neighbours[p] = nn

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
                tx, ty = adjacent[x, y][dx, dy]
                if board[tx, ty] != '#':
                    pos = (tx, ty)
        print(pos, dd)

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
