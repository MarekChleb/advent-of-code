from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines


def snafu_to_num(num_str):
    poww = 0
    ss = 0
    for v in reversed(num_str):
        if v == '-':
            ss -= 5 ** poww
        elif v == '=':
            ss -= 2 * (5 ** poww)
        else:
            ss += int(v) * (5 ** poww)
        poww += 1
    return ss

def num_to_snafu(num):
    snafu = ''
    po = 0
    while num > 0:
        r = num % 5
        if r == 3:
            num += 2 * (5 ** po)
            snafu += '='
            # po -= 1
        elif r == 4:
            num +=  (5 ** po)
            snafu += '-'
            # po -= 1
        else:
            snafu += str(r)

        num //= 5
        # po += 1
    return snafu[::-1]
def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        solution += snafu_to_num(line.raw_line)

    solution = num_to_snafu(solution)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
