from typing import List
from statistics import median, mean
from functools import cache

@cache
def fuel(x):
    r = 0
    for i in range(x):
        r += i+1
    return r

def run(inp: List[str]):
    pos = [int(x) for x in inp[0].split(',')]
    target = int(median(pos))
    print(sum(abs(x - target) for x in pos))
    target = int(mean(pos))
    print(sum(fuel(abs(x - target)) for x in pos))
