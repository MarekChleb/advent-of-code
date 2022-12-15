import math
from glob import glob
from typing import List

import parse

from helpers import Line
from utils.readlines import read_lines

def dist(p1, p2):
    return int(math.fabs(p1[0] - p2[0]) + math.fabs(p1[1] - p2[1]))

def neighs(p, d, yy):
    x, y = p
    a = []
    dyy = int(math.fabs(y - yy))
    dxx = d - dyy
    for dx in range(-dxx, dxx + 1):
        if dx == 0 and yy == y:
            continue
        a.append((x + dx, yy))

    return a
def get_solution(lines: List[Line]) -> str:
    solution = 0
    sens = set()
    beacons = set()
    imposs = set()
    for line in lines:
        sx, sy, bx, by = parse.parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', line.raw_line)
        sens.add((sx, sy))
        beacons.add((bx, by))

        for ne in neighs((sx, sy), dist((sx, sy), (bx, by)), 2000000):
            x, y = ne
            if y == 2000000:
                imposs.add((x, y))


    solution = len(imposs - sens - beacons)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
