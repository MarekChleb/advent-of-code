from utils.readlines import LineInterface
from parse import parse


class Line(LineInterface):
    def __init__(self, line: str):
        x, y, z, r = parse("pos=<{},{},{}>, r={}", line)
        self.x, self.y, self.z, self.r = int(x), int(y), int(z), int(r)
        # print(self.x, self.y, self.z, self.r)
        super().__init__(line)
