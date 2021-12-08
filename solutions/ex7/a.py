from typing import List

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    positions = lines[0].positions
    nums = set(positions)
    diffs = {k: sum([abs(k - v) for v in positions]) for k in nums}

    solution = min(diffs.values())
    return str(solution)


print(get_solution(input_lines))