from typing import Sequence, TypeVar, Tuple, Callable, Generic, List, Optional

from utils.graph import Graph, Edge

T = TypeVar('T')
Coordinates = Tuple[int, int]


def default_key_func(c: Coordinates) -> Coordinates:
    return c


class Board(Generic[T]):
    def __init__(self, rows: Sequence[Sequence[T]], default_el: T, key_func=default_key_func):
        self._get_key = key_func
        self.board = {}
        self._default_el = default_el
        for y in range(len(rows)):
            row = rows[y]
            for x in range(len(row)):
                self.board[key_func((x, y))] = row[x]

    def set_key_func(self, key_func: Callable[[Coordinates], Coordinates]):
        self._get_key = key_func

    def get(self, k: Coordinates) -> T:
        key = self._get_key(k)
        return self.board[key] if key in self.board else self._default_el

    def set(self, k: Coordinates, v: T):
        self.board[self._get_key(k)] = v

    def around(self, k: Coordinates) -> List[Coordinates]:
        x, y = k
        neighbours = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                xx = x + dx
                yy = y + dy
                k = self._get_key((xx, yy))
                if k in self.board:
                    neighbours.append(k)
        return neighbours

    def around_non_diagonal(self, k: Coordinates) -> List[Coordinates]:
        x, y = k
        neighbours = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x + dx
            yy = y + dy
            k = self._get_key((xx, yy))
            if k in self.board:
                neighbours.append(k)
        return neighbours

    def __repr__(self) -> str:
        x_min, y_min = min(self.board.keys())
        x_max, y_max = max(self.board.keys())
        pretty_printed = ''
        for y in range(y_max, y_min - 1, -1):
            for x in range(x_min, x_max + 1):
                pretty_printed += str(self.get((x, y)))
            pretty_printed += '\n'
        return pretty_printed

    def __len__(self) -> int:
        return len(self.board)

    def to_graph_non_diagonal(self, get_func: Optional[Callable[[Coordinates], T]] = None) -> Graph[Coordinates, T]:
        vertices = list(self.board.keys())
        if get_func is None:
            get_func = self.get
        edges = []
        for k in self.board:
            for neighbour in self.around_non_diagonal(k):
                edges.append(Edge(k, neighbour, get_func(neighbour)))

        return Graph[Coordinates, T](vertices, edges)

    def move(self, start: Coordinates, end: Coordinates):
        start_val = self.get(start)
        self.set(end, start_val)
        self.set(start, self._default_el)
