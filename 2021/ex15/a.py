from glob import glob
from typing import List

from helpers import Line, ChitonsBoard
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    rows = []
    for line in lines:
        row = [int(v) for v in line.raw_line]
        rows.append(row)

    board = ChitonsBoard(rows)
    chitons = board.to_graph_non_diagonal()

    shortest_path_values = chitons.dijkstra((0, 0))
    last_point = max(board.board.keys())
    solution = shortest_path_values[last_point]
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
