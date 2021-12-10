from typing import List, Union

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line)
input_lines = read_lines(Line, 'input.in')


def get_key(word: Union[str, List[str]]) -> str:
    return ''.join(sorted(word))


def get_solution(lines: List[Line]) -> str:
    solution = 0
    for line in lines:
        poss = {i: set("abcdefg") for i in range(10)}
        for x in line.signal:
            poss[len(x)] &= set(x)

        top = list(poss[3] - poss[2])[0]
        bot = list(poss[6] & poss[5] - set(top))[0]
        mid = list(poss[5] - {top, bot})[0]
        dr = list(poss[6] & poss[2])[0]
        ur = list(poss[2] - {dr})[0]
        ul = list(poss[6] - {top, bot, mid, dr})[0]
        dl = list(set("abcdefg") - {top, bot, mid, dr, ur, ul})[0]

        nums = {
            get_key(list(set("abcdefg") - set(mid))): 0,
            get_key([ur, dr]): 1,
            get_key([top, bot, mid, ur, dl]): 2,
            get_key([top, bot, mid, ur, dr]): 3,
            get_key([ur, ul, mid, dr]): 4,
            get_key([top, bot, mid, ul, dr]): 5,
            get_key(list(set("abcdefg") - set(ur))): 6,
            get_key([top, ur, dr]): 7,
            get_key("abcdefg"): 8,
            get_key(list(set("abcdefg") - set(dl))): 9,
        }

        i = 1000
        for num in line.output:
            solution += nums[get_key(num)] * i
            i //= 10

    return str(solution)


print(get_solution(input_lines))