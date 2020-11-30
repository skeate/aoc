import re
import numpy as np
from typing import List

def run(inp: List[str]):
    v = ''.join(inp)

    c = re.compile('\d+')

    def parse(l):
        m = l[6]
        x1, y1, x2, y2 = [int(x) for x in c.findall(l)]
        return (m, x1, y1, x2+1, y2+1)

    v = [parse(l) for l in v.strip().split('\n')]

    g = np.zeros((1000,1000))

    for m, x1, y1, x2, y2 in v:
        if m == 'n':
            g[x1:x2,y1:y2] = 1
        elif m == 'f':
            g[x1:x2,y1:y2] = 0
        else:
            g[x1:x2,y1:y2] = 1 - g[x1:x2,y1:y2]

    print(np.count_nonzero(g == 1))


    g = np.zeros((1000,1000))

    for m, x1, y1, x2, y2 in v:
        if m == 'n':
            g[x1:x2,y1:y2] += 1
        elif m == 'f':
            g[x1:x2,y1:y2] -= 1
            g[g < 0] = 0
        else:
            g[x1:x2,y1:y2] += 2

    print(int(np.sum(g)))
