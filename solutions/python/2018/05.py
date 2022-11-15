import itertools
from typing import List

def react(poly):
    i = 0
    while i < len(poly) - 1:
        a, b = poly[i], poly[i + 1]
        if a.lower() == b.lower() and a != b:
            poly = poly.replace(a + b, '')
            i -= 2
        i += 1
    return len(poly)

def run(inp: List[str]):
    poly = inp[0].strip()

    print(react(poly))

    print(min([react(p) for p in [poly.replace(c, '').replace(c.lower(), '') for c in set(poly.upper())]]))
