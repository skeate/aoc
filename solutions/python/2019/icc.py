import sys
from time import sleep

opcode = {
    1:  ('add',    3),
    2:  ('mult',   3),
    3:  ('input',  1),
    4:  ('output', 1),
    5:  ('jnz',    2),
    6:  ('jz',     2),
    7:  ('lt',     3),
    8:  ('eq',     3),
    9:  ('rela',   1),
    99: ('halt',   0),
}

namel = max(len(x[0]) for x in opcode.values())

class ddict(dict):
    def __missing__(self, key):
        self[key] = 0
        return 0

class ICC:
    def __init__(self, code, iq, oq, id='', debug = False, default_input = None):
        self.orig_code = code
        self.code = {}
        self.iq = iq
        self.oq = oq
        self.debug = debug
        self.id = id
        self.relbase = 0
        self.default_input = default_input

    def run(self, continuous=False):
        while True:
            self.ip = 0
            self.code = ddict({i: p for i,p in enumerate(self.orig_code)})
            while self.ip is not None:
                self.ip = self.execute_instruction()
            if not continuous:
                break

    def amsg(self, s):
        print(f'[ICC-{self.id}] {s}')

    def dmsg(self, s):
        if self.debug:
            self.amsg(s)

    def execute_instruction(self):
        full_op = self.code[self.ip]
        op = full_op % 100
        name, args = opcode[op]
        modes = [
            ((full_op // 10 ** i) % 10)
            for i in range(2, 2 + args)
        ]
        params = [self.code[self.ip + x] for x in range(1, 1 + args)]
        dest = params[-1] if len(params) > 0 else 0
        dest += self.relbase if len(modes) > 0 and modes[-1] == 2 else 0
        vals = [a if m == 1 else (self.code[a] if m == 0 else self.code[a + self.relbase]) for a,m in zip(params, modes)]

        if op not in opcode:
            self.amsg(f'unknown opcode {op} at pos {self.ip}')
            return None

        self.dmsg(f'{self.ip:>4} {name:>{namel}} ' +
                  f'{", ".join(str(p) + ("_i" if m == 1 else f"_r({v})" if m == 2 else f"({v})") for m,p,v in zip(modes, params, vals))}'
                  )

        if name == 'halt':
            return None

        elif name == 'add':
            self.code[dest] = vals[0] + vals[1]

        elif name == 'mult':
            self.code[dest] = vals[0] * vals[1]

        elif name == 'input':
            if self.default_input is not None:
                try:
                    self.code[dest] = self.iq.get_nowait()
                except:
                    self.code[dest] = self.default_input
                sleep(.000001)
            else:
                self.code[dest] = self.iq.get()

        elif name == 'output':
            self.oq.put(vals[0])

        elif name == 'jnz':
            if vals[0] != 0:
                return vals[1]

        elif name == 'jz':
            if vals[0] == 0:
                return vals[1]

        elif name == 'lt':
            self.code[dest] = 1 if vals[0] < vals[1] else 0

        elif name == 'eq':
            self.code[dest] = 1 if vals[0] == vals[1] else 0

        elif name == 'rela':
            self.relbase += vals[0]
            self.dmsg(f'relative base now {self.relbase}')

        return self.ip + 1 + args


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: icc.py <intcode file> [...inputs]')
        exit(1)
    with open(sys.argv[1]) as f:
        intcode = [int(x) for x in f.read().strip().split(',')]

    class IOStream:
        def __init__(self):
            self.ap = 2
            self.remaining = ''

        def get(self):
            if len(self.remaining) > 0:
                x, self.remaining = self.remaining[0], self.remaining[1:]
                return ord(x)
            if len(sys.argv) > self.ap:
                a = sys.argv[self.ap]
                self.ap += 1
                return int(a)
            self.remaining = input() + '\n'
            x, self.remaining = self.remaining[0], self.remaining[1:]
            return ord(x)
        def put(self, x):
            print(chr(x), end='')

    io = IOStream()

    icc = ICC(intcode, io, io, debug = False)
    icc.run()
