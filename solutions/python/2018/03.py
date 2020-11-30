import re
import sys
sys.path.append('..')
from typing import List
from grid import Grid

def fill(g: Grid, x, y, w, h, c):
    for a in range(x, x+w):
        for b in range(y, y+h):
            if (a,b) in g.grid:
                g.grid[(a,b)] |= set([c])
            else:
                g.grid[(a,b)] = set([c])

def run(inp: List[str]):
    cloth = Grid()
    
    claims = set([])
    for claim in inp:
        m = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)
        if m is not None:
            fill(cloth, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), m.group(1))
            claims.add(m.group(1))

    print(len([v for v in cloth.grid.values() if v is not None and len(v) > 1]))

    for claim in claims:
        if any(claim in x and len(x) > 1 for x in cloth.grid.values() if x is not None):
            continue
        print(claim)
        exit()
    print('no intact claim found')
