from typing import List
import math

def count_trees(m, dx, dy):
    x = 0
    y = 0
    trees = 0
    while y < len(m):
        trees += 1 if m[y][x] == '#' else 0
        x = (x + dx) % len(m[0])
        y += dy
    return trees

def count_trees2(m, dx, dy):
    x = 0
    y = 0
    trees = 0
    visited = 0
    while visited < len(m):
        trees += 1 if m[y][x] == '#' else 0
        x = (x + dx) % len(m[0])
        y = (y + dy) % len(m)
        visited += 1
    return trees

def run(inp: List[str]):
    inp = [list(x.strip()) for x in inp]
    slopes = [
        (1, 1),
        (3, 1), # part 1 slope
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees = [count_trees(inp, *x) for x in slopes]
    print(trees[1])
    print(math.prod(trees))

    print('min trees:', min([(count_trees2(inp, x, y), (x, y)) for x in range(31) for y in range(1, len(inp))]))
