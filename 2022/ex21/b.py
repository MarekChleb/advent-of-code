from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    def f(x):
        # root = 0
        oks = set()
        while len(oks) < len(lines):
            for i, line in enumerate(lines):
                if i not in oks:
                    try:
                        if line.raw_line.startswith('humn'):
                            humn = x
                            oks.add(i)
                            continue
                        if line.raw_line.startswith('root'):
                            exec(line.raw_line.replace('+', '-').replace(':', '='))
                            oks.add(i)
                            continue
                        exec(line.raw_line.replace(':', '='))
                        oks.add(i)
                    except NameError:
                        pass

        return locals().get('root', 7)


    lr = [-3500000000000, 3500000000000]

    while lr[0] < lr[1]:
        l, r = lr
        m = (l + r) // 2
        v = -f(m)
        if v < 0:
            lr[0] = m
        elif v == 0:
            print(m)
            solution = m
            break
        else:
            lr[1] = m
    # solution = f(1)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
