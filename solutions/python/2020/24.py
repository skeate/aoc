from typing import List
from functools import cache
import re

def parse_moves(moves):
    pos = [0, 0, 0]
    for step in re.findall(r'(ne|nw|se|sw|e|w)', moves):
        if step == 'e':
            pos[0] -= 1
            pos[1] -= 1
        elif step == 'se':
            pos[1] -= 1
            pos[2] -= 1
        elif step == 'sw':
            pos[0] += 1
            pos[2] -= 1
        elif step == 'w':
            pos[0] += 1
            pos[1] += 1
        elif step == 'nw':
            pos[1] += 1
            pos[2] += 1
        elif step == 'ne':
            pos[0] -= 1
            pos[2] += 1
        else:
            raise 'wtf'
    return tuple(pos)


@cache
def neighbors(pos):
    return [
        (pos[0] + dx, pos[1] + dy, pos[2] + dz)
        for dx,dy,dz in [
            (-1, -1, 0),
            (0, -1, -1),
            (1, 0, -1),
            (1, 1, 0),
            (0, 1, 1),
            (-1, 0, 1)
        ]
    ]


def day(bts):
    next_bts = set()
    wts = set()
    for bt in bts:
        bnbs = 0
        for nb in neighbors(bt):
            if nb not in bts:
                wts.add(nb)
            else:
                bnbs += 1
        if 0 < bnbs < 3:
            next_bts.add(bt)
    for wt in wts:
        if sum(1 for bnb in neighbors(wt) if bnb in bts) == 2:
            next_bts.add(wt)
    return next_bts


def run(inp: List[str]):
    black_tiles = set()
    for moves in inp:
        pos = parse_moves(moves)
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    print(len(black_tiles))

    for _ in range(100):
        black_tiles = day(black_tiles)
    print(len(black_tiles))
