from typing import List

from line import Line
from utils.readlines import read_lines

lines = read_lines(Line, 'input.in')


def get_solution(_lines: List[Line]) -> str:
    depth = 0
    horizontal = 0
    aim = 0
    for l in _lines:
        if l.command == "forward":
            horizontal += l.value
            depth += aim * l.value
        else:
            aim += l.value if l.command == "down" else -l.value
    solution = depth * horizontal
    return str(solution)


print(get_solution(lines))