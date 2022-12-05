from glob import glob
from typing import List

from helpers import Line, Polymerization
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    start_template = ""
    rules = {}
    for line in lines:
        if line.type == "template" and line.raw_line != "":
            start_template = line.raw_line
        elif line.type == "insertion":
            rules[line.start] = line.end

    start_char, end_char = start_template[0], start_template[-1]
    poly = Polymerization(rules, start_template)
    for i in range(10):
        poly.step()

    counts = poly.get_counts()
    counts[start_char] += 1
    counts[end_char] += 1
    max_key = max(counts, key=counts.get)
    min_key = min(counts, key=counts.get)
    solution = (counts[max_key] - counts[min_key]) / 2
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
