from abc import ABC
from typing import Hashable, Iterable


class UnionFind(ABC):
    def __init__(self, points: Iterable[Hashable]):
        pass

    def find(self, p: Hashable) -> Hashable:
        pass

    def union(self, p: Hashable, q: Hashable):
        pass

    def is_connected(self, p: Hashable, q: Hashable) -> bool:
        return self.find(p) == self.find(q)

    def get_unions_count(self) -> int:
        pass

class QuickFind(UnionFind):
    def __init__(self, points: Iterable[Hashable]):
        super().__init__(points)
        self._parents = { p: p for p in points }

    def find(self, p: Hashable) -> Hashable:
        return self._parents[p]

    def union(self, p: Hashable, q: Hashable):
        root_p, root_q = self._parents[p], self._parents[q]
        for node in self._parents:
            if self._parents[node] == root_p:
                self._parents[node] = root_q

    def is_connected(self, p: Hashable, q: Hashable) -> bool:
        return self._parents[p] == self._parents[q]

    def get_unions_count(self) -> int:
        return len(set(self.find(p) for p in self._parents))


class QuickUnion(UnionFind):
    def __init__(self, points: Iterable[Hashable]):
        super().__init__(points)
        self._parents = { p: p for p in points }

    def find(self, p: Hashable) -> Hashable:
        while p != self._parents[p]:
            p = self._parents[p]
        return p

    def union(self, p: Hashable, q: Hashable):
        root_p, root_q = self.find(p), self.find(q)
        self._parents[root_p] = root_q

    def is_connected(self, p: Hashable, q: Hashable) -> bool:
        return self.find(p) == self.find(q)

    def get_unions_count(self) -> int:
        return len(set(self.find(p) for p in self._parents))

class QuickUnionFind(UnionFind):
    def __init__(self, points: Iterable[Hashable]):
        super().__init__(points)
        self._parents = { p: p for p in points }
        self._ranks = { p: 1 for p in points }

    def find(self, p: Hashable) -> Hashable:
        while p != self._parents[p]:
            self._parents[p] = self._parents[self._parents[p]]
            p = self._parents[p]
        return p


    def union(self, p: Hashable, q: Hashable):
        root_u, root_v = self.find(p), self.find(q)
        if root_u == root_v:
            return
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1

    def is_connected(self, p: Hashable, q: Hashable) -> bool:
        return self.find(p) == self.find(q)


    def get_unions_count(self) -> int:
        return len(set(self.find(p) for p in self._parents))