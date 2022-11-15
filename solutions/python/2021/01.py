from typing import List

def increases(l):
    increases = 0
    for i, j in zip(l, l[1:]):
        if j > i:
            increases += 1
    return increases

def run(inp: List[str]):
    depths = [int(x) for x in inp]
    print(increases(depths))

    summed_depths = [x + y + z for x,y,z in zip(depths, depths[1:], depths[2:])]
    print(increases(summed_depths))
