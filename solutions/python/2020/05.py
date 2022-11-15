from typing import List

def to_binary(s: str):
    return int(s.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)

def run(inp: List[str]):
    passes = set([to_binary(p) for p in inp])
    print(max(passes))
    for p in range(8, 2**10 - 8):
        if p not in passes and (p+1) in passes and (p-1) in passes:
            print(p)
            break
