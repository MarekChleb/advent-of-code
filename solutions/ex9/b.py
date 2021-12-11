import math
from typing import List

from line import Line, LavaTubes
from utils.readlines import read_lines

input_lines = read_lines(Line)


input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    rows = [line.row for line in lines]
    tubes = LavaTubes(rows)

    low_points = tubes.get_low_points()
    basin_values = sorted([tubes.get_basin_count(p) for p in low_points])
    basin_values = basin_values[-3:]

    solution = math.prod(basin_values)
    return str(solution)


print(get_solution(input_lines))
