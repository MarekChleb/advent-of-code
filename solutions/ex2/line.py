from utils.readlines import LineInterface


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
        splitted = line.split(" ")
        self.command = splitted[0]
        self.value = int(splitted[1])
