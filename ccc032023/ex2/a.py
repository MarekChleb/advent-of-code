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
    for j, line in enumerate(lines[1:]):
        nl = line.raw_line
        while len(nl) != 1:
            new_line = []
            for i in range(0, len(nl), 2):
                p = nl[i:i+2]
                new_line.append(wins[p])
            nl = ''.join(new_line)
        solution.append(str(j + 2) + ' ' + nl)

    return str('\n'.join(solution))


for i, filename in enumerate(glob('input/*.in')):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename, get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
