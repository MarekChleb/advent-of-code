from collections import defaultdict
from typing import List, Tuple, Dict

from line import Line, LavaTubes
from utils.readlines import read_lines

input_lines = read_lines(Line)

input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    rows = [line.row for line in lines]
    tubes = LavaTubes(rows)

    low_points = tubes.get_low_points()

    solution = sum([tubes.get_point_value(p[0], p[1]) + 1 for p in low_points])
    return str(solution)


print(get_solution(input_lines))
