from typing import List

def run(inp: List[str]):
    v = [x.strip() for x in inp]

    dists = {}

    left = set()

    for a,to,b,eq,d in [x.split(' ') for x in v]:
        left.add(a)
        left.add(b)
        if a not in dists:
            dists[a] = {}
        if b not in dists:
            dists[b] = {}
        dists[a][b] = int(d)
        dists[b][a] = int(d)

    def dists_from(city, left, f):
        if len(left) == 0:
            return 0
        return f([dists[city][target] + dists_from(target, left - set([target]), f) for target in left])

    print(min([dists_from(city, left - set([city]), min) for city in left]))
    print(max([dists_from(city, left - set([city]), max) for city in left]))
