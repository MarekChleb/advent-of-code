from glob import glob
from typing import List

from helpers import Line
from utils.readlines import read_lines

vals = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6,
    "rock": 1,
    "paper": 2,
    "scissor": 3
}

types = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
    "X": "rock",
    "Y": "paper",
    "Z": "scissor",
}

loses = {
    "rock": "paper",
    "paper": "scissor",
    "scissor": "rock"
}

wins = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}


def won(f, s):
    t1, t2 = types[f], types[s]

    if s == "X":
        t2 = wins[t1]

    if s == "Y":
        t2 = t1

    if s == "Z":
        t2 = loses[t1]

    if t1 == t2:
        return 3
    if t1 == "rock":
        if t2 == "paper":
            return 6
        return 0
    if t1 == "paper":
        return 6 if t2 == "scissor" else 0
    return 6 if t2 == "rock" else 0




def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        f, s = line.raw_line.split(" ")
        vv = vals[wins[types[f]]] if s == "X" else vals[types[f]]
        if s == "Z":
            vv = vals[loses[types[f]]]
        solution += vv + won(f, s)
        # print(vv, won(f, s))
    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
