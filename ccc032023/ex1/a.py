from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

wins = {
    'PP': 'P',
    'SS': 'S',
    'RR': 'R',
    'PR': 'P',
    'RP': 'P',
    'RS': 'R',
    'SR': 'R',
    'SP': 'S',
    'PS': 'S'
}

def get_solution(lines: List[Line]) -> str:
    solution = []
    for line in lines[1:]:
        solution.append(wins[line.raw_line])

    return str('\n'.join(solution))


for i, filename in enumerate(glob('input/*.in')):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename, get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
