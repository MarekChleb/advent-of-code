from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        self.bits = [int(c) for c in line]
        self.length = len(self.bits)