from dataclasses import dataclass

from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)


values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

lefts = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

rights = {lefts[k]: k for k in lefts}


class BracketChecker2:
    def __init__(self, row: str):
        self.row = row
        self.stacks = {b: 0 for b in lefts.keys()}

    def check(self) -> int:
        value = 0
        for b in self.row:
            if b in lefts:
                self.stacks[b] += 1
            elif b in rights:
                if self.stacks[rights[b]] > 0:
                    self.stacks[rights[b]] -= 1
                else:
                    value += values[b]
                    return value

        return value


closing_values = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


class BracketChecker:
    def __init__(self, row: str):
        self.row = row
        self.stack = []

    def check(self) -> int:
        value = 0
        for b in self.row:
            if b in lefts:
                self.stack.append(b)
            elif b in rights:
                if len(self.stack) == 0 or rights[b] != self.stack[-1]:
                    return values[b]
                self.stack.pop()

        return value

    def closing_value(self) -> int:
        val = 0
        for v in self.stack[::-1]:
            val = val * 5 + closing_values[v]
        return val
