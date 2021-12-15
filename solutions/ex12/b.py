from glob import glob
from typing import List

from helpers import Line, ChitonsBoard
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    rows = []
    for line in lines:
        row = [int(v) for v in line.raw_line]
        appends = [[(v + i - 1) % 9 + 1 for v in row] for i in range(1, 5)]
        for a in appends:
            row += a
        rows.append(row)

    additional_rows = []
    for i in range(1, 5):
        for row in rows:
            additional_rows.append([(v + i - 1) % 9 + 1 for v in row])

    rows += additional_rows
    board = ChitonsBoard(rows)
    chitons = board.to_graph_non_diagonal()

    shortest_path_values = chitons.dijkstra((0, 0))
    last_point = max(board.board.keys())
    solution = shortest_path_values[last_point]
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
