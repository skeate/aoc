from typing import List

def run(inp: List[str]):
    vs = [int(x) for x in inp]
    print(sum(vs))

    freq = 0
    visited = set()
    i = 0
    while freq not in visited:
        visited.add(freq)
        freq += vs[i]
        i = (i + 1) % len(vs)
    print(freq)
