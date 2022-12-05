from typing import Any, List

from utils.graph import Graph, Edge
from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        self.x1, self.x2 = line.split('-')

    def __iter__(self):
        yield self.x1
        yield self.x2


class Caves(Graph[str, Any]):
    def __init__(self, vertices: List[str], edges: List[Edge[str, Any]]):
        super().__init__(vertices, edges)

    @staticmethod
    def is_small(key: str) -> bool:
        return not key.isupper()

    def get_paths_count(self, limit: int = 1):
        start_point = 'start'
        end_point = 'end'

        h = [(start_point, set(), False)]
        paths = []
        paths_count = 0
        while len(h) > 0:
            p, visited, used_small = h[0]
            h = h[1:]
            if p == end_point:
                paths_count += 1
                continue
            if self.is_small(p):
                visited.add(p)
            for neighbour, _ in self.neighbours[p]:
                if neighbour == start_point:
                    continue
                if self.is_small(neighbour) and not used_small and neighbour in visited:
                    new_visited = set(visited)
                    h += [(neighbour, new_visited, True)]
                elif neighbour not in visited:
                    new_visited = set(visited)
                    h += [(neighbour, new_visited, used_small)]

        return paths_count
