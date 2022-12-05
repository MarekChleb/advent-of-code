from glob import glob
from typing import List

from parse import parse

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    row_line_idx = 0
    cols = 0
    i = 0
    for line in lines:
        if line.raw_line.startswith(' 1'):
            row_line_idx = i
            cols = len(line.raw_line.split('   '))
            break
        i += 1

    stacks = [[] for _ in range(cols)]
    for i, line in enumerate(lines):
        if i > row_line_idx - 1:
            break
        for j in range(0, len(line.raw_line), 4):
            c = line.raw_line[j+1]
            if c == ' ':
                continue
            stacks[j//4].append(c)

    for i in range(row_line_idx + 2, len(lines)):
        raw_line = lines[i].raw_line
        amount, fr, to = [int(x) for x in parse('move {} from {} to {}', raw_line)]
        frr = stacks[fr-1][:amount]
        stacks[fr-1] = stacks[fr-1][amount:]
        stacks[to-1] = frr + stacks[to-1]

    print(stacks)
    solution = ''.join([st[0] for st in stacks if len(st) > 0])
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
