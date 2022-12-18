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

    for valve in flow:

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
