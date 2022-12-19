from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

rocks = [
    [(3, 0), (4, 0), (5, 0), (6, 0)],
    [(4, 0), (3, 1), (4, 1), (5, 1), (4, 2)],
    [(3, 0), (4, 0), (5, 0), (5, 1), (5, 2)],
    [(3, 0), (3, 1), (3, 2), (3, 3)],
    [(3, 0), (4, 0), (3, 1), (4, 1)]
]

def get_solution(lines: List[Line]) -> str:
    solution = 0
    move = ""
    for line in lines:
        move = line.raw_line
    move_i = 0

    for rock
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
