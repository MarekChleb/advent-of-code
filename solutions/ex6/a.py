from typing import List

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    timers = lines[0].timers
    for i in range(80):
        timers = [t - 1 for t in timers]
        apps = len([t for t in timers if t == -1])
        timers = [6 if t == -1 else t for t in timers] + [8] * apps

    solution = len(timers)
    return str(solution)


print(get_solution(input_lines))