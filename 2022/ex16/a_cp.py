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

    print(g, flow)
    dyn = {}

    q = [('AA', 0, ['AA'], False, [0], {})]
    alll = [('AA', 0, ['AA'], False, [0], {})]
    earl = {}
    def kk(p, cr):
        return f'{cr}_{list(set(p)).sort()}'

    while len(q):
        valve, turn, path, wait_for_open, vv, moves = q.pop(0)
        # print(valve, turn, path, wait_for_open, vv, moves)
        if turn == 26:
            break
        if wait_for_open:
            vvv = vv.copy()
            vvv.append(vvv[-1] + flow[valve])
            el = (valve, turn + 1, path, False, vvv, moves)
            q.append(el)
            alll.append(el)
            continue

        for nn in g[valve]:
            if moves.get((valve, nn), 0) > 0:
                continue
            pp = path.copy()
            mm = moves.copy()
            mm[(valve, nn)] = mm.get((valve, nn), 0) + 1
            vvv = vv.copy()
            vvv.append(vv[-1])
            if nn not in path:
                pp.append(nn)
                el = (nn, turn + 1, pp, True, vvv, mm)
                q.append(el)
                alll.append(el)

            pp.append(nn)
            el = (nn, turn + 1, pp, False, vvv, mm)
            q.append(el)
            alll.append(el)

        # q.append((valve, turn+1, path, wait_for_open, vv, moves))

    # print(q)

    mmm = 0
    for valve, turn, path, wait_for_open, vv, moves in q:
        if vv[:9] == [0, 0, 20, 20, 20, 33, 33, 33, 33]:
            print(vv)
        ach = sum(vv) + (30 - turn) * vv[-1]
        if mmm < ach:
            mmm = ach
    solution = mmm
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
