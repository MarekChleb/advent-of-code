from typing import List, Sequence

from utils.board import Board
from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)


class ChitonsBoard(Board[int]):
    def __init__(self, rows: Sequence[Sequence[int]]):
        super().__init__(rows, -1)
