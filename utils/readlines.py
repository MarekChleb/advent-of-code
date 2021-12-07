from typing import Type, List, TypeVar


class LineInterface:
    def __init__(self, line: str):
        self.raw_line = line


LineType = TypeVar('LineType', bound=LineInterface)


def read_lines(line_type: Type[LineType], filename="example.in") -> List[LineType]:
    f = open(filename)
    return [line_type(line.rstrip()) for line in f]
