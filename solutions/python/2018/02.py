from typing import List
from collections import Counter
import itertools

def diff(s1: str, s2: str):
    return sum([1 for c1, c2 in zip(s1, s2) if c1 != c2])

def same(s1: str, s2: str):
    return ''.join([c1 for c1, c2 in zip(s1, s2) if c1 == c2])

def run(inp: List[str]):
    twos = len([x for x in inp if 2 in Counter(x).values()])
    threes = len([x for x in inp if 3 in Counter(x).values()])
    print(twos * threes)

    for s1, s2 in itertools.permutations(inp, 2):
        if diff(s1, s2) == 1:
            print(same(s1,s2))
            exit()
