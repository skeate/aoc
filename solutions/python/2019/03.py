import sys
sys.path.append('..')
from typing import List
from grid import Grid

def run(inp: List[str]):
    v = [x.split(',') for x in inp]

    steps = 0
    pn = 0
    def m(g,c):
        nonlocal steps
        steps += 1
        if c in g:
            if g[c][0] == pn: return g[c]
            return (2, steps + g[c][1])
        return (pn, steps)
    g = Grid(m)
    for pn, path in enumerate(v):
        steps=0
        g.loc = (0,0)
        for step in path:
            d = int(step[1:])
            if step[0] == 'R': g.slide_x(d)
            if step[0] == 'L': g.slide_x(-d)
            if step[0] == 'U': g.slide_y(d)
            if step[0] == 'D': g.slide_y(-d)

    intersections = { c: k for c,k in g.grid.items() if k[0] == 2 }
    ds = [sum(abs(c) for c in x) for x in intersections.keys()]
    print(min(ds))

    tss = [ts[1] for ts in intersections.values()]
    print(min(tss))
