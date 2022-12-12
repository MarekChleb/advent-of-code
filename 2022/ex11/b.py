import math
from glob import glob
from typing import List

import parse

from helpers import Line
from utils.readlines import read_lines

parse_monke = """Monkey {}:
  Starting items: {}
  Operation: new = {}
  Test: divisible by {}
    If true: throw to monkey {}
    If false: throw to monkey {}"""

class Monke:
    def __init__(self, monke_id, items, op, divisible_by, true_monkey, false_monkey):
        self.monke_id = monke_id
        self.items = [int(x) for x in items.split(', ')]
        self.op = op
        self.divisible_by = int(divisible_by)
        self.true_monkey = int(true_monkey)
        self.false_monkey = int(false_monkey)
        self.inspected = 0

    def evaluate_item(self, old):
        old = old
        new = eval(self.op) % 9699690
        self.inspected += 1
        if new % self.divisible_by == 0:
            return self.true_monkey, new
        return self.false_monkey, new
    def throw(self):
        throws = [self.evaluate_item(item) for item in self.items]
        self.items = []
        return throws

    def append_item(self, val):
        self.items.append(val)

    def __repr__(self):
        return f'Monkey {self.monke_id} inspected items {self.inspected} times.'
def get_solution(lines: List[Line]) -> str:
    solution = 0
    i = 0
    monkes = []
    print(len(lines))

    for i in range(0, len(lines), 7):
        monke_str = '\n'.join([line.raw_line for line in lines[i:i+6]])
        monke_id, items, op, divisible_by, true_monkey, false_monkey = parse.parse(parse_monke, monke_str)
        monke = Monke(monke_id, items, op, divisible_by, true_monkey, false_monkey)

        monkes.append(monke)

    print(math.prod([x.divisible_by for x in monkes]))
    for i in range(10000):
        for monke in monkes:
            throws = monke.throw()
            for next_monke, val in throws:
                monkes[next_monke].append_item(val)

        if i in [0, 19, 999, 1999]:
            print(monkes)
        # print(monkes)

    print([m.inspected for m in monkes])
    monkes.sort(key=lambda x: x.inspected)
    solution = monkes[-1].inspected * monkes[-2].inspected

    return str(solution)


for filename in glob('input/*.in'):
    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
