from typing import List

def get_overlaps(lines):
    g = {}
    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2
        horiz = y1 == y2
        vert = x1 == x2
        diag = not horiz and not vert
        mlen = max(abs(y2 - y1), abs(x2 - x1)) + 1
        dx = 1 if x2 >= x1 else -1
        dy = 1 if y2 >= y1 else -1
        xs = list(range(x1, x2 + dx, dx)) if horiz or diag else [x1] * mlen
        ys = list(range(y1, y2 + dy, dy)) if vert or diag else [y1] * mlen
        for p in zip(xs, ys):
            if p in g:
                g[p] += 1
            else:
                g[p] = 1
    return len([x for x in g.values() if x > 1])

def run(inp: List[str]):
    lines = [
        (tuple(map(int, p[0].split(","))), tuple(map(int, p[1].split(","))))
        for p in [i.split(" -> ") for i in inp]
    ]
    ortho_lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
    print(get_overlaps(ortho_lines))
    print(get_overlaps(lines))
