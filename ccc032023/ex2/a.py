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
