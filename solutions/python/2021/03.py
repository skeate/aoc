from typing import List
from statistics import multimode

def mode(ns: List[int], favor: int):
    modes = multimode(ns)
    if len(modes) == 1:
        return modes[0] if favor == 1 else ((~modes[0]) & 1)
    return favor

def iths(ns: List[List[int]], i: int):
    return [n[i] for n in ns]

def search(nums: List[List[int]], k: int):
    cur_nums = nums
    for i in range(len(nums[0])):
        bit = mode(iths(cur_nums, i), k)
        cur_nums = list(filter(lambda n: n[i] == bit, cur_nums))
        if len(cur_nums) == 1:
            return int(''.join([str(i) for i in cur_nums[0]]), 2)

def run(inp: List[str]):
    nums = [[int(l) for l in s.strip()] for s in inp]
    matrix = [[int(s[i]) for s in inp] for i in range(len(inp[0].strip()))]
    gamma = int(''.join([str(mode(i, 1)) for i in matrix]), 2)
    epsilon = gamma ^ 0b111111111111
    print(epsilon * gamma)

    oxy = search(nums, 1)
    co2 = search(nums, 0)
    print(oxy * co2)
