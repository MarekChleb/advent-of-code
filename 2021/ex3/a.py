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


def get_solution(lines: List[Line]) -> str:
    popular_bits = [0] * lines[0].length
    for line in lines:
        for i, bit in enumerate(line.bits):
            popular_bits[i] += bit

    lines_count = len(lines)
    epsilon_bits = [1 if bit * 2 > lines_count else 0 for bit in popular_bits]
    gamma_bits = [1 - bit for bit in epsilon_bits]
    solution = get_number(epsilon_bits) * get_number(gamma_bits)
    return str(solution)


print(get_solution(input_lines))