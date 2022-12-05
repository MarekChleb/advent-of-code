from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        signal, output = line.split(" | ")
        self.signal = signal.split(" ")
        self.output = output.split(" ")
