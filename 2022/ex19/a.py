from glob import glob
from typing import List

import parse

from helpers import Line, Blueprint, Blueprint2
from utils.readlines import read_lines

b_format = """Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian."""

def get_solution(lines: List[Line]) -> str:
    solution = 0
    bps = []
    for line in lines:
        bid, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_clay = parse.parse(b_format, line.raw_line)
        # bps.append(Blueprint(bid, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_clay))
        # print(bid, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_clay)
        b = Blueprint2(bid, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_clay)
        solution += b.get_value()
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
