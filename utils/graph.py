from dataclasses import dataclass
from heapq import heappush, heappop
from typing import TypeVar, Generic, List, Callable, Dict

KT = TypeVar('KT')
VT = TypeVar('VT')


@dataclass
class Edge(Generic[KT, VT]):
    start: KT
    end: KT
    value: VT

    def __iter__(self):
        yield self.start
        yield self.end
        yield self.value

    def __repr__(self):
        return f"{self.start}--{self.value}-->{self.end}"


@dataclass
class Neighbour(Generic[KT, VT]):
    end: KT
    value: VT

    def __iter__(self):
        yield self.end
        yield self.value


class Graph(Generic[KT, VT]):
    def __init__(self, vertices: List[KT], edges: List[Edge[KT, VT]]):
        self.vertices = vertices
        self.edges = edges
        self.neighbours = {}
        for start, end, value in edges:
            if start not in self.neighbours:
                self.neighbours[start] = []
            self.neighbours[start].append(Neighbour[KT, VT](end, value))

    def dijkstra(self, start: KT, callback: Callable = None) -> Dict[KT, VT]:
        h = [(0, start)]
        visited = set()
        values = {}
        current_shortest = {}
        while len(h) > 0:
            value, current = heappop(h)
            visited.add(current)
            values[current] = value
            for neighbour, edge_value in self.neighbours[current]:
                if neighbour in visited:
                    continue
                if neighbour in current_shortest:
                    if value + edge_value < current_shortest[neighbour]:
                        current_shortest[neighbour] = value + edge_value
                        heappush(h, (value + edge_value, neighbour))
                else:
                    current_shortest[neighbour] = value + edge_value
                    heappush(h, (value + edge_value, neighbour))
            if callback is not None:
                callback()

        return values
