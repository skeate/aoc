from typing import List

def run(inp: List[str]):
    s = sum(int(s) // 3 - 2 for s in inp)
    print(s)

    total = 0
    for x in inp:
        m = int(x) // 3 - 2
        while m > 0:
            total += m
            m = max(0,m // 3 - 2)
    print(total)
