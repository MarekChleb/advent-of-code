import math
from glob import glob
from typing import List

from ortools.sat.python import cp_model

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    model = cp_model.CpModel()
    # inf = cp_model.INT_MAX
    inf = 2137213721
    u = {}

    solved_x = model.NewIntVar(-inf, inf, 'x')
    solved_y = model.NewIntVar(-inf, inf, 'y')
    solved_z = model.NewIntVar(-inf, inf, 'z')

    solution = 0

    points = {}
    i = 0
    for line in lines:
        x, y, z, r = line.x, line.y, line.z, line.r
        points[i] = (x, y, z)
        u[i] = model.NewIntVar(0, 1, f'u[{i}]')
        model.Add(solved_x - x + solved_y - y + solved_z - z <= r + (1 - u[i]) * inf)
        model.Add(solved_x - x - solved_y + y + solved_z - z <= r + (1 - u[i]) * inf)
        model.Add(solved_x - x + solved_y - y - solved_z + z <= r + (1 - u[i]) * inf)
        model.Add(solved_x - x - solved_y + y - solved_z + z <= r + (1 - u[i]) * inf)
        model.Add(-solved_x + x + solved_y - y + solved_z - z <= r + (1 - u[i]) * inf)
        model.Add(-solved_x + x - solved_y + y + solved_z - z <= r + (1 - u[i]) * inf)
        model.Add(-solved_x + x + solved_y - y - solved_z + z <= r + (1 - u[i]) * inf)
        model.Add(-solved_x + x - solved_y + y - solved_z + z <= r + (1 - u[i]) * inf)
        i += 1

    model.Maximize(sum([u[i] for i in u]))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    print(f'status is {"optimal" if status == cp_model.OPTIMAL else "feasible or not"}')
    print(f'number of nanobots in range: {solver.ObjectiveValue()}')

    solved_x_value = solver.Value(solved_x)
    solved_y_value = solver.Value(solved_y)
    solved_z_value = solver.Value(solved_z)
    print(f'x = {solved_x_value}, y = {solved_y_value}, z = {solved_z_value}')
    # for ii in u:
    #     if solver.Value(u[ii]) == 1:
    #         print(f'{u[ii]} -> {points[ii]}')

    solution = math.fabs(solved_x_value) + math.fabs(solved_y_value) + math.fabs(solved_z_value)
    return str(solution)


# def get_solution(lines: List[Line]) -> str:
#     solver = pywraplp.Solver.CreateSolver('SCIP')
#     inf = solver.infinity()
#     # inf = 213721372
#     u = {}
#
#     solved_x = solver.IntVar(-inf, inf, 'x')
#     solved_y = solver.IntVar(-inf, inf, 'y')
#     solved_z = solver.IntVar(-inf, inf, 'z')
#
#     solution = 0
#
#     points = {}
#     i = 0
#     for line in lines:
#         x, y, z, r = line.x, line.y, line.z, line.r
#         points[i] = (x, y, z)
#         u[i] = solver.IntVar(0, 1, f'u[{i}]')
#         print(x, y, z, r)
#         solver.Add(solved_x - x + solved_y - y + solved_z - z <= r + (1 - u[i]) * inf)
#         solver.Add(solved_x - x - solved_y + y + solved_z - z <= r + (1 - u[i]) * inf)
#         solver.Add(solved_x - x + solved_y - y - solved_z + z <= r + (1 - u[i]) * inf)
#         solver.Add(solved_x - x - solved_y + y - solved_z + z <= r + (1 - u[i]) * inf)
#         solver.Add(-solved_x + x + solved_y - y + solved_z - z <= r + (1 - u[i]) * inf)
#         solver.Add(-solved_x + x - solved_y + y + solved_z - z <= r + (1 - u[i]) * inf)
#         solver.Add(-solved_x + x + solved_y - y - solved_z + z <= r + (1 - u[i]) * inf)
#         solver.Add(-solved_x + x - solved_y + y - solved_z + z <= r + (1 - u[i]) * inf)
#         i += 1
#
#     solver.Maximize(solver.Sum([u[i] for i in u]))
#
#     status = solver.Solve()
#
#     print(solver.constraints())
#     print(f'status is {"optimal" if status == pywraplp.Solver.OPTIMAL else "feasible or not"}')
#     print(f'number of nanobots in range: {solver.Objective().Value()}')
#     print(f'x = {solved_x.solution_value()}, y = {solved_y.solution_value()}, z = {solved_z.solution_value()}')
#     for ii in u:
#         if u[ii].solution_value() == 1:
#             print(f'{u[ii]} -> {points[ii]}')
#
#     return str(solution)

for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))

# input_lines = read_lines(Line, 'input/example.in')
# print('input/example.in', get_solution(input_lines))
