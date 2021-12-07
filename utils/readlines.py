from typing import Type, Iterable


class LineInterface:
    def __init__(self, line: str):
        self.raw_line = line


def read_lines(line_type: Type[LineInterface], filename="example.in") -> Iterable[LineInterface]:
    f = open(filename)
    return [line_type(line.rstrip()) for line in f]
