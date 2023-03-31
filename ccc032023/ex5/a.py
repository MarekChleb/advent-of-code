from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

wins = {
    'PP': 'P',
    'RR': 'R',
    'SS': 'S',
    'LL': 'L',
    'YY': 'Y',
    'PR': 'P',
    'RP': 'P',
    'PY': 'P',
    'YP': 'P',
    'RS': 'R',
    'SR': 'R',
    'RL': 'R',
    'LR': 'R',
    'SP': 'S',
    'PS': 'S',
    'SL': 'S',
    'LS': 'S',
    'LP': 'L',
    'PL': 'L',
    'LY': 'L',
    'YL': 'L',
    'YS': 'Y',
    'SY': 'Y',
    'YR': 'Y',
    'RY': 'Y'
}


# def generate_tournament(winner, r, p, s, y, l) -> bool:
#     generate_tournament(winner, r, p, s - 1, )


def get_solution(lines: List[Line]) -> str:
    solution = []
    _, nums = lines[0].raw_line.split(" ")
    nums = int(nums)
    for line in lines[1:]:
        ss = []
        r, p, s, y, l = line.raw_line.split(" ")
        r = int(r[:-1])
        p = int(p[:-1])
        s = int(s[:-1])
        y = int(y[:-1])
        l = int(l[:-1])

        cur_c = nums // 2 - 1
        while r >= cur_c and cur_c > 0:
            ss.append('R' * cur_c + 'P')
            r -= cur_c
            p -= 1
            cur_c = (cur_c + 1) // 2 - 1

        while y >= cur_c and cur_c > 0:
            ss.append('Y' * cur_c + 'L')
            y -= cur_c
            l -= 1
            cur_c = (cur_c + 1) // 2 - 1
        # ss.append('P' + 'R' * r + 'S' * (s - 1) + 'P' * (p - 1) + 'S')

        if p <= 1:
            ss.append('R' * r + 'Y' * y + 'P' * p + 'L' * l + 'S' * s)
        else:
            ss.append('P' + 'R' * r + 'Y' * y + 'P' * (p - 1) + 'L' * l + 'S' * s)



        solution.append(''.join(ss))

    return str('\n'.join(solution))


for i, filename in enumerate(sorted(glob('input/*.in'))):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename)
    print(get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
