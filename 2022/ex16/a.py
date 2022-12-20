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
    current_level = 0
    cum_level = 0
    turn = 0
    opened = set()
    q = [(turn, 'AA', opened, current_level, cum_level)]
    tt = 0
    while len(q) > 0:
        turn, node, opened, current_level, cum_level = q.pop(0)
        if tt < turn:
            print(turn)
            tt += 1
            q = sorted(q, key=lambda x: x[4], reverse=True)[:100000]

        if turn == 30:
            break

        if node not in opened:
            opened_cp = opened.copy()
            opened_cp.add(node)
            next_level = current_level + flow[node]
            q.append((turn + 1, node, opened_cp, next_level, cum_level + current_level))

        for neigh in g[node]:
            opened_cp = opened.copy()
            q.append((turn + 1, neigh, opened_cp, current_level, cum_level + current_level))

    # print(q)
    solution = max(q, key=lambda x: x[4])
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
