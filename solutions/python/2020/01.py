from typing import List

def sump(inp):
    for i in inp:
        if 2020 - i in inp:
            return i * (2020 - i)

def sump2(inp):
    for i in inp:
        for j in inp:
            if 2020 - (i + j) in inp:
                return i * j * (2020 - (i+j))

def run(inp: List[str]):
    inp = set([*map(int, inp)])
    print(sump(inp))
    print(sump2(inp))
