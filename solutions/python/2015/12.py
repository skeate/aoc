from typing import List
import re
import json

def sum_non_red(x):
    if type(x) == list:
        return sum(sum_non_red(z) for z in x)
    if type(x) == dict:
        if 'red' in x.values():
            return 0
        return sum(sum_non_red(z) for z in x.values())
    if type(x) == str:
        return 0
    return x

def run(inp: List[str]):
    x = inp[0].strip()
    nums = [int(n) for n in re.findall(r'-?\d+', x)]
    print(sum(nums))

    y = json.loads(x)
    print(sum_non_red(y))
