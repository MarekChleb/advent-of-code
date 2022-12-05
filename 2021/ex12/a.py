from glob import glob
from typing import List

from helpers import Line, Caves
from utils.graph import Edge
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0
    vertices = set()
    edges = []
    for line in lines:
        x1, x2 = line
        vertices.add(x1)
        vertices.add(x2)
        edges.append(Edge(x1, x2, 0))
        edges.append(Edge(x2, x1, 0))

    vertices = list(vertices)
    caves = Caves(vertices, edges)
    solution = caves.get_paths_count()
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
