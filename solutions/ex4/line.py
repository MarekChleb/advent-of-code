from dataclasses import dataclass
from typing import List

from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)


@dataclass
class Bingo:
    nums: List[List[int]]
    marked = set()

    def mark(self, num: int):
        self.marked.add(num)

    def is_bingo(self) -> bool:
        return self.check_rows() or self.check_columns()

    def check_rows(self) -> bool:
        for row in self.nums:
            not_marked = set(row) - self.marked
            if len(not_marked) == 0:
                return True
        return False

    def check_columns(self) -> bool:
        for i in range(5):
            column = [row[i] for row in self.nums]
            not_marked = set(column) - self.marked
            if len(not_marked) == 0:
                return True
        return False

    def get_unmarked_numbers(self) -> List[int]:
        all_nums = set()
        for row in self.nums:
            all_nums |= set(row)

        unmarked_set = all_nums - self.marked
        return list(unmarked_set)


@dataclass
class BingoGame:
    bingos: List[Bingo]
    marked = set()

    def mark(self, num: int):
        self.marked.add(num)
        for bingo in self.bingos:
            bingo.mark(num)

    def check_bingos(self) -> bool:
        for bingo in self.bingos:
            if bingo.is_bingo():
                return True
        return False

    def get_winning_bingo(self) -> Bingo:
        for bingo in self.bingos:
            if bingo.is_bingo():
                return bingo
        return Bingo([])

    def purge_won_bingos(self) -> List[Bingo]:
        self.bingos = [bingo for bingo in self.bingos if not bingo.is_bingo()]
        return self.bingos


def parse_bingo(lines: List[Line]) -> Bingo:
    nums = []
    for i in range(5):
        nums.append([int(num) for num in lines[i].raw_line.split(" ") if num != ''])

    return Bingo(nums)