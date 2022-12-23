import random

from utils.points import get_adjacent_manhattan

points = get_adjacent_manhattan((0, 0, 0, 0), 22)
random.seed(7)

def gen(name, k):
    with open(f'input/{name}', 'w') as f:
        x_points = random.choices(points, k=k)
        for p in x_points:
            f.write(f'{",".join(str(c) for c in p)}\n')

gen('x_large_input.in', 10000)
gen('y_large_input.in', 20000)
