from glob import glob
from typing import List

import parse

from helpers import Line
from utils.readlines import read_lines

# znajdz odleglosc każdego od każdego
# zrób dynamica od dołu -> dyn[el, tura] = (otwarte, najlepszy wynik)
# dla sasiad, droga od el -> dyn[el, tura] = dyn[sasiad, tura - droga - 1] jeśli el nie w sasiadowych otwartych
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

    for v in flow:
        dyn[(v, 0)] = (0, set(), 0)

    # dyn[('AA', 0)] = (0, set(), 0)
    for i in range(1, 31):
        for v in flow:

            nei = [(dyn[(nn, i - 1)][0] + dyn[(nn, i - 1)][2], dyn[(nn, i - 1)][1], dyn[(nn, i - 1)][2]) for nn in g[v] if (nn, i-1) in dyn]
            if (v, i-1) in dyn:
                a, b, c = dyn[(v, i - 1)]
                if v not in b:
                    bb = b.copy()
                    bb.add(v)
                    nei += [(a + c + flow[v], bb, c + flow[v])]
                else:
                    nei += [(a + c, b, c)]

            sorted_nn = sorted(nei, key=lambda x: (x[0], x[2]), reverse=True)
            # print(sorted_nn)
            if len(sorted_nn) == 0:
                continue
            a, b, c = sorted_nn[0]
            bb = b.copy()
            dyn[(v, i)] = (a, bb, c)
            print(f'dyn[{(v, i)}] = {dyn[(v, i)]}')

    # print(alll)

    print(dyn)
    print(dyn[('AA', 28)])
    mmm = 0
    # for valve, turn, opened, cv, sss in alll:
    #     ach = sss + (30 - turn) * cv
    #     if mmm < ach:
    #         mmm = ach
    solution = mmm
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
