from typing import List

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    counts = {i: 0 for i in range(9)}
    for t in lines[0].timers:
        counts[t] += 1
    solution = 0
    days = 256
    for i in range(days):
        temp_counts = {k: 0 for k in counts}
        for j in range(8):
            temp_counts[j] = counts[j+1]
        temp_counts[8] = counts[0]
        temp_counts[6] += counts[0]
        counts = temp_counts

    solution += sum(counts.values())
    return str(solution)


print(get_solution(input_lines))