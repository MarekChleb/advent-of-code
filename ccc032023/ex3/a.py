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
        ss = []
        r, p, s = line.raw_line.split(" ")
        r = int(r[:-1])
        p = int(p[:-1])
        s = int(s[:-1])

        while r > 2:
            ss.append('RRRP')
            r -= 3
            p -= 1

        if r == 2:
            if s > 1:
                ss.append('RPRS')
                s-= 1
                r -= 2
                p-=1
            else:
                ss.append('RPRP')
                r -= 2
                p -= 2
        elif r == 1:
            ss.append('RP')
            p -= 1
            r -= 1

        ss.append('P' * p)
        ss.append('S' * s)

        solution.append(''.join(ss))

    return str('\n'.join(solution))


for i, filename in enumerate(sorted(glob('input/*.in'))):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename, get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
