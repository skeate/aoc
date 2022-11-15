from typing import List
import itertools
from functools import cache
import operator

def add_tuples(a, b):
    return tuple(map(operator.add, a, b))

@cache
def neighbors(p, d=3):
    return set(add_tuples(p, dp) for dp in itertools.product(range(-1, 2), repeat=d))

def conway(grid, d=3):
    new_grid = set()
    all_neighbors = set.union(*[neighbors(p, d) for p in grid])
    for n in all_neighbors:
        active_neighbors = [nn for nn in neighbors(n, d) if nn in grid and nn != n]
        if len(active_neighbors) == 3 or len(active_neighbors) == 2 and n in grid:
            new_grid.add(n)
    return new_grid

def solve(inp, d):
    grid = set()
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            if c == '#':
                grid.add((x, y) + (d-2) * (0,))

    for _ in range(6):
        grid = conway(grid, d)

    print(len(grid))

def run(inp: List[str]):
    solve(inp, 3)
    solve(inp, 4)
