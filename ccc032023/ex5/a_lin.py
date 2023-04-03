import math
from glob import glob
from typing import List

from ortools.sat.python import cp_model

from helpers import Line
from utils.readlines import read_lines

wins = {
    'PP': 'P',
    'RR': 'R',
    'SS': 'S',
    'LL': 'L',
    'YY': 'Y',
    'PR': 'P',
    'RP': 'P',
    'PY': 'P',
    'YP': 'P',
    'RS': 'R',
    'SR': 'R',
    'RL': 'R',
    'LR': 'R',
    'SP': 'S',
    'PS': 'S',
    'SL': 'S',
    'LS': 'S',
    'LP': 'L',
    'PL': 'L',
    'LY': 'L',
    'YL': 'L',
    'YS': 'Y',
    'SY': 'Y',
    'YR': 'Y',
    'RY': 'Y'
}


# def generate_tournament(winner, r, p, s, y, l) -> bool:
#     generate_tournament(winner, r, p, s - 1, )


def get_solution(lines: List[Line]) -> str:
    solution = []
    _, nums = lines[0].raw_line.split(" ")
    nums = int(nums)
    for yyyyy, line in enumerate(lines[1:]):
        print(yyyyy)
        ret = ''
        r, p, s, y, l = line.raw_line.split(" ")
        r = int(r[:-1])
        p = int(p[:-1])
        s = int(s[:-1])
        y = int(y[:-1])
        l = int(l[:-1])

        rr = {}
        pp = {}
        ss = {}
        yy = {}
        ll = {}

        model = cp_model.CpModel()

        lvls = int(math.log2(nums)) + 1
        # print(lvls)
        nums2 = nums
        for lll in range(lvls):
            for k in range(nums2):
                kkk = (lll, k)
                rr[kkk] = model.NewIntVar(0, 1, f'[rr{kkk}]')
                pp[kkk] = model.NewIntVar(0, 1, f'[pp{kkk}]')
                ss[kkk] = model.NewIntVar(0, 1, f'[ss{kkk}]')
                yy[kkk] = model.NewIntVar(0, 1, f'[yy{kkk}]')
                ll[kkk] = model.NewIntVar(0, 1, f'[ll{kkk}]')

                model.Add(rr[kkk] + pp[kkk] + ss[kkk] + yy[kkk] + ll[kkk] == 1)

                if lll > 0:
                    model.Add(6 * rr[kkk] <= 6 + (
                        3 * rr[lll - 1, 2 * k] + 3 * rr[lll - 1, 2 * k + 1] + ss[lll - 1, 2 * k] + ss[lll - 1, 2 * k + 1] +
                        ll[lll - 1, 2 * k] + ll[lll - 1, 2 * k + 1]
                        - 4))
                    model.Add(6 * ss[kkk] <= 6 + (
                        3 * ss[lll - 1, 2 * k] + 3 * ss[lll - 1, 2 * k + 1] + pp[lll - 1, 2 * k] + pp[lll - 1, 2 * k + 1] +
                        ll[lll - 1, 2 * k] + ll[lll - 1, 2 * k + 1]
                        - 4))
                    model.Add(6 * ll[kkk] <= 6 + (
                        3 * ll[lll - 1, 2 * k] + 3 * ll[lll - 1, 2 * k + 1] + pp[lll - 1, 2 * k] + pp[lll - 1, 2 * k + 1] +
                        yy[lll - 1, 2 * k] + yy[lll - 1, 2 * k + 1]
                        - 4))
                    model.Add(6 * yy[kkk] <= 6 + (
                        3 * yy[lll - 1, 2 * k] + 3 * yy[lll - 1, 2 * k + 1] + ss[lll - 1, 2 * k] + ss[lll - 1, 2 * k + 1] +
                        rr[lll - 1, 2 * k] + rr[lll - 1, 2 * k + 1]
                        - 4))
                    model.Add(6 * pp[kkk] <= 6 + (
                        3 * pp[lll - 1, 2 * k] + 3 * pp[lll - 1, 2 * k + 1] + rr[lll - 1, 2 * k] + rr[lll - 1, 2 * k + 1] +
                        yy[lll - 1, 2 * k] + yy[lll - 1, 2 * k + 1]
                        - 4))


            nums2 = nums2 // 2

        model.Add(ss[(lvls - 1, 0)] == 1)


        model.Add(sum([rr[(0, q)] for q in range(nums)]) == r)
        model.Add(sum([ss[(0, q)] for q in range(nums)]) == s)
        model.Add(sum([pp[(0, q)] for q in range(nums)]) == p)
        model.Add(sum([ll[(0, q)] for q in range(nums)]) == l)
        model.Add(sum([yy[(0, q)] for q in range(nums)]) == y)

        model.Maximize(sum(rr[k] for k in rr) + sum(ss[k] for k in ss) + sum(pp[k] for k in pp) + sum(yy[k] for k in yy) + sum(ll[k] for k in ll))

        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        # print(f'status is {"optimal" if status == cp_model.OPTIMAL else "feasible or not"}')
        # print(f'number of beacons in range: {solver.ObjectiveValue()}')

        for k in range(nums):
            kk = (0, k)
            if solver.Value(rr[kk]) == 1:
                ret += 'R'
            elif solver.Value(pp[kk]) == 1:
                ret += 'P'
            elif solver.Value(ss[kk]) == 1:
                ret += 'S'
            elif solver.Value(ll[kk]) == 1:
                ret += 'L'
            elif solver.Value(yy[kk]) == 1:
                ret += 'Y'


        solution.append(ret)

    return str('\n'.join(solution))


for i, filename in enumerate(sorted(glob('input/*.in'))):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename)
    print(get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
