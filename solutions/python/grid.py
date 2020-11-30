import os
from itertools import zip_longest

def same(x): return x
def noop(a,b): pass

class Grid:
    def __init__(self, visit=noop, start=(0,0)):
        self.grid = {}
        self.loc = start
        self._visit = visit
        self.grid[start] = self.visit()

    def visit(self):
        return self._visit(self.grid, self.loc)

    def setPos(self, loc):
        self.loc = loc
        self.grid[loc] = self.visit()

    def move(self, dloc):
        oldLoc = self.loc
        self.loc = tuple(sum(x) for x in zip_longest(self.loc, dloc, fillvalue=0))
        self.grid[self.loc] = self.visit()

    def slide_x(self, dx):
        neg = dx < 0
        for x in range(1, abs(dx) + 1):
            if neg: self.left()
            else: self.right()

    def slide_y(self, dy):
        neg = dy < 0
        for y in range(1, abs(dy) + 1):
            if neg: self.down()
            else: self.up()

    def slide_z(self, dz):
        neg = dz < 0
        for z in range(1, abs(dz) + 1):
            if neg: self.backward()
            else: self.forward()

    def up(self):
        self.move((1,))
    def down(self):
        self.move((-1,))
    def left(self):
        self.move((0,-1))
    def right(self):
        self.move((0,1))
    def forward(self):
        self.move((0,0,1))
    def backward(self):
        self.move((0,0,-1))

    def display(self, flipx=False, flipy=False, trans=lambda x:x, mark=None):
        minx = min(c[0] for c in self.grid.keys())
        miny = min(c[1] for c in self.grid.keys())
        maxx = max(c[0] for c in self.grid.keys())
        maxy = max(c[1] for c in self.grid.keys())
        rows = maxy - miny + 1
        cols = maxx - minx + 1
        tty_rows, tty_cols = (int(d) for d in os.popen('stty size', 'r').read().split())
        if tty_cols < cols:
            print(f'Grid ({rows} x {cols}) too large for terminal ({tty_rows} x {tty_cols})')
        else:
            ordery = reversed if flipy else same
            orderx = reversed if flipx else same
            for y in ordery(range(miny, maxy + 1)):
                for x in orderx(range(minx, maxx + 1)):
                    if (x,y) == mark:
                        print('x', end='')
                    elif (x,y) in self.grid:
                        print(trans(self.grid[(x,y)]), end='')
                    else:
                        print(' ', end='')
                print()
