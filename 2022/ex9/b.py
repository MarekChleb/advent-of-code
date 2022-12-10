import math
from glob import glob
from typing import List

from helpers import Line
from utils.board import Board
from utils.readlines import read_lines



def dist(t1, t2):
    return int(max(math.fabs(t1[0] - t2[0]), math.fabs(t1[1] - t2[1])))


def dist2(t1, t2):
    return int(math.fabs(t1[0] - t2[0]) + math.fabs(t1[1] - t2[1]))

def adj(p):
    x, y = p
    return [(x+1, y + 1),(x, y + 1),(x-1, y + 1),(x+1, y),(x-1, y),(x+1, y - 1),(x, y - 1),(x-1, y - 1)]
def get_solution(lines: List[Line]) -> str:
    solution = 0
    tails = [(0, 0) for x in range(10)]
    visited = set()
    visited.add(tails[-1])
    for line in lines:
        dx, dy = 0, 0
        dirr, amount = line.raw_line.split(' ')
        amount = int(amount)

        if dirr == 'R':
            dx = 1
            dy = 0
        elif dirr == 'L':
            dx = -1
            dy = 0
        elif dirr == 'U':
            dx = 0
            dy = 1
        elif dirr == 'D':
            dx = 0
            dy = -1

        for i in range(amount):
            prev = tails[0]
            tails[0] = (tails[0][0] + dx, tails[0][1] + dy)
            moved = (dx, dy)
            for tt in range(1, 10):
                st = tails[tt-1]
                tail = tails[tt]
                tx, ty = tail

                if dist(st, tail) > 1:
                    ddx, ddy = moved
                    if tx == st[0]:
                        tails[tt] = (tx, ty + ddy)
                        moved = (0, ddy)
                    elif ty == st[1]:
                        tails[tt] = (tx + ddx, ty)
                        moved = (ddx, 0)
                    elif int(math.fabs(ddx) + math.fabs(ddy)) == 2:
                            tails[tt] = (tx + ddx, ty + ddy)
                    else:
                        moved = (prev[0] - tx, prev[1] - ty)
                        tails[tt] = prev
                else:
                    break
                prev = tail
            # if dist(tails[-2], tails[-1]):
            #     tails[-1] = prev

            visited.add(tails[-1])
        b = Board[str]([['.'] * 29] * 21, default_el='.', key_func=lambda ttt: (ttt[0] - 14, ttt[1] - 11))
        b.set_key_func(lambda ttt: ttt)
        for it, t in enumerate(tails):
            # b.set((t[1], t[0]), str(it))
            b.set(t, str(it))

        print(b, tails)
        print(tails[-1])

    solution = len(visited)
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
