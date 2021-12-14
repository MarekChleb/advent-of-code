from typing import List, Set

from utils.board import Board, Coordinates
from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)


class Octopuses(Board[int]):
    def __init__(self, rows: List[List[int]]):
        super().__init__(rows, default_el=0)

    def get_pop_candidates(self) -> Set[Coordinates]:
        return set(c for c in self.board if self.get(c) > 9)

    def inc(self, k):
        self.set(k, self.get(k) + 1)

    def add_all(self):
        for k in self.board:
            self.inc(k)

    def flash(self) -> int:
        self.add_all()
        popped = set()
        popped_candidates = self.get_pop_candidates()
        while len(popped_candidates) > 0:
            for c in popped_candidates:
                arounds = set(self.around(c)) - popped
                for neighbour in arounds:
                    self.inc(neighbour)

            popped |= popped_candidates
            popped_candidates = self.get_pop_candidates() - popped

        flashed = 0
        popped = [c for c in self.board if self.get(c) > 9]
        for p in popped:
            self.set(p, 0)
            flashed += 1

        return flashed
