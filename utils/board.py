from typing import Sequence, TypeVar, Tuple, Callable, Generic, List

T = TypeVar('T')
KT = Tuple[int, int]


def default_key_func(x: int, y: int) -> KT:
    return x, y


class Board(Generic[T]):
    def __init__(self, rows: Sequence[Sequence[T]], default_el: T, key_func=default_key_func):
        self._get_key = key_func
        self.board = {}
        self._default_el = default_el
        for y in range(len(rows)):
            row = rows[y]
            for x in range(len(row)):
                self.board[key_func(x, y)] = row[x]

    def set_key_func(self, key_func: Callable[[KT], KT]):
        self._get_key = key_func

    def get(self, k: KT) -> T:
        return self.board[k] if k in self.board else self._default_el

    def set(self, k: KT, v: T):
        self.board[k] = v

    def around(self, k: KT) -> List[T]:
        x, y = k
        neighbours = []
        for dx in [-1, 0, 1]:
            for dy in[-1, 0, 1]:
                if dx == dy == 0:
                    continue
                xx = x + dx
                yy = y + dy
                if (xx, yy) in self.board:
                    neighbours.append((xx, yy))
        return neighbours

    def around_non_diagonal(self, k: KT) -> List[T]:
        x, y = k
        return list(set(self.around(k)) - {(x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)})