from typing import List

# dx, dy
# E S W N
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
cds = 'ESWN'

def run(inp: List[str]):
    moves = [(m[0], int(m[1:])) for m in inp]
    facing = 0
    x = 0
    y = 0
    for d, l in moves:
        if d in cds:
            tf = cds.index(d)
        elif d == 'L':
            facing = int(facing - l / 90) % 4
            tf = facing
            l = 0
        elif d == 'R':
            facing = int(facing + l / 90) % 4
            tf = facing
            l = 0
        else:
            tf = facing
        x += l * dirs[tf][0]
        y += l * dirs[tf][1]
    print(abs(x) + abs(y))

    wpx = 10
    wpy = 1
    x = 0
    y = 0
    for d, l in moves:
        if d in cds:
            wpx += l * dirs[cds.index(d)][0]
            wpy += l * dirs[cds.index(d)][1]
        elif d == 'L':
            while (l / 90) > 0:
                wpx, wpy = -wpy, wpx
                l -= 90
        elif d == 'R':
            while (l / 90) > 0:
                wpx, wpy = wpy, -wpx
                l -= 90
        else:
            x += l * wpx
            y += l * wpy
    print(abs(x) + abs(y))
