from typing import List
from itertools import groupby
from collections import Counter

def valid(m, mx):
    l = 0
    for r in m:
        if r - l > 3 or r - l < 1:
            return False
        l = r
    if mx - l > 3 or mx - l < 1:
        return False
    return True


def count(m):
    """
    this works by checking the deltas between numbers. turns out all the inputs
    have deltas of 1 or 3, never 2. so we wind up with patterns like
    (1, 1, 1, 3, 1, 1, 3)
    the 3s represent gaps that invalidate the sequence if either side (left or
    right of gap) is removed, so we can essentially subdivide the whole thing at
    those points

    then we have (1,1,1) and (1,1). however many variations of those, multiply
    them together, you get your answer.

    (1,)      = 1 variation (either side is a 3 gap, so we can't remove them)
    (1,1)     = 2 variations
    (1,1,1)   = 4 variations
    (1,1,1,1) = 7 variations

    so count the subsequences, use power operator, get answer.
    """
    diffs = []
    for i in range(1, len(m) - 1):
        diffs.append(m[i] - m[i-1])
    c = Counter([len(list(l)) for i,l in groupby(diffs) if i == 1])
    return 2 ** c[2] * 4 ** c[3] * 7 ** c[4]


def run(inp: List[str]):
    inp = [0, *map(int, inp)]
    inp.sort()
    inp.append(max(inp) + 3)
    ones = 0
    threes = 0
    for i in range(1, len(inp)):
        diff = inp[i] - inp[i-1]
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1

    print(ones*threes)
    print(count(inp))
