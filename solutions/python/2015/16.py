from typing import List
import re

def run(inp: List[str]):
    matcher = re.compile(r': (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
    things = (matcher.findall(s)[0] for s in inp)
    sues = [{ a: int(b), c: int(d), e: int(f)} for a,b,c,d,e,f in things]
    target_sue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    possible_sues = [(i + 1, sues[i]) for i in range(len(sues))]

    for prop,amt in target_sue.items():
        possible_sues = [ps for ps in possible_sues if prop not in ps[1] or ps[1][prop] == amt]
    print(possible_sues[0][0])

     
    possible_sues = [(i + 1, sues[i]) for i in range(len(sues))]

    for prop,amt in target_sue.items():
        possible_sues = [ps for ps in possible_sues if prop not in ps[1] or (
            ps[1][prop] > amt if prop in ('cats', 'trees') else
            ps[1][prop] < amt if prop in ('pomeranians', 'goldfish') else
            ps[1][prop] == amt)]
    print(possible_sues[0][0])
