from typing import List

from line import Line, parse_bingo, BingoGame
from utils.readlines import read_lines

input_lines = read_lines(Line, 'input.in')


def get_solution(lines: List[Line]) -> str:
    nums = lines[0].raw_line.split(",")
    nums = [int(num) for num in nums]

    lines = lines[2:]
    i = 0
    bingos = []
    while i < len(lines):
        bingos.append(parse_bingo(lines))
        lines = lines[6:]

    game = BingoGame(bingos)

    i = 0
    last_num = nums[0]
    while not game.check_bingos():
        game.mark(nums[i])
        last_num = nums[i]
        i += 1

    winning_bingo = game.get_winning_bingo()
    sum_unmarked = sum(winning_bingo.get_unmarked_numbers())

    solution = last_num * sum_unmarked
    return str(solution)


print(get_solution(input_lines))