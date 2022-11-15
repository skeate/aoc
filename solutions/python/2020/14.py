from typing import List
from itertools import combinations
import re

def run(inp: List[str]):
    mem = {}
    for line in inp:
        if line.startswith('mask'):
            new_mask = line.split(' ')[2]
            bm_and = 0
            bm_or = 0
            for c in new_mask.strip():
                bm_and = bm_and << 1
                bm_or = bm_or << 1
                if c != '0':
                    bm_and |= 1
                if c == '1':
                    bm_or |= 1
        else:
            res = re.search(r'mem\[(\d+)\] = (\d+)', line)
            addr = int(res.group(1))
            val = int(res.group(2))
            mem[addr] = (val & bm_and) | bm_or
    print(sum(mem.values()))


    mem = {}
    for line in inp:
        if line.startswith('mask'):
            new_mask = line.split(' ')[2]
            am_or = 0
            am_flt = set()
            for i, c in enumerate(new_mask.strip()):
                am_or = am_or << 1
                if c == 'X':
                    am_flt.add(35-i)
                if c == '1':
                    am_or |= 1
        else:
            res = re.search(r'mem\[(\d+)\] = (\d+)', line)
            addr = int(res.group(1))
            val = int(res.group(2))
            cs = (c for r in range(len(am_flt) + 1) for c in combinations(am_flt, r))
            for c in cs:
                addr_ = addr | am_or
                for x in am_flt:
                    if x in c:
                        addr_ |= 1 << x
                    else:
                        addr_ &= ~(1 << x)
                mem[addr_] = val
            # print(mem)
    print(sum(mem.values()))
