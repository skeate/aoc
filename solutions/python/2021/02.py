from typing import List
import functools

def parse(s: str):
    d, a = s.split(' ')
    a = int(a)
    if (d == 'forward'): return (a,0)
    # if (d == 'backward'): return (-a,0)
    if (d == 'up'): return (0,-a)
    if (d == 'down'): return (0,a)

def run(inp: List[str]):
    deltas = [parse(x) for x in inp]
    final_pos = functools.reduce(lambda a,b: (a[0] + b[0], a[1] + b[1]), deltas)
    print(final_pos[0] * final_pos[1])

    final_pos_2 = functools.reduce(
        lambda a,b: (a[0] + b[0], a[1] + b[1], a[2] + b[0] * (a[1] + b[1])),
        [(d[0], d[1], 0) for d in deltas]
    )
    print(final_pos_2[0] * final_pos_2[2])
