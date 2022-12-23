import time
from glob import glob
from typing import List, Type

from helpers import Line
from utils.points import get_adjacent_manhattan
from utils.readlines import read_lines
from utils.union_find import QuickFind, UnionFind, QuickUnion, QuickUnionFind


def get_solution(lines: List[Line], UnionFindClass: Type[UnionFind]) -> str:
    points = set()

    for line in lines:
        p = tuple(int(x) for x in line.raw_line.split(','))
        points.add(p)

    qf = UnionFindClass(points)

    for (i, p) in enumerate(points):
        if i % 1000 == 0 and i > 0:
            print('computing', i)
        for q in get_adjacent_manhattan(p, 3):
            if q in points:
                qf.union(p, q)

    solution = qf.get_unions_count()

    return str(solution)


classes = [QuickUnionFind, QuickFind, QuickUnion]

for cls in classes:
    print(f'Starting {cls} solution')
    start_time = time.time()

    for filename in sorted(glob('input/*.in')):
        input_lines = read_lines(Line, filename)
        print(filename, get_solution(input_lines, cls))

    end_time = time.time() - start_time
    print(f'Took {end_time} seconds\n')


