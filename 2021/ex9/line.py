from collections import defaultdict
from typing import List, Dict, Tuple

from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        self.row = [int(num) for num in line]


Point = Tuple[int, int]


class LavaTubes:
    area: Dict[Point, int] = defaultdict(lambda: 10)

    def __init__(self, rows: List[List[int]]):
        for y in range(len(rows)):
            row = rows[y]
            for x in range(len(row)):
                self.area[(x, y)] = row[x]

    def is_low_point(self, x: int, y: int) -> bool:
        val = self.area[(x, y)]
        return val < self.area[(x + 1, y)] and val < self.area[(x - 1, y)] and val < self.area[(x, y + 1)] and val < \
               self.area[(x, y - 1)]

    def get_low_points(self) -> List[Point]:
        keys = list(self.area.keys())
        return [point for point in keys if self.is_low_point(point[0], point[1])]

    def get_point_value(self, x: int, y: int) -> int:
        return self.area[(x, y)]

    @staticmethod
    def get_adjacent(p: Point) -> List[Point]:
        x, y = p
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def get_basin_count(self, start: Point) -> int:
        q = [start]
        visited = set()
        count = 0
        while len(q) > 0:
            p = q[0]
            q = q[1:]
            if p in visited:
                continue
            count += 1
            visited.add(p)
            v = self.area[p]
            q += [adj for adj in self.get_adjacent(p) if v < self.area[adj] < 9]
        return count
