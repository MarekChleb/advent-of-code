from typing import List

from line import Line
from utils.readlines import read_lines

input_lines = read_lines(Line)


input_lines = read_lines(Line, 'input.in')


class Ocean:
    marked = {}

    def cross_line(self, line: Line):
        if line.x1 == line.x2:
            lower, higher = min(line.y1, line.y2), max(line.y1, line.y2)
            for y in range(lower, higher + 1):
                key = (line.x1, y)
                self.marked[key] = self.marked.get(key, 0) + 1
        elif line.y1 == line.y2:
            lower, higher = min(line.x1, line.x2), max(line.x1, line.x2)
            for x in range(lower, higher + 1):
                key = (x, line.y1)
                self.marked[key] = self.marked.get(key, 0) + 1
        elif abs(line.x1 - line.x2) == abs(line.y1 - line.y2):
            dx = (line.x1 - line.x2) / abs(line.x1 - line.x2)
            dy = (line.y1 - line.y2) / abs(line.y1 - line.y2)

            for i in range(abs(line.x1 - line.x2) + 1):
                key = (line.x2 + i * dx, line.y2 + i * dy)
                self.marked[key] = self.marked.get(key, 0) + 1

    def count_overlapping_points(self) -> int:
        return sum([1 for p in self.marked if self.marked[p] > 1])


def get_solution(lines: List[Line]) -> str:
    ocean = Ocean()
    for line in lines:
        ocean.cross_line(line)
    solution = ocean.count_overlapping_points()
    return str(solution)


print(get_solution(input_lines))
