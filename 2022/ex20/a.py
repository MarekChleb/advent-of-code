from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

def move(x, i, v):
    vv = v[0]
    vi = (i + vv) % (len(x) - 1)
    x.pop(i)
    x.insert(vi, v)

def get_mod(x, i, ad):
    return x[(i + ad) % len(x)]
def get_solution(lines: List[Line]) -> str:
    solution = 0
    dd = []
    ds = set()
    zero = ()
    for i, line in enumerate(lines):
        v = int(line.raw_line)
        dd.append((v, i))
        if v == 0:
           zero = (v, i)

    cpd = dd.copy()
    # print(dd)
    for v, i in cpd:
        gi = dd.index((v, i))
        move(dd, gi, (v, i))
    # print(dd)

    zero_i = dd.index(zero)
    solution = get_mod(dd, zero_i, 1000)[0] + get_mod(dd, zero_i, 2000)[0] + get_mod(dd, zero_i, 3000)[0]



    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
