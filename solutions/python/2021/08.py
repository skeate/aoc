from typing import List

def q(s: set[str]) -> str:
    return list(s)[0]

def map_segments(nums: List[str]):
    ss = [set(s) for s in sorted(nums, key=lambda s: len(s))]
    cf = ss[0]
    acf = ss[1]
    bcdf = ss[2]
    abcdefg = ss[9]

    a = acf - cf
    bd = (bcdf - cf)
    aeg = abcdefg - bcdf
    and_cf = [s & cf for s in ss if len(s & cf) == 1]
    pair = [and_cf[0], set(q(k) for k in and_cf) - and_cf[0]]
    c, f = pair if and_cf.count(and_cf[0]) == 1 else reversed(pair)
    acdeg = [s for s in ss if len(s) == 5 and q(f) not in s and q(c) in s][0]
    abdfg = [s for s in ss if len(s) == 5 and q(f) in s and q(c) not in s][0]
    # acdfg = [s for s in ss if len(s) == 5 and q(f) in s and q(c) in s][0]
    g = abdfg - bd - a - f
    e = aeg - a - g
    b = bcdf - acdeg - f
    d = bd - b

    return {
        q(a): 'a',
        q(b): 'b',
        q(c): 'c',
        q(d): 'd',
        q(e): 'e',
        q(f): 'f',
        q(g): 'g',
    }


segments_to_number = {
    frozenset({ 'a', 'b', 'c', 'e', 'f', 'g' }):      0,
    frozenset({ 'c', 'f' }):                          1,
    frozenset({ 'a', 'c', 'd', 'e', 'g' }):           2,
    frozenset({ 'a', 'c', 'd', 'f', 'g' }):           3,
    frozenset({ 'b', 'c', 'd', 'f' }):                4,
    frozenset({ 'a', 'b', 'd', 'f', 'g' }):           5,
    frozenset({ 'a', 'b', 'd', 'e', 'f', 'g' }):      6,
    frozenset({ 'a', 'c', 'f' }):                     7,
    frozenset({ 'a', 'b', 'c', 'd', 'e', 'f', 'g' }): 8,
    frozenset({ 'a', 'b', 'c', 'd', 'f', 'g' }):      9,
}

def run(inp: List[str]):
    outputs = [s.split('|')[1].strip().split(' ') for s in inp]
    print(sum(len(list(x for x in output if len(x) in [2, 4, 3, 7])) for output in outputs))

    digits = [s.split('|')[0].strip().split(' ') for s in inp]
    total = 0
    for out, dig in zip(outputs, digits):
        smap = map_segments(dig)
        total += int(''.join(str(segments_to_number[frozenset(smap[c] for c in o)]) for o in out))
    print(total)
