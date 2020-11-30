import sys
sys.path.append('..')
from typing import List
from grid import Grid

def visit(g, l):
    try:
        return g[l] + 1
    except:
        return 1



def run(inp: List[str]):
    v = ''.join(inp)

    g = Grid(visit, (0,0))
    for d in v:
        if d == '^': g.up()
        elif d == 'v': g.down()
        elif d == '<': g.left()
        elif d == '>': g.right()

    print(len(g.grid))

    santa = Grid(visit, (0,0))
    robo = Grid(visit, (0,0))
    for i in range(len(v)):
        g = santa if i % 2 == 0 else robo
        d = v[i]
        if d == '^': g.up()
        elif d == 'v': g.down()
        elif d == '<': g.left()
        elif d == '>': g.right()

    print(len({**santa.grid, **robo.grid}))
