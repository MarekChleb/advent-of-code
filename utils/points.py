from typing import Sequence, List


def manhattan_dist(p1: Sequence[int], p2: Sequence[int]) -> int:
    if len(p1) != len(p2):
        raise Exception('bad len')
    return sum(abs(x1 - x2) for x1, x2 in zip(p1, p2))

def get_adjacent_manhattan(p: Sequence[int], d: int) -> List[Sequence[int]]:
    pts = [()]
    for i in range(len(p)):
        next_pts = []
        for possible_val in range(-d, d+1):
            next_pts += [x + (p[i] + possible_val,) for x in pts]
        pts = next_pts
    ball = [x for x in pts if manhattan_dist(x, p) <= d and manhattan_dist(x, p) != 0]
    return ball