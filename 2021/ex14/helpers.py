from typing import Dict, Tuple

from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        if "->" in line:
            self.type = "insertion"
            self.start, self.end = line.split(" -> ")
        else:
            self.type = "template"


class Polymerization:
    def __init__(self, rules: Dict[str, str], start_template: str):
        self.rules = rules
        self.pairs = {}
        for i in range(len(start_template) - 1):
            p = start_template[i:i+2]
            self.pairs[p] = self.pairs.get(p, 0) + 1

    def step(self):
        new_pairs = {}
        for p in self.pairs:
            count = self.pairs[p]
            p1, p2 = self.new_pairs(p, self.rules[p])
            new_pairs[p1] = new_pairs.get(p1, 0) + count
            new_pairs[p2] = new_pairs.get(p2, 0) + count
        self.pairs = new_pairs

    @staticmethod
    def new_pairs(start: str, end: str) -> Tuple[str, str]:
        a, b = start
        return a + end, end + b

    def get_counts(self) -> Dict[str, int]:
        counts = {}
        for p in self.pairs:
            a, b = p
            count = self.pairs[p]
            counts[a] = counts.get(a, 0) + count
            counts[b] = counts.get(b, 0) + count
        return counts