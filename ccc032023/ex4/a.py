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
    _, nums = lines[0].raw_line.split(" ")
    nums = int(nums)
    for line in lines[1:]:
        ss = []
        r, p, s = line.raw_line.split(" ")
        r = int(r[:-1])
        p = int(p[:-1])
        s = int(s[:-1])

        cur_c = nums // 2 - 1
        while r >= cur_c and cur_c > 0:
            ss.append('R' * cur_c + 'P')
            r -= cur_c
            p -= 1
            cur_c = (cur_c + 1) // 2 - 1

        if r > 0:
            ss.append('P' + 'R' * r + 'S' * (s-1) + 'P' * (p-1) + 'S')
        else:
            ss.append('R' * r + 'P' * p + 'S' * s)

        solution.append(''.join(ss))

    return str('\n'.join(solution))


for i, filename in enumerate(sorted(glob('input/*.in'))):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename, get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
