from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

def neighs(x, y, z):
    return [(x + 1, y, z),(x - 1, y, z),(x, y + 1, z),(x, y - 1, z),(x, y, z + 1),(x, y, z - 1)]

def neighs2(x, y, z):
    ne = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == dy == dz == 0:
                    continue
                ne.append((x + dx, y + dy, z + dz))
    return ne

def get_solution(lines: List[Line]) -> str:
    solution = 0
    ne = {}
    for line in lines:
        x, y, z = [int(nn) for nn in line.raw_line.split(',')]
        ne[(x, y, z)] = []
        solution += 6
        for ni in neighs(x, y, z):
            if ni in ne:
                ne[ni].append((x, y, z))
                ne[(x, y, z)].append(ni)
                solution -= 2

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
