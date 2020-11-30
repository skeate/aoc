from itertools import groupby
from typing import List

def las(n):
    return ''.join([str(len(list(c))) + x for x, c in groupby(n)])

def run(inp: List[str]):
    input = inp[0].strip()
    lased_input = input
    for i in range(40):
        lased_input = las(lased_input)
    print(len(lased_input))
    for i in range(10):
        lased_input = las(lased_input)
    print(len(lased_input))
