from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        start_pair, next_pair = line.split(" -> ")
        self.x1, self.y1 = [int(num) for num in start_pair.split(",")]
        self.x2, self.y2 = [int(num) for num in next_pair.split(",")]
