import math
from glob import glob
from typing import List

import parse
from ortools.sat.python import cp_model

from helpers import Line
from utils.readlines import read_lines

def dist(p1, p2):
    return int(math.fabs(p1[0] - p2[0]) + math.fabs(p1[1] - p2[1]))

def neighs(p, d, yy):
    x, y = p
    a = []
    dyy = int(math.fabs(y - yy))
    dxx = d - dyy
    for dx in range(-dxx, dxx + 1):
        if dx == 0 and yy == y:
            continue
        a.append((x + dx, yy))

    return a
def get_solution(lines: List[Line]) -> str:
    solution = 0
    sens = set()
    beacons = set()
    imposs = set()
    model = cp_model.CpModel()
    # inf = cp_model.INT_MAX
    inf = 2137213721
    u = {}
    maxx = 4000000
    solved_x = model.NewIntVar(0, maxx, 'x')
    solved_y = model.NewIntVar(0, maxx, 'y')
    yx = {}
    yy = {}

    for line in lines:
        sx, sy, bx, by = parse.parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', line.raw_line)
        sens.add((sx, sy))
        s = (sx, sy)
        beacons.add((bx, by))
        dd = dist((sx, sy), (bx, by))
        u[s] = model.NewIntVar(0, 1, f'u[{s}]')
        yx[s] = model.NewIntVar(0, 1, f'yx[{s}]')
        yy[s] = model.NewIntVar(0, 1, f'yy[{s}]')

        # https://optimization.cbe.cornell.edu/index.php?title=Optimization_with_absolute_values
        model.Add(solved_x - sx + yx[s] * inf + solved_y - sy + yy[s] * inf > dd + (u[s] - 1) * inf)
        model.Add(solved_x - sx + yx[s] * inf - solved_y + sy + (1 - yy[s]) * inf > dd + (u[s] - 1) * inf)
        model.Add(-solved_x + sx + (1 - yx[s]) * inf + solved_y - sy + yy[s] * inf > dd + (u[s] - 1) * inf)
        model.Add(-solved_x + sx + (1 - yx[s]) * inf - solved_y + sy + (1 - yy[s]) * inf > dd + (u[s] - 1) * inf)

    model.Maximize(sum([u[i] for i in u]))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    print(f'status is {"optimal" if status == cp_model.OPTIMAL else "feasible or not"}')
    print(f'number of beacons in range: {solver.ObjectiveValue()}')

    solved_x_value = solver.Value(solved_x)
    solved_y_value = solver.Value(solved_y)

    print(solved_x_value, solved_y_value)
    solution = solved_x_value * 4000000 + solved_y_value
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
