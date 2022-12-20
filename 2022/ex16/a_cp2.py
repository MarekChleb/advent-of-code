from glob import glob
from typing import List

import parse

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    g = {}
    flow = {}
    for line in lines:
        valve, rate, _, _, _, valves = parse.parse('Valve {} has flow rate={:d}; {} {} to {} {}', line.raw_line)
        # valves.lstrip('valve ').lstrip('valves ')
        valves = valves.split(', ')
        g[valve] = valves
        flow[valve] = rate

    # print(g, flow)
    dyn = {}

    q = [('AA', 1, set(), 0, 0)]
    alll = [('AA', 1, set(), 0, 0)]
    earl = {}
    def kk(p, op, l):
        return f'{p}_{l}_{op}'

    came_from = {}

    shown = set()
    while len(q):
        valve, turn, opened, cv, sss = q.pop(0)
        if turn not in shown:
            print(turn)
            shown.add(turn)
            q = sorted(q, key=lambda x: x[4], reverse=True)[:10000]
        if turn == 30:
            break

        k = kk(valve, opened, cv)

        if valve not in opened:
            pp = opened.copy()
            pp.add(valve)
            v = flow[valve] + cv
            el = (valve, turn + 1, pp, v, sss + v)
            q.append(el)
            alll.append(el)
            kn = kk(valve, pp, v)
            came_from[kn] = k

        for nn in g[valve]:
            kn = kk(nn, opened, cv)
            if kn not in came_from:
                pp = opened.copy()
                el = (nn, turn + 1, pp, cv, sss + cv)
                q.append(el)
                alll.append(el)
                came_from[kn] = k

    # print(alll)

    # print(came_from)
    mmm = 0
    for valve, turn, opened, cv, sss in alll:
        ach = sss + (30 - turn) * cv
        if mmm < ach:
            mmm = ach
    solution = mmm
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
