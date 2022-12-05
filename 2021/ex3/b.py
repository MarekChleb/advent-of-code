from collections import Counter
from typing import List

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line, 'input.in')


def get_number(bits: List[int]) -> int:
    val = 0
    pot = 0
    for bit in bits[::-1]:
        val += bit * (2 ** pot)
        pot += 1
    return val


def get_popular_bit(lines: List[Line], idx: int) -> int:
    c = Counter([line.bits[idx] for line in lines])
    zeroes, ones = c.get(0, 0), c.get(1, 0)
    if zeroes > ones:
        return 0
    return 1


def filter_lines(lines: List[Line], idx: int, popular_bit: int, default_bit: int) -> List[Line]:
    if default_bit == 1:
        return [line for line in lines if line.bits[idx] == popular_bit]
    return [line for line in lines if line.bits[idx] == 1 - popular_bit]


def get_rating_number(lines: List[Line], bit: int) -> List[int]:
    i = 0
    while len(lines) > 1:
        popular_bit = get_popular_bit(lines, i)
        lines = filter_lines(lines, i, popular_bit, bit)
        i += 1
    return lines[0].bits


def get_solution(lines: List[Line]) -> str:
    oxygen_rating_bits = get_rating_number(lines, 1)
    co2_rating_bits = get_rating_number(lines, 0)
    solution = get_number(oxygen_rating_bits) * get_number(co2_rating_bits)
    return str(solution)


print(get_solution(input_lines))