from glob import glob
from typing import List

from typing import Sequence, TypeVar, Tuple, Callable, Generic, List, Optional, Type

class LineInterface:
    def __init__(self, line: str):
        self.raw_line = line


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)

LineType = TypeVar('LineType', bound=LineInterface)


def read_lines(line_type: Type[LineType], filename="example.in") -> List[LineType]:
    f = open(filename)
    return [line_type(line.rstrip()) for line in f]


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
        print("-"*20)
        print(line.raw_line)
        r, p, s, y, l = line.raw_line.split(" ")
        r = int(r[:-1])
        p = int(p[:-1])
        s = int(s[:-1])
        y = int(y[:-1])
        l = int(l[:-1])

        cur_c = nums // 2 - 1
        while r >= cur_c and cur_c > 0:
            ss.append('R' * cur_c)
            r -= cur_c
            if cur_c == nums//2 -1:
                if p > 0:
                    ss.append('P')
                    p -= 1
                elif y > 0:
                    ss.append('Y')
                    y -= 1
                else:
                    raise("shouldnt happen 1")
            else: 
                if y > 0:
                    ss.append('Y')
                    y -= 1
                elif p > 0:
                    ss.append('P')
                    p -= 1
                else:
                    raise("shouldnt happen 1.5")

            cur_c = (cur_c + 1) // 2 - 1

        while y >= cur_c and cur_c > 0:
            ss.append('Y' * cur_c)
            y -= cur_c
            if p > 0:
                ss.append('P')
                p -= 1
            elif l > 0:
                ss.append('L')
                l -= 1
            else:
                raise("shouldnt happen 2")

            cur_c = (cur_c + 1) // 2 - 1

        while r > 0 and y > 0:
            ss.append("RY")
            r -= 1
            y -= 1

        while r > 0 and p > 0:
            ss.append("RP")
            r -= 1
            p -= 1
            
        while y > 0 and p > 0:
            ss.append("YP")
            y -= 1
            p -= 1


        ss.append("P" * p)
        ss.append("L" * l)
        ss.append("S" * s)

        print("R", r)
        print("Y", y)
        print("P", p)
        print("L", l)
        print("S", s)

        solution.append(''.join(ss))

    return str('\n'.join(solution))


for i, filename in enumerate(sorted(glob('input/level5_1.in'))):
    input_lines = read_lines(Line, filename)
    s = get_solution(input_lines)
    print(filename)
    print(get_solution(input_lines))
    with open(filename + '.out', "w") as output:
        output.write(str(s))
