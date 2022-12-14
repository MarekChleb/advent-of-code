import functools
from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


ccc = {}

def keys(x, y):
    return f'{x}_{y}'
def comp(x, y):
    k1 = keys(x, y)
    if k1 in ccc:
        return ccc[k1]

    k = f'{x}_{y}'
    if type(x) == type(y):
        if type(x) == type(1):
            if x == y:
                ccc[k] = 0
                return 0
            v = 1 if x < y else -1
            ccc[k] = v
            return v
        for i, valx in enumerate(x):
            if i == len(y):
                ccc[k] = -1
                return -1
            valy = y[i]
            cc = comp(valx, valy)
            if cc != 0:
                ccc[k] = cc
                return cc
        if len(x) < len(y):
            ccc[k] = 1
            return 1
        return 0
    if type(x) == type(1):
        v = comp([x], y)
        ccc[k] = v
        return v
    v = comp(x, [y])
    ccc[k] = v
    return v
def get_solution(lines: List[Line]) -> str:
    solution = 0
    j = 1
    dd = [[[2]], [[6]]]
    for i in range(0, len(lines), 3):
        p1 = eval(lines[i].raw_line)
        p2 = eval(lines[i+1].raw_line)

        dd.append(p1)
        dd.append(p2)

    dd.sort(key=functools.cmp_to_key(comp), reverse=True)
    print(dd)
    ind2 = dd.index([[2]]) + 1
    ind6 = dd.index([[6]]) + 1
    solution = ind2 * ind6

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
