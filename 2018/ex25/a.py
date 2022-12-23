import time
from glob import glob
from typing import List

from helpers import Line
from utils.points import get_adjacent_manhattan
from utils.readlines import read_lines


def get_solution(lines: List[Line]) -> str:
    solution = 0

    points = set()
    for line in lines:
        p = tuple(int(x) for x in line.raw_line.split(','))
        points.add(p)

    adj = {}
    for p in points:
        adj[p] = [x for x in get_adjacent_manhattan(p, 3) if x in points]

    visited = set()
    for p in points:
        if p in visited:
            continue

        solution += 1
        visited.add(p)
        q = [p]
        while len(q) > 0:
            pp = q.pop()
            for nei in adj[pp]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)



    # print(father)


    return str(solution)


print(f'Starting solution')
start_time = time.time()

for filename in sorted(glob('input/*.in')):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))

end_time = time.time() - start_time
print(f'Took {end_time} seconds\n')
