from typing import List

def ll(arr):
    nexts = (len(arr) + 1) * [-1]
    for n,nx in zip(arr, arr[1:] + (arr[0],)):
        nexts[n] = nx
    return nexts

def move(cur, cs):
    next_three = (cs[cur], cs[cs[cur]], cs[cs[cs[cur]]])
    prev = cur - 1
    while prev == 0 or prev in next_three:
        prev -= 1
        if prev <= 0:
            prev = len(cs) - 1
    next = cs[cur]
    third = cs[cs[cs[cur]]]
    cs[cur], cs[third], cs[prev] = cs[third], cs[prev], next
    return cs[cur]

def pprint(cur, cs):
    acc = str(cur)
    n = cs[cur]
    while n != cur:
        acc += str(n)
        n = cs[n]
    return acc

def run(inp: List[str]):
    inp = tuple(int(c) for c in inp[0].strip())
    c = inp[0]
    cs = ll(inp)
    for _ in range(100):
        c = move(c, cs)
    print(pprint(1, cs)[1:])

    cs = ll(inp + tuple(range(10, 1_000_001)))
    c = inp[0]
    for _ in range(10_000_000):
        c = move(c, cs)
    print(cs[1] * cs[cs[1]])
