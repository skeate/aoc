from typing import List

def round(p1, p2, winner=lambda x,y: 1 if x[0] > y[0] else 2):
    if winner(p1, p2) == 1:
        return (tuple([*p1[1:], p1[0], p2[0]]), p2[1:])
    else:
        return (p1[1:], tuple([*p2[1:], p2[0], p1[0]]))

def score(p):
    total = 0
    for i, pi in enumerate(reversed(p)):
        total += (i + 1) * pi
    return total


def recgame(p1, p2):
    p1cache = set()
    p2cache = set()

    # print('recgame', p1, p2)

    def recround(p1, p2):
        if p1 in p1cache or p2 in p2cache:
            return 1
        p1cache.add(p1)
        p2cache.add(p2)
        if p1[0] <= len(p1) - 1 and p2[0] <= len(p2) - 1:
            sp1, sp2 = recgame(p1[1:1 + p1[0]], p2[1:1 + p2[0]])
            return 1 if sp1 > sp2 else 2
        return 1 if p1[0] > p2[0] else 2

    while len(p1) != 0 and len(p2) != 0:
        p1, p2 = round(p1, p2, winner=recround)
    return (score(p1), score(p2))


def run(inp: List[str]):
    div = inp.index('\n')
    p1 = tuple([int(t) for t in inp[1:div]])
    p2 = tuple([int(t) for t in inp[div + 2:]])

    while len(p1) != 0 and len(p2) != 0:
        p1, p2 = round(p1, p2)

    print(max(score(p1), score(p2)))

    p1 = tuple([int(t) for t in inp[1:div]])
    p2 = tuple([int(t) for t in inp[div + 2:]])

    print(max(recgame(p1, p2)))
