from typing import List
import operator
import re

def matching_paren(l, i):
    parens = 0
    for k in range(i+1, len(l)):
        if l[k] == '(':
            parens += 1
        elif l[k] == ')':
            parens -= 1
            if parens < 0:
                return k

def process(l):
    l = l.strip()
    ans = 0
    i = 0
    op = operator.add
    while i < len(l):
        c = l[i]
        if c == '(':
            mp = matching_paren(l, i)
            ans = op(ans, process(l[i + 1:mp]))
            i = mp
        elif c == '+':
            op = operator.add
        elif c == '*':
            op = operator.mul
        elif c == ' ':
            pass
        else:
            ans = op(ans, int(c))
        i += 1
    return ans

class Num(int):
    def __init__(self, n):
        self.n = n

    def repr(self):
        return self.n

    def __add__(self, n):
        return Num(self.n * n.repr())

    def __radd__(self, n):
        return Num(self.n * n.repr())

    def __mul__(self, n):
        return Num(self.n + n.repr())

    def __rmul__(self, n):
        return Num(self.n + n.repr())

def process_flipped(l):
    l = re.sub(r'(\d)', r'Num(\1)', l)
    l = re.sub(r'\+', r'_', l)
    l = re.sub(r'\*', r'+', l)
    l = re.sub(r'_', r'*', l)
    # print(l)
    return eval(l).repr()

def run(inp: List[str]):
    print(sum(process(l) for l in inp))
    print(sum(process_flipped(l) for l in inp))
