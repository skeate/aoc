from typing import List

def run(inp: List[str]):
    v = { orbiter: set([center]) for center,orbiter in [p.strip().split(')') for p in inp]}

    def finish(orbiter):
        if 'COM' not in v[orbiter]:
            v[orbiter] |= finish(*v[orbiter])
        return v[orbiter]

    for orbiter, orbitees in v.items():
        finish(orbiter)

    ans1 = sum(len(x) for x in v.values())

    ans2 = len(v['YOU'] ^ v['SAN'])

    print(ans1)

    print(ans2)
