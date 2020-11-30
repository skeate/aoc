import re
from typing import List

def run(inp: List[str]):
    v = ''.join(inp)

    r = re.compile(r'(?:([a-z0-9]+) )?(?:(OR|AND|LSHIFT|RSHIFT|NOT) )?([a-z0-9]+)')

    def parse(x):
        src, dst = x.split(' -> ')
        try:
            a, op, b = r.match(src).groups()
        except:
            print(src,dst)
            exit(1)
        return (dst, a, op, b)


    v = [parse(x) for x in v.strip().split('\n')]

    regs = {}
    for dst,a,op,b in v:
        regs[dst] = (op, a, b)

    def calc(reg, regs):
        if type(regs[reg]) is tuple:
            op, a, b = regs[reg]
            if a is not None:
                try:
                    a = int(a)
                except:
                    a = calc(a, regs)
            try:
                b = int(b)
            except:
                b = calc(b, regs)

            if op == 'RSHIFT': regs[reg] = a >> b
            elif op == 'LSHIFT': regs[reg] = a << b
            elif op == 'AND': regs[reg] = a & b
            elif op == 'OR': regs[reg] = a | b
            elif op == 'NOT': regs[reg] = ~b
            else: regs[reg] = b
        return regs[reg]

    ans1 = calc('a', regs)
    print(ans1)

    regs = {}
    for dst,a,op,b in v:
        regs[dst] = (op, a, b)

    regs['b'] = ans1

    print(calc('a', regs))
