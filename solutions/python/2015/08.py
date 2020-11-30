from typing import List

def convert(c):
    if c == '"':
        return '\\"'
    if c == '\\':
        return '\\\\'
    return c

def run(inp: List[str]):
    inp = [x.strip() for x in inp]
    chars = sum([len(x) for x in inp])
    chars2 = sum([len(eval(x)) for x in inp])
    chars3 = sum([2 + len(''.join([convert(c) for c in x])) for x in inp])

    print(chars - chars2)
    print(chars3 - chars)
