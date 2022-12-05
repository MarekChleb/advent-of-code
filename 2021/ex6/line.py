from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        self.timers = [int(num) for num in line.split(",")]
