import re
from typing import List

def valid(s: str):
    m = re.search(r'(\d+)-(\d+) (\w): (\w+)', s)
    low = int(m.group(1))
    high = int(m.group(2))
    l = m.group(3)
    pw = m.group(4)

    return low <= pw.count(l) <= high

def valid2(s: str):
    m = re.search(r'(\d+)-(\d+) (\w): (\w+)', s)
    low = int(m.group(1))
    high = int(m.group(2))
    l = m.group(3)
    pw = m.group(4)

    lm = pw[low-1] == l
    hm = pw[high-1] == l
    return (lm or hm) and not (lm and hm)

def run(inp: List[str]):
    print(len([p for p in inp if valid(p)]))
    print(len([p for p in inp if valid2(p)]))
